#!/usr/bin/env python
#coding:utf-8
import sys
import socket
import fcntl
import struct
import logging
from config import *
import urllib,httplib

# 设置全局Socket超时时间(覆盖HTTP连接超时)
socket.setdefaulttimeout(Connect_TimeOut)

# 启用日志记录
logging.basicConfig(level=logging.DEBUG,
            format='%(asctime)s [%(levelname)s] %(message)s',
            filename=sys.path[0]+'/omsys.log',
            filemode='a')

# 对$(history 1)进行合法校验,少于6个参数则报错
# 正确的格式为"173 root 2014-11-13 22:13:39 ls"
if len(sys.argv)<6:
    logging.error('History not configured in /etc/profile!')
    sys.exit()

# 获取本地IP地址函数,用来确认数据来源
def get_local_ip(ethname):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        addr = fcntl.ioctl(sock.fileno(), 0x8915, struct.pack('256s', ethname))
        return socket.inet_ntoa( addr[20:24] )
    except Exception,e:
        logging.error('get localhost IP address error:'+str(e))
        return "127.0.0.1"

# 数据上报函数
def pull_history(http_get_param=""):
    try:
        # 与SERVER 端建立http连接,指定超时时间
        http_client =httplib.HTTPConnection(OMServer_address, 80, timeout=Connect_TimeOut)
        # 发起GET请求
        http_client.request("GET", http_get_param)
        # 获取HTTP返回对象
        response =http_client.getresponse()

        # 将HTTP 200状态则退出
        if response.status != 200:       
            logging.error('response http status error:'+str(response.status))
            sys.exit()
        # 返回字段非OK则退出
        http_content=response.read().strip()
        if http_content != "OK":       
            logging.error('response http content error:'+str(http_content))
            sys.exit()

    except Exception, e:
        logging.error('connection django-cgi server error:'+str(e))
        sys.exit()
    finally:
        if http_client:
            http_client.close()
        else:
            logging.error('connection django-cgi server unknown error.')
            sys.exit()

# 调用获取本地IP函数
Sysip = get_local_ip(Net_driver)
# 获取history信息中的系统用户
SysUser = sys.argv[2]
# 获取history ID 信息
History_Id = sys.argv[1]
# 获取history 日期 信息
History_date = sys.argv[3]
# 获取history 时间 信息
History_time = sys.argv[4]
History_command = ""

# 获取history的系统命令信息
for i in range(5, len(sys.argv)):
    History_command+= sys.argv[i]+" "

# 合并所有信息的HTTP GET 参数格式,部分信息使用urilib.quote进行URL编码
s= "/omaudit/omaudit_pull/?history_id="+History_Id+"&history_ip="+Sysip+"&history_user="+SysUser+"&history_datetime="+History_date+urllib.quote(" ")+History_time+"&history_command="+urllib.quote(History_command.strip())

# 调用数据上报函数
pull_history(s)
