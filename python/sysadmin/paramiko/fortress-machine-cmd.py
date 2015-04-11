#!/usr/bin/python
# -*- coding: utf-8 -*-

import paramiko
import os,sys,time

# 目标机器
hostname = "192.168.18.152"
username = "root"
password = "abc123"

# 堡垒机
blip = "192.168.18.100"
bluser = "root"
blpasswd = "abc123"

port = 22
# 服务器密码前的标志串
passinfo = '\'s password: '
paramiko.util.log_to_file('syslogin.log')

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname = blip, username = bluser, password = blpasswd)

#new session
# 创建会话,开启命令调用
channel = ssh.invoke_shell()
# 会话命令执行超时时间,10秒
channel.settimeout(10)

buff = ''
resp = ''
channel.send('ssh ' + username + '@' + hostname + '\n')

# ssh登录的提示信息判断,输出串尾含有'\'s password: '的时候退出WHILE循环
while not buff.endswith(passinfo):
    try:
        resp = channel.recv(9999)
    except Exception, e:
        print 'Error info:%s connection time.' % (str(e))
        channel.close()
        ssh.close()
        sys.exit()
    buff += resp
    if not buff.find('yes/no') == -1: # 输出串尾含有"yes/no"时发送"yes"并回车
        channel.send('yes\n')
	buff=''

channel.send(password + '\n') # 发送目标主机密码

buff=''
while not buff.endswith('# '): # "输出串尾为 # 时说明校验通过并退出while循环"
    resp = channel.recv(9999)
    if not resp.find(passinfo) == -1: # 输出串尾含有"\'s password:  " 说明密码不正确,要求重新输入
        print 'Error info: Authentication failed.'
        channel.close() # 关闭对象后退出
        ssh.close()
        sys.exit() 
    buff += resp

channel.send('ifconfig\n') # 认证通过后发送ifconfig命令来查看结果
buff=''
try: 
    while buff.find('# ')==-1:
        resp = channel.recv(9999)
        buff += resp
except Exception, e:
    print "error info:"+str(e)

print buff   # 打印输出串
channel.close()
ssh.close()
