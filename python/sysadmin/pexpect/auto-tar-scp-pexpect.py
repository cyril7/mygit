#!/usr/bin/python
# -*- coding: utf-8 -*-

import pexpect
import sys

# 目标主机
ip="192.168.18.10"
user="root"
passwd="abc"
target_file="/tmp/diff.html"

child = pexpect.spawn('/usr/bin/ssh', [user + '@' + ip])
fout = file('mylog.txt', 'w')
child.logfile = fout

try:
    child.expect('(?i)password')
    child.sendline(passwd)
    child.expect('#')
    child.sendline('tar -czf /tmp/pssh.tar.gz ' + target_file)
    child.expect('#')
    print child.before
    child.sendline('exit')
    fout.close()
except EOF:
    print "expect EOF"
except TIMEOUT:
    print "expect TIMEOUT"

child = pexpect.spawn('/usr/bin/scp', [user + '@' + ip + ':/tmp/pssh.tar.gz', '/tmp'])
fout = file('mylog.txt','a')
child.logfile = fout
try:
    child.expect('(?i)password')
    child.sendline(passwd)
    child.expect(pexpect.EOF)
except EOF:
    print "expect EOF"
except TIMEOUT:
    print "expect TIMEOUT"
