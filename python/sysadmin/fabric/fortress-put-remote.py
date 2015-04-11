#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fabric.api import *
from fabric.context_managers import *
from fabric.contrib.console import confirm

env.user='root'
env.gateway='192.168.18.100'
env.hosts=['192.168.18.152']
#env.hosts=['192.168.1.21','192.168.1.22']
env.passwords = {
    'root@192.168.18.100:22': 'abc123',
    'root@192.168.18.152:22': 'abc123',
#    'root@192.168.1.21:22': 'SKJh935yft#',
#    'root@192.168.1.22:22': 'SKJh935yft#',
#    'root@192.168.1.23:22': 'KJSD9325hgs'
}
# 本地上传的文件路径
lpackpath="/tmp/pssh.tar.gz"
# 远端接收文件的路径
rpackpath="/tmp/data"

@task
def put_task():
    run("mkdir -p /tmp/data")
    with settings(warn_only=True):
        result = put(lpackpath, rpackpath)
    if result.failed and not confirm("put file failed, Continue[Y/N]?"):
        abort("Aborting file put task!")

@task
def run_task():
    with cd("/tmp/install"):
        run("tar -zxvf lnmp0.9.tar.gz")
        with cd("lnmp0.9/"):
            run("./centos.sh")

@task
def go():
    put_task()
    #run_task()
