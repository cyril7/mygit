#!/usr/bin/python
# -*- coding: utf-8 -*
#  by criver
from fabric.api import *
from fabric.colors import *
from fabric.contrib.files import exists 
env.user = 'apps'
env.password = ''
#env.hosts = [ 'grid00', 'grid01', 'grid02', 'grid03', 'grid04', 'grid05']

# plugin_dir => /usr/lib or /usr/lib64
'''
def assign_plugin_dir():
    global plugin_dir 
    with lcd('/home/aaa/nagios_manipulate'):
        if exists('/usr/lib64/nagios/plugins/'):
            plugin_dir = 'lib64'
        else:
            plugin_dir = 'lib'
        print green('plugin_dir is ' + plugin_dir)
'''
#@task
def check_apps_exits():
    grep_apps = 'flume'
    run('pgrep -fl ' + grep_apps)

#@task
def deploy_apps_flume():
    # global plugin_dir
    put_apps = 'apps_flume.tar.gz'
    with lcd('/home/aaa/deploy/'):
        put(put_apps, '/home/apps/')
        sudo('/bin/tar zxfp /home/apps/' + put_apps + ' -C /')
        sudo('chown -R apps:apps /apps')
        run('cd /apps/svr/flume/external-lib/ && python flume_init.py start')
        run('pgrep -fl flume')
        print green('deploy to remote ' + put_apps  + ' success!')

def deploy():
    #execute(assign_plugin_dir)
    execute(check_apps_exits)
    #execute(deploy_apps_flume)
