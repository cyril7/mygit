#!/usr/bin/python
# -*- coding: utf-8 -*-
import commands
import smtplib
from email.mime.multipart import MIMEMultipart  #导入MIMEMultipart类  
from email.mime.text import MIMEText    	#导入MIMEText类  

DIR = "/tmp/diskmonitor"
HTML = DIR + "/report.html"
HOST = "smtp.139.com"
SUBJECT = "Disk Usage Routine Inspection"
TO = "abc@139.com"
FROM = "13333@139.com"

try:
    f = open(HTML, "r")
    html = f.read()
finally:
    if f:
        f.close()


msg = MIMEMultipart()
msg.attach(MIMEText(html, 'html', "utf-8")) 


msg['Subject'] = SUBJECT    	#邮件主题  
msg['From'] = FROM    		#邮件发件人,邮件头部可见  
#msg['To']=",".join(TO)  		#当收件人为多个时
msg['To']=TO                            #当收件人为一个时
try:
 
    ## test connection
    tserver = smtplib.SMTP()
    tserver.connect(HOST,"25")
    tserver.quit()

    server=smtplib.SMTP()
    server.connect(HOST,"25")
    #server.starttls()
    server.login("133@139.com","abc")
    server.sendmail(FROM, [TO], msg.as_string()) #当收件人为一个时
    #server.sendmail(FROM, TO, msg.as_string())    #当收件人为多个时
    server.quit()
    print "success_to_send_email"
except Exception,e:
    print "fail_:"+str(e)
