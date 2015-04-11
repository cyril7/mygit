#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
[root@www fabric]# fab -f fabfile.py host_type -H 127.0.0.1
"""

from fabric.api import run

def host_type():
    run('uname -s')
