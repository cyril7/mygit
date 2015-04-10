#!/usr/bin/python
# -*- coding: utf-8 -*-

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

HOST = "smtp.qq.com"
SUBJECT = u"官网业务服务质量周报"
TO = "abc@aliyun.com"
FROM = "abc@qq.com"

# 读取图片
def addimg(src,imgid):
    fp = open(src, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', imgid)
    return msgImage

# 定义mixed实现构建一个带附件的邮件体
# 定义related实现构建内嵌资源的邮件体
# 定义alternative实现构建纯文本于超文本共存的邮件体
msg = MIMEMultipart('related')

msgtext = MIMEText("<font color=red>官网业务周平均延时图表:<br><img src=\"cid:weekly\" border=\"1\"><br>详细内容见附件。</font>","html","utf-8")
msg.attach(msgtext)
msg.attach(addimg("img/weekly.png","weekly"))

# 附加文档
attach = MIMEText(open("doc/week_report.xlsx", "rb").read(), "base64", "utf-8")
attach["Content-Type"] = "application/octet-stream"

# 由于qqmail 使用gb18030页面编码,为了保证中文文件名不出现乱码,对文件名进行编码转换
attach["Content-Disposition"] = "attachment; filename=\"业务服务质量周报(12周).xlsx\"".decode("utf-8").encode("gb18030")
msg.attach(attach)

msg['Subject'] = SUBJECT
msg['From']=FROM
msg['To']=TO
try:
    server = smtplib.SMTP()
    server.connect(HOST,"25")

    # Gmail 发送服务才需要TLS    
    #server.starttls()    

    server.login("abc@qq.com","abc789")    
    server.sendmail(FROM, TO, msg.as_string())
    server.quit()
    print "邮件发送成功！"
except Exception, e:  
    print "失败："+str(e) 
