#!/usr/bin/python
# -*- coding: utf-8 -*-

import paramiko

hostname = '192.168.18.100'
username = 'root'
password = 'abc123'
paramiko.util.log_to_file('syslogin.log')

ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.connect(hostname = hostname, username = username, password = password)
stdin,stdout,stderr = ssh.exec_command('free -m')
print stdout.read()
ssh.close()
