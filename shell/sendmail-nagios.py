#!/usr/local/bin/python
import smtplib
import string
import sys
import getopt

def usage():
   print """sendmail is a send mail Plugins
   Usage:

   sendmail [-h|--help][-t|--to][-s|--subject][-m|--message]

   Options:
          --help|-h)
                 print sendmail help.
          --to|-t)
                 Sets sendmail to email.
          --subject|-s)
                  Sets the mail subject.
          --message|-m)
                  Sets the mail body
    Example:
           only one to email  user
          ./1.py -t 'xxx@126.com' -s 'hello xxx' -m 'hello deng,this is sendmail test!
           many to email  user
          ./1.py -t 'xxx@163.com,xxx@126.com' -s 'hello xxx' -m 'hello xx,this is sendmail test!"""
   sys.exit(3)

try:
   options,args = getopt.getopt(sys.argv[1:],"ht:s:m:",["help","to=","subject=","message="])
except getopt.GetoptError:
   usage()
for name,value in options:
    if name in ("-h","--help"):
       usage()
    if name in ("-t","--to"):
# accept message user
       TO = value
       TO = TO.split(",")
    if name in ("-s","--title"):
       SUBJECT = value
    if name in ("-m","--message"):
       MESSAGE = value
       MESSAGE = MESSAGE.split('\\n')
       MESSAGE = '\n'.join(MESSAGE)

#smtp HOST
HOST = "mail.cc.net"               
#smtp port
PORT = "25"               
#FROM mail user
USER = 'monitor@cc.net'                              
#FROM mail password
PASSWD = 'pass'
#FROM EMAIL
FROM = "monitor@cc.net"    


BODY = string.join((
    "From: %s" % FROM,
    "To: %s" % TO,
    "Subject: %s" % SUBJECT,
    "",
    MESSAGE),"\r\n")

smtp = smtplib.SMTP()
smtp.connect(HOST,PORT)
smtp.starttls()
smtp.login(USER,PASSWD)
smtp.sendmail(FROM,TO,BODY)
smtp.quit()

"""
try:
   BODY = string.join((
      "From: %s" % FROM,
      "To: %s" % TO,
      "Subject: %s" % SUBJECT,
      "",
      MESSAGE),"\r\n")

   smtp = smtplib.SMTP()
   smtp.connect(HOST,PORT)
   smtp.starttls()
   smtp.login(USER,PASSWD)
   smtp.sendmail(FROM,TO,BODY)
   smtp.quit()
except:
   print "UNKNOWN ERROR"
   print "please look help"
   print "./1.py -h"


"""
