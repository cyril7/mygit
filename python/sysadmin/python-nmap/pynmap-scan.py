#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
pip install python-nmap
"""

import sys
import nmap

scan_row=[]
input_data = raw_input('Please input hosts and port: ')
scan_row = input_data.split(" ")
if len(scan_row)!=2:
    print "Input errors,example \"192.168.1.0/24 80,443,22\""
    sys.exit(0)

hosts=scan_row[0]    #接收用户输入的主机
port=scan_row[1]    #接收用户输入的端口

try:
    nm = nmap.PortScanner()    #创建端口扫描对象
except nmap.PortScannerError:
    print('Nmap not found', sys.exc_info()[0])
    sys.exit(0)
except:
    print("Unexpected error:", sys.exc_info()[0])
    sys.exit(0)

try:
    nm.scan(hosts=hosts, arguments=' -v -sS -p '+port)    #调用扫描方法，参数指定扫描主机hosts，nmap扫描命令行参数arguments
except Exception,e:
    print "Scan erro:"+str(e)
    
for host in nm.all_hosts():    #遍历扫描主机
    print('----------------------------------------------------')
    print('Host : %s (%s)' % (host, nm[host].hostname()))    #输出主机及主机名
    print('State : %s' % nm[host].state())    #输出主机状态，如up、down

    for proto in nm[host].all_protocols():    #遍历扫描协议，如tcp、udp
        print('----------')
        print('Protocol : %s' % proto)    #输入协议名

        lport = nm[host][proto].keys()    #获取协议的所有扫描端口
        lport.sort()    #端口列表排序
        for port in lport:    #遍历端口及输出端口与状态
            print('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))




"""
读了一下nmap.py，发现scan方法调用了自身的analyse_nmap_xml_scan方法，于是修改analyse_nmap_xml_scan方法，直接把解析的dom对象返回，于是scan方法也返回了该对象，调用dom的toxml()方法，结果当中就根本没有“elapsed”这个词。

SLES11SP3环境，nmap版本是4.75。后来换了个CentOS7的环境，nmap-6.40，发现就一切正常了。看来后来的某个nmap版本开始，把elapsed这一项以属性的形式直接返回了。
"""
