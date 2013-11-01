#coding:utf-8
import urllib2
#from bs4 import BeautifulSoup
import BeautifulSoup

# soup = BeautifulSoup(urllib2.urlopen('http://www.qiushibaike.com/8hr').read())
#soup = BeautifulSoup(urllib2.urlopen('http://blog.pkufranky.com/2011/11/使用vim和markdown撰写blog并发布到wordpress/').read())
soup = BeautifulSoup(urllib2.urlopen('http://www.cnblogs.com/dotey/archive/2011/06/09/2075954.html').read())
for result in soup.findAll("div", "postTitle" ):
    print result.text
