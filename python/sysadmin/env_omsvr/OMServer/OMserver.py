# -*- coding: utf-8 -*-
import time
import os,sys
import re
from cPickle import dumps
from rpyc import Service
from rpyc.utils.server import ThreadedServer
import ConfigParser
import logging
from libraries import *
from config import *

# 定义服务器端模块存放路径
sysdir=os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.sep.join((sysdir,'modules/'+AUTO_PLATFORM)))

class ManagerService(Service):

    # 定义login 认证方法,对外开放调用的方法,rpyc要求加上"exposed_" 前缀,调用时使用login()即可
    def exposed_login(self,user,passwd):
        if user=="OMuser" and passwd=="KJS23o4ij09gHF734iuhsdfhkGYSihoiwhj38u4h":
            # 认证结果标记变量,True为认证通过,反之为认证失败
            self.Checkout_pass=True
        else:
            self.Checkout_pass=False
    


    def exposed_Runcommands(self,get_string):
        # 启用日志记录，设定格式,路径等
        logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s [%(levelname)s] %(message)s',
                    filename=sys.path[0]+'/logs/omsys.log',
                    filemode='a')
        
        # 判断是否通过验证
        try:
            if self.Checkout_pass!=True:
                return tencode("User verify failed!",SECRET_KEY)
        except:
                return tencode("Invalid Login!",SECRET_KEY)

        #获取rpyc client(即django omserverweb为rpcy client)的请求串get_string,通过tdecode方法解密后再进行分解,分隔符为"@@"
        self.get_string_array=tdecode(get_string,SECRET_KEY).split('@@')
        # 获取功能模块ID
        self.ModuleId=self.get_string_array[0]
        # 获取操作目标主机
        self.Hosts=self.get_string_array[1]
        
        # 获取功能模块的具体参数并追加到列表
        sys_param_array=[]
        for i in range(2,len(self.get_string_array)-1):
            sys_param_array.append(self.get_string_array[i])
        
        # 加载模块ID应对的模块名, 格式为"Mid_" + 模块id,如"Mid_1001.py"
        mid="Mid_"+self.ModuleId
        importstring = "from "+mid+" import Modulehandle"
        try:
            exec importstring
        except:
            return tencode(u"Module \""+mid+u"\" does not exist, Please add it",SECRET_KEY)
        
        # 调用模块相关方法,下发执行任务
        Runobj=Modulehandle(self.ModuleId,self.Hosts,sys_param_array)
        Runmessages=Runobj.run()

        # 根据不同主控端组件格式化输出, 支持func, ansible, saltstack
        if AUTO_PLATFORM=="func":
            if type(Runmessages) == dict:
                returnString = func_transform(Runmessages,self.Hosts)
            else:
                returnString = str(Runmessages).strip()
            
        elif AUTO_PLATFORM=="ansible":
            if type(Runmessages) == dict:
                returnString = ansible_transform(Runmessages,self.Hosts)
            else:
                returnString = str(Runmessages).strip()
                
        elif AUTO_PLATFORM=="saltstack":
            if type(Runmessages) == dict:
                returnString = saltstack_transform(Runmessages,self.Hosts)
            else:
                returnString = str(Runmessages).strip()

        # 对返回给rypc client (django omserverweb) 的数据串进行加密
        # 此处的 SECRET_KEY 为 django settings.py 里面的 SECRET_KEY
        return tencode(returnString,SECRET_KEY)


# 启动rpyc 服务监听,接听,响应请求        
s = ThreadedServer(ManagerService,port=11511,auto_register=False)
s.start()
