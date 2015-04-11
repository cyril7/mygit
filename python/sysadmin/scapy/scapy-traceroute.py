#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
通过scapy的traceroute()方法实现探测机到目标服务器的路由轨迹，整个过程的原理见图3-14，首先通过探测机以SYN方式进行TCP服务扫描，同时启动tcpdump进行抓包，捕获扫描过程经过的所有路由点，再通过graph()方法进行路由IP轨迹绘制，中间调用ASN映射查询IP地理信息并生成svg流程文档，最后使用ImageMagick工具将svg格式转换成png，流程结束
"""


"""
# yum install -y  graphviz ImageMagick 
# pip install scapy
"""

import os, sys, time, subprocess
import warnings, logging

# 屏蔽scapy无用告警信息
warnings.filterwarnings("ignore", category = DeprecationWarning)

# 屏蔽模块IPV6的多余告警
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

from scapy.all import traceroute
domains = raw_input('Please input one or more IP/domain: ')

# 用空格分隔输入的域名
target = domains.split(' ')
dport = [80]

if len(target) >= 1 and target[0] != '':
    """
    traceroute(target, dport=80, minttl=1, maxttl=30, sport=<RandShort>, l4=None, filter=None, timeout=2, verbose=None, **kargs) 
    该方法实现TCP跟踪路由功能，关键参数说明如下：
    
    target：跟踪的目标对象，可以是域名或IP，类型为列表，支持同时指定多个目标，如["www.qq.com","www.baidu.com","www.google.com.hk"]；
    
    dport：目标端口，类型为列表，支持同时指定多个端口，如[80,443]；
    
    minttl：指定路由跟踪的最小跳数（节点数）；
    
    maxttl：指定路由跟踪的最大跳数（节点数）。
    """
    #启动路由跟踪
    res, unans = traceroute(target, dport = dport, retry = -2)
    #生成svg矢量图形
    res.graph(target = "> trace.svg")
    time.sleep(1)
    subprocess.Popen("/usr/bin/convert trace.svg trace.png", shell=True)

else:
    print "IP/domain number of errors,exit"
