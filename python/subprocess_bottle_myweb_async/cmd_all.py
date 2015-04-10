#!/usr/bin/env python
'''
Class that for istribute the method output_%s
>>> import cmd_all
>>> dir(cmd_all)
['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'cmd_conn_counts', 'cmd_nginx_restart', 'cmd_opened_port', 'cmd_server_restart', 'cmd_uptime']
>>> def cmd_from_form(value):
...     cmd_function = getattr(cmd_all, "cmd_%s" % value, cmd_all.cmd_uptime)
...     return cmd_function()
... 
>>> cmd = cmd_from_form(value="opened_port")
>>> cmd
'netstat -lnp'
'''
def cmd_uptime():
    return  "uptime" 

def cmd_opened_port():
    return "netstat -lnp"

def cmd_conn_counts():
    return "netstat -n | awk '/^tcp/ {++S[\$NF]} END {for(a in S) print a, S[a]}'"

def cmd_nginx_restart():
    return "/etc/init.d/nginx restart"

def cmd_server_restart():
    return "reboot"

def cmd_bat_bt_service_proxy():
    return "/root/dev/python/progress_Bar/sub/bat_bt_service_proxy.sh"

def cmd_bt_chinfo_service():
    return "/root/dev/python/progress_Bar/sub/bat_bt_chinfo_service.sh"

def cmd_bat_bt_wd_service():
    return "/root/dev/python/progress_Bar/sub/bat_bt_wd_service.sh"

def cmd_bat_bt_uinfo_service():
    return "/root/dev/python/progress_Bar/sub/bat_bt_uinfo_service.sh"

def cmd_bat_bt_chinfo_service():
    return "/root/dev/python/progress_Bar/sub/bat_bt_chinfo_service.sh"
