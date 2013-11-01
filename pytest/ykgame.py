#!/usr/bin/python
#coding=utf-8
'''
缘起：
上篇因为工作需要（就是把腾讯新闻copy到单位自己网站上去每天15条更新）所以写了一个抓取腾讯新闻的python小脚本
这次是因为想用手机看youku视频，比如xiaoy的魔兽解说，但是打开浏览器输入game.youku.com的时候，三星9003太不
给力，因而需要一个打开速度快的目录小网站。

思路：
1.数据表设计：
　　id(int),                    //主键自增
　　title(varchar 50),    //速度优先，只需要title，不需要图片
　　href(varchar 50),   //视频播放地址
　　date(varchar 25),  //采集的date中有如“1小时前”，因此也设计成varchar

2.采集函数设计：
　　视频列表页url = http://i.youku.com/u/UMTE0NDEzOTky/videos/order_1_view_1_page_id (id =1,2...)
　　每页视频个数为20，采集内容为title,href,date，优酷的html很规整，因此正则提取很好写，详见代码。

3.采集流程及入库：
　　采用多线程采集，开9个进程，每个进程提取一个列表页20个视频，总共采集180个视频，如果想全站采集的话修改即可。
　　数据库采用mysql，如何使python支持mysql详见Python网站建设，因为是多线程所以在插入数据的时候需要资源锁。
　　关于python多线程thread以及资源锁，可以参照Python模块学习。
'''
import urllib2
import re
#import MySQLdb
import sqlite3
import thread
import time
#创建锁，用于访问数据库
lock = thread.allocate_lock()
#抓取函数
def fetch(id=1,debug=False):
    urlbase = 'http://i.youku.com/u/UMTE0NDEzOTky/videos/'
    :Q
    :q

    url = urlbase + 'order_1_view_1_page_' + str(id) + '/'
    res = urllib2.urlopen(url).read()
    abstarct = re.compile(r'<ul class="v".*?</ul>',re.DOTALL).findall(res)
    
    vid_list = []
    for i in range(0,len(abstarct)):
        title = re.compile(r'title="(.*?)"',re.DOTALL).findall(abstarct[i])
        href = re.compile(r'href="(.*?)"',re.DOTALL).findall(abstarct[i])
        date = re.compile(r'<span>(.*?)</span>',re.DOTALL).findall(abstarct[i])
        if debug == True:
            print title[0]+href[0]+date[0]
        vid = {
            'title' : title[0],
            'href'  : href[0],
            'date'  : date[0]
        }
        vid_list.append(vid)
    print thread.get_ident()    
    return vid_list
#插入数据库
def insert_db(page):
    global lock
    #执行抓取函数
    vid_date = fetch(page,False)
    sql = "insert into ykgame (title,href,date) values (%s,%s,%s)"
    #插入数据，一页20条
    for i in range(0,len(vid_date)):
        param = (vid_date[i]['title'],vid_date[i]['href'],
                    vid_date[i]['date'])
        lock.acquire() #创建锁
        cursor.execute(sql,param)
        conn.commit()
        lock.release() #释放锁
                
if __name__ == "__main__":
    #连接数据库
    #conn = MySQLdb.connect(host="localhost",user="root",
    #        passwd="root",db="python_test",charset="utf8")
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    #conn.select_db('python_test')
    #创建表
    #sql = "CREATE TABLE IF NOT EXISTS \
    #    ykgame(id int PRIMARY KEY AUTO_INCREMENT, title varchar(50), \
    #    href varchar(50), date varchar(25))"        
    #cursor.execute(sql)
    #插入数据库
    for i in range(1,10):
        thread.start_new_thread(insert_db,(i,))
        print '采集中...'
    time.sleep(3)
    #关闭数据库
    cursor.close()
    conn.close()

'''
说明：
　　urllib2模块：进行网页内容抓取
　　re模块：进行正则表达式提取
　　MySQLdb模块：mysql操作
　　thread模块：多线程操作
　　time模块：time.sleep(3)

遇到的问题：
1.mysql中文乱码：问题比较复杂，通用解决办法如下
　　程序中只要在开头写好：#coding=utf-8
　　连接数据库的时候设置编码方式：conn=MySQLdb.connect(host="127.0.0.1",user="webdb",passwd="web123",db="web",charset="utf8")
      对于采集来的中文字符串，可以编码转换后插入str = str.decode("gbk").encode("utf-8")

2.Warning: Data truncated for column 'href' at row 1
　　原因：href 数据库中为 varchar(25)，而实际长度>25
　　解决办法：将href 数库中改为 varchar(50)

3.多线程问题：现象混乱有时候无报错，注意事项如下
　　使用相同资源是需要用资源锁，不然出现异常
　　线程处理时间短时，启用线程后加time.sleep(3)
'''
