#!/usr/bin/python
# -*- coding: utf-8 -*-

import paramiko
import os,sys,time

# 目标机器信息
hostname = "192.168.18.152"
username = "root"
password = "abc123"

# 堡垒机信息
blip = "192.168.18.100"
bluser = "root"
blpasswd = "abc123"

# 堡垒机存文件目录
tmpdir = "/tmp"
# 目标机器文件目录
remotedir = "/tmp/data"
# 用户主机上传的文件
localpath = "/tmp/pssh.tar.gz"
# 上传到堡垒机的文件路径
tmppath = tmpdir + "/pssh.tar.gz"
# 传输到目标主机后的文件路径
remotepath = remotedir + "/pssh_remote.tar.gz"

port=22
passinfo='\'s password: '
paramiko.util.log_to_file('syslogin.log')

t = paramiko.Transport((blip, port))
t.connect(username = bluser, password = blpasswd)
sftp = paramiko.SFTPClient.from_transport(t)
sftp.put(localpath, tmppath)
sftp.close()

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname = blip,username = bluser,password = blpasswd)

#new session
channel=ssh.invoke_shell()
channel.settimeout(10)

buff = ''
resp = ''
channel.send('scp '+ tmppath + ' ' + username + '@' + hostname + ':' + remotepath + '\n')

while not buff.endswith(passinfo):
    try:
        resp = channel.recv(9999)
    except Exception,e:
        print 'Error info:%s connection time.' % (str(e))
        channel.close()
        ssh.close()
        sys.exit()
    buff += resp
    if not buff.find('yes/no')==-1:
        channel.send('yes\n')
	buff=''

channel.send(password+'\n')

buff=''
while not buff.endswith('# '):
    resp = channel.recv(9999)
    if not resp.find(passinfo)==-1:
        print 'Error info: Authentication failed.'
        channel.close()
        ssh.close()
        sys.exit() 
    buff += resp

print buff
channel.close()
ssh.close()
