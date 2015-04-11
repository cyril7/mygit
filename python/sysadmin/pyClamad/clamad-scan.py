#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
yum install -y clamav clamd clamav-update
chkconfig --levels 235 clamd on # service clamd start
/usr/bin/freshclam  # update virus databases
setenforce 0
sed -i -e  '^TCPAddr/{ s/127.0.0.1/0.0.0.0/; }' /etc/clamd.conf
/etc/init.d/clamd start  # listen on 3310 

pip install pyClamd
"""
import time, pyclamd
from threading import Thread

class Scan(Thread):

    def __init__(self.IP, scan_type, file):
    """构造方法"""
        Thread.__init__(self)
        self.IP = IP
        self.scan_type = scan_type
        self.file = file
        self.connstr = ""
        self.scanresult = ""


    def __run__(self):
    """多进程run方法"""

    try:
        # 本机启动 clamd 服务,3310端口启动
        cd = pyclamd.ClamdNetworkSocket(self.IP, 3310)
        if cd.ping():
            self.connstr = self.IP + " connection [OK]"
            
            # 重载clamd 病毒特征库,建议更新病毒库后做reload()
            cd.reload()

            # 选择不同的扫描模式
            if self.scan_type == "contscan_file" :
                self.scanresult="{0}\n".format(cd.contscan_file(self.file))
            elif self.scan_type == "multiscan_file" :
                self.scanresult="{0}\n".format(cd.multiscan_file(self.file)) 
            elif self.scan_type=="scan_file":
                self.scanresult="{0}\n".format(cd.scan_file(self.file))
            time.sleep(1)

        else:
            self.connstr=self.IP+" ping error,exit"
            return
    except Exception, e:
        self.connstr = self.IP + " " + str(e)

# 设置扫描参数
IPs=['192.168.1.21','192.168.1.22']
scantype = "multiscan_file"
scanfile = "/data/www"
i = 1  
threadnum = 2 # 启动的线程数
scanlist = [] # 存储扫描Scan类线程对象列表

# 开始扫描
for ip in IPs:
    # 创建扫描Scan类对象,参数(IP, 扫描模式, 扫描路径)
    currp = Scan(ip, scantype, scanfile)
    # 追加对象到列表
    scanlist.append(currp)

    if i % threadnum == 0 or i == len(IPs):
        for task in scanlist:
            task.start()
  
        for task in scanlist:
            task.join()
            print task.connstr
            print task.scanresult
        scanlist = []   
    i += 1
