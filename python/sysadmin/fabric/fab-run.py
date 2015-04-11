#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
[root@www fabric]# fab -f fab-run.py local_task
[root@www fabric]# fab -f fab-run.py remote_task
"""
from fabric.api import *

env.user='root'
env.hosts=['192.168.18.100','192.168.18.152']
env.password='abc123'

@runs_once
def local_task():
    local("uname -a")

def remote_task():
    with cd("/tmp"):
        run("ls -l")
