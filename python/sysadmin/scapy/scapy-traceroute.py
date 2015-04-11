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


"""
"-"表示路由节点无回应或超时；"11"表示扫描的指定服务无回应；"SA"表示扫描的指定服务有回应，一般是最后一个主机IP。
root@www scapy]# python scapy-traceroute.py
Please input one or more IP/domain: google.com.hk linux.org
Begin emission:
*.*****************************Finished to send 60 packets.
**********.Begin emission:
*Finished to send 20 packets.
.Begin emission:
Finished to send 19 packets.
Begin emission:
*Finished to send 19 packets.
Begin emission:
*Finished to send 18 packets.
.Begin emission:
Finished to send 17 packets.
Begin emission:
*Finished to send 17 packets.
Begin emission:
*Finished to send 16 packets.
.Begin emission:
*Finished to send 15 packets.
Begin emission:
*Finished to send 14 packets.
Begin emission:
*Finished to send 13 packets.
.Begin emission:
*Finished to send 12 packets.
.Begin emission:
Finished to send 11 packets.
Begin emission:
*Finished to send 11 packets.
Begin emission:
*Finished to send 10 packets.
.Begin emission:
Finished to send 9 packets.
Begin emission:
*Finished to send 9 packets.
Begin emission:
*Finished to send 8 packets.
.Begin emission:
Finished to send 7 packets.
Begin emission:
*Finished to send 7 packets.
Begin emission:
*Finished to send 6 packets.
.Begin emission:
Finished to send 5 packets.
Begin emission:
*Finished to send 5 packets.
Begin emission:
*Finished to send 4 packets.
.Begin emission:
Finished to send 3 packets.
Begin emission:
*Finished to send 3 packets.
Begin emission:
*Finished to send 2 packets.
.Begin emission:
Finished to send 1 packets.
Begin emission:
Finished to send 1 packets.
*
Received 72 packets, got 60 answers, remaining 0 packets
   107.170.40.56:tcp80 216.58.221.35:tcp80 
1  192.168.18.1    11  192.168.18.202  11  
2  58.62.224.1     11  58.62.224.1     11  
3  59.42.127.73    11  59.42.127.73    11  
4  183.56.33.121   11  183.56.33.121   11  
5  61.144.3.30     11  183.56.30.1     11  
6  202.97.33.214   11  202.97.34.182   11  
7  192.168.18.202  5   192.168.18.202  5   
8  202.97.58.254   11  202.97.61.26    11  
9  202.97.50.22    11  202.97.122.70   11  
10 213.248.102.225 11  209.85.241.58   11  
11 213.248.80.17   11  72.14.235.79    11  
12 213.155.135.116 11  192.168.18.202  5   
13 213.155.130.251 11  192.168.18.202  5   
14 216.6.90.6      11  192.168.18.202  5   
15 63.243.128.122  11  192.168.18.202  5   
16 107.170.40.56   SA  192.168.18.202  5   
17 192.241.164.238 11  192.168.18.202  5   
18 107.170.40.56   SA  192.168.18.202  5   
19 107.170.40.56   SA  192.168.18.202  5   
20 107.170.40.56   SA  192.168.18.202  5   
21 107.170.40.56   SA  192.168.18.202  5   
22 107.170.40.56   SA  192.168.18.202  5   
23 107.170.40.56   SA  192.168.18.202  5   
24 107.170.40.56   SA  192.168.18.202  5   
25 107.170.40.56   SA  192.168.18.202  5   
26 107.170.40.56   SA  192.168.18.202  5   
27 107.170.40.56   SA  192.168.18.202  5   
28 107.170.40.56   SA  192.168.18.202  5   
29 107.170.40.56   SA  192.168.18.202  5   
30 107.170.40.56   SA  192.168.18.202  5

"""
