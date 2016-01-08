#!/usr/bin/python
# -*- coding: utf-8 -*-
# Plain Emails with python script
# Author: fengzc
# For omd Flexible Notification from Check_MK
# OMD[gzhlgz]:~/local/share/check_mk/notifications$

import os, sys, re, smtplib, string, commands

# to ==> could be list ['a@a.com', 'b@b.com']
def sendmail(subject, to, content):
    HOST = "mail.bingosoft.net"
    SUBJECT = subject
    TO = to
    FROM = "cloud-monitor@bingosoft.net"
    CONTENT = content
    BODY = string.join((
        "From: %s" % FROM,
        "TO: %s" % TO,
        "Subject: %s" % SUBJECT,
        "",
        CONTENT
        ), "\r\n")
    server = smtplib.SMTP()
    server.connect(HOST,"25")
    server.starttls()
    server.login(FROM, "pass@word2")
    server.sendmail(FROM, TO, BODY)
    server.quit()

#
# HOST TEMPLATES
#

tmpl_host_subject = 'Check_MK: $HOSTNAME$ - $NOTIFICATIONTYPE$'

tmpl_host_txt = '''
Date:     $SHORTDATETIME$
Host:     $HOSTNAME$ ($HOSTALIAS$)
Address:  $HOSTADDRESS$
State:    $LASTHOSTSTATE$ -> $HOSTSTATE$ ($NOTIFICATIONTYPE$)
Output:   $HOSTOUTPUT$
Perfdata: $HOSTPERFDATA$
$LONGHOSTOUTPUT$
'''
#URL:      http://10.200.84.152:8888/$OMD_SITE$$HOSTURL$

tmpl_service_subject = 'Check_MK: $HOSTNAME$/$SERVICEDESC$ $NOTIFICATIONTYPE$'

tmpl_service_txt = '''
Date:     $SHORTDATETIME$
Host:     $HOSTNAME$ ($HOSTALIAS$)
Address:  $HOSTADDRESS$
Service:  $SERVICEDESC$
State:    $LASTSERVICESTATE$ -> $SERVICESTATE$ ($NOTIFICATIONTYPE$)
Output:   $SERVICEOUTPUT$
Perfdata: $SERVICEPERFDATA$
$LONGSERVICEOUTPUT$
'''
#URL:      http://10.200.84.152:8888/$OMD_SITE$$SERVICEURL$

def substitute_context(template, context):
    # First replace all known variables
    for varname, value in context.items():
        template = template.replace('$'+varname+'$', value)

    # Remove the rest of the variables and make them empty
    template = re.sub("\$[A-Z]+\$", "", template)
    return template

def prepare_contents(context):
    if context['WHAT'] == 'HOST':
        tmpl_txt  = tmpl_host_txt
    else:
        tmpl_txt  = tmpl_service_txt

    return substitute_context(tmpl_txt, context)

                        
def main():
    # gather all options from env
    #fh = open("/tmp/mkmail.log", "a")
    #  'NOTIFY_WHAT': u'SERVICE' 
    # context = dict([(var[7:], value.decode("utf-8")) for (var, value) in os.environ.items() if var.startswith("NOTIFY_")])
    # utf-8 decode would throw a error while there is chinese character in environ.items()
    context = dict([(var[7:], value) for o(var, value) in os.environ.items() if var.startswith("NOTIFY_")])
    #fh.write("\n" + str(context) + "\n")
    #fh.close()

    if context['WHAT'] == 'HOST':
        context['SUBJECT'] = substitute_context(tmpl_host_subject, context)
    else:
        context['SUBJECT'] = substitute_context(tmpl_service_subject, context)

    # Prepare the mail contents
    content_txt = prepare_contents(context)

    # send mail
    mail_receivers = {"ops": "ops@a.net", "fengzc": "12@139.com", "ye": "13@139.com"}
    sendmail(context['SUBJECT'], mail_receivers.values(), content_txt)
    
main()
