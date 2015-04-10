#!/usr/bin/python
# -*- coding: utf-8 -*-

import os,sys
import time
import sys
import pycurl

URL="http://www.baidu.com"
c = pycurl.Curl()
c.setopt(pycurl.URL, URL)
                
#连接超时时间,5秒
c.setopt(pycurl.CONNECTTIMEOUT, 5)

#下载超时时间,5秒
c.setopt(pycurl.TIMEOUT, 5)

# 完成交互后强制断开连接,不重用
c.setopt(pycurl.FORBID_REUSE, 1)

# 指定HTTP重定向的最大数为1
c.setopt(pycurl.MAXREDIRS, 1)

# 屏蔽下载进度条
c.setopt(pycurl.NOPROGRESS, 1)

# 设置保存DNS信息的时间为30秒
c.setopt(pycurl.DNS_CACHE_TIMEOUT,30)

# 用来储存返回的HTTP头部以及页面内容
indexfile = open(os.path.dirname(os.path.realpath(__file__))+"/content.txt", "wb")

# 将返回的HEADER重定向到infexfile文件对象
c.setopt(pycurl.WRITEHEADER, indexfile)

# 将返回的HTML内容重定向到infexfile文件对象
c.setopt(pycurl.WRITEDATA, indexfile)
try:
    c.perform()
except Exception,e:
    print "connecion error:"+str(e)
    indexfile.close()
    c.close()
    sys.exit()

# 获取DNS解析时间
NAMELOOKUP_TIME =  c.getinfo(c.NAMELOOKUP_TIME)

# 获取建立连接时间
CONNECT_TIME =  c.getinfo(c.CONNECT_TIME)

# 获取从建立连接到准备传输所消耗的时间
PRETRANSFER_TIME =   c.getinfo(c.PRETRANSFER_TIME)

# 获取从建立连接到传输开始消耗的时间
STARTTRANSFER_TIME = c.getinfo(c.STARTTRANSFER_TIME)

# 获取传输的总时间
TOTAL_TIME = c.getinfo(c.TOTAL_TIME)

# HTTP状态码
HTTP_CODE =  c.getinfo(c.HTTP_CODE)

# 下载数据包大小
SIZE_DOWNLOAD =  c.getinfo(c.SIZE_DOWNLOAD)

# HTTP头部大小
HEADER_SIZE = c.getinfo(c.HEADER_SIZE)

# 平均下载速度
SPEED_DOWNLOAD=c.getinfo(c.SPEED_DOWNLOAD)

print "HTTP状态码：%s" %(HTTP_CODE)
print "DNS解析时间：%.2f ms"%(NAMELOOKUP_TIME*1000)
print "建立连接时间：%.2f ms" %(CONNECT_TIME*1000)
print "准备传输时间：%.2f ms" %(PRETRANSFER_TIME*1000)
print "传输开始时间：%.2f ms" %(STARTTRANSFER_TIME*1000)
print "传输结束总时间：%.2f ms" %(TOTAL_TIME*1000)

print "下载数据包大小：%d bytes/s" %(SIZE_DOWNLOAD)
print "HTTP头部大小：%d byte" %(HEADER_SIZE)
print "平均下载速度：%d bytes/s" %(SPEED_DOWNLOAD)

indexfile.close()
c.close()
