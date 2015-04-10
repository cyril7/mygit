#!/usr/bin/python
# -*- coding: utf-8 -*-
import smtplib
import string
 
HOST = "smtp.qq.com"
SUBJECT = "Test email from Python"
TO = "abc@aliyun.com"
FROM = "abc@qq.com"
text = "Python rules them all!"
BODY = string.join((
        "From: %s" % FROM,
        "To: %s" % TO,
        "Subject: %s" % SUBJECT ,
        "",
        text
        ), "\r\n")
server = smtplib.SMTP()

# 25 端口
server.connect(HOST,"25")

# 启用TLS模式,使用GMAIL的SMTP服务时需要启动此项才能正常发邮件
# server.starttls()

server.login("abc@qq.com","abc789")
server.sendmail(FROM, [TO], BODY)
server.quit()
