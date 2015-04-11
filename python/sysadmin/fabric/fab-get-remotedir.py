#!/usr/bin/env python
from fabric.api import * 

env.user='root'
env.hosts=['192.168.18.100','192.168.18.152']
env.password='abc123'

@runs_once
def input_raw():
    return prompt("please input directory name:",default="/home")

def worktask(dirname):
    run("ls -l " + dirname)

@task
def go():
    getdirname = input_raw()
    worktask(getdirname)
