# -*- coding: utf-8 -*-
#
#--------------------------------------------------------------------------
# views.py
#--------------------------------------------------------------------------
#
#---------------------------------------------------------------------------

import os,sys,time
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context
from django.template.loader import get_template
from autoadmin.models import ServerFunCateg
from autoadmin.models import ServerAppCateg
from autoadmin.models import ServerList
from autoadmin.models import ModuleList
from django.conf import settings
from django.template import RequestContext
from public.views import *
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.utils.log import logger

"""
=OMserver main page
"""
def index(request):
    # 给字典赋值,以便渲染模板
    res_template_dist={'system_name': settings.SYSTEM_NAME}
    return render_to_response('autoadmin/main.html',res_template_dist)
    
"""
=Add module page
"""
"""
module 是用来添加操作服务器的命令行,直接和ansible等交互
"""
def module_add(request):
    # 给字典赋值,以便渲染模板
    res_template_dist={'system_name': settings.SYSTEM_NAME}
    return render_to_response('autoadmin/module_add.html',res_template_dist)


"""
=Return server function categ
"""
"""
CMDB 体系中一种比较典型的资产定义方法,即采用"功能分类"作为根类,其子类为"应用分类",在最小单位的"服务器"中指定"应用分类"进行关联,完成层级定义.
功能分类  --> 应用分类 <-- 服务器列表
Linux.web(一级功能类别), bbs.domain.com(二级应用类别),10.11.100.10服务器归到bbs.domain.com类别
"""
def server_fun_categ(request):
    categ_id="-1"
    categ_name=u"<-请选择功能类别->"
    
    ServerFunObj = ServerFunCateg.objects.order_by('id')
    for e in ServerFunObj:
        categ_id+=","+str(e.id)
        categ_name+=","+e.server_categ_name
    fun_categ_string=categ_name+"|"+categ_id
    return HttpResponse(fun_categ_string)


"""
=Return server app categ
"""
"""
根据应用表的id 返回应用列表
"""
def server_app_categ(request):
    categ_id="-1"
    categ_name=u"<-请选择应用类别->"

    if not 'fun_categId' in request.GET:
        fun_categId=""
    else:
        fun_categId=request.GET['fun_categId']
            
    ServerAppObj = ServerAppCateg.objects.filter(server_categ_id=fun_categId)
    for e in ServerAppObj:
        categ_id+=","+str(e.id)
        categ_name+=","+e.app_categ_name
    app_categ_string=categ_name+"|"+categ_id
    return HttpResponse(app_categ_string)


"""
=Return server IP list
"""
"""
根据ID in server_app_categ (即 server_app_id in server_list)查找server IP
"""
def server_list(request):
    ip=""
    ip_hostname=""

    if not 'app_categId' in request.GET:
        app_categId=""
    else:
        app_categId=request.GET['app_categId']
            
    ServerListObj = ServerList.objects.filter(server_app_id=app_categId)
    for e in ServerListObj:
        ip+=","+e.server_lip
        ip_hostname+=","+e.server_lip+"*"+e.server_name
    server_list_string=ip[1:]+"|"+ip_hostname[1:]
    return HttpResponse(server_list_string)


"""
=Return module list
"""
"""
根据 module 表 id 查找 module 名称列表
"""
def module_list(request):
    module_id="-1"
    module_name=u"请选择功能模块..."
    
    ModuleObj = ModuleList.objects.order_by('id')
    for e in ModuleObj:
        module_id+=","+str(e.id)
        module_name+=","+e.module_name
    module_list_string=module_name+"|"+module_id
    return HttpResponse(module_list_string)


"""
=Return module info
"""
# 返回具体的module
def module_info(request):

    if not 'Module_Id' in request.GET:
        Module_Id=""
    else:
        Module_Id=request.GET['Module_Id']
        
    ModuleObj = ModuleList.objects.get(id=Module_Id)
    module_info_string=str(ModuleObj.id)+"@@"+ModuleObj.module_name+"@@"+ModuleObj.module_caption+"@@"+ModuleObj.module_extend

    return HttpResponse(module_info_string)


"""
=Run module
"""
def module_run(request):
    import rpyc
    from cPickle import loads
    put_string=""
    
    #  从表单中接收模块id, 操作主机, 模块扩展参数等
    if not 'ModuleID' in request.GET:
        Module_Id=""
    else:
        Module_Id=request.GET['ModuleID']
        put_string+=Module_Id+"@@"

    if not 'hosts' in request.GET:
        Hosts=""
    else:
        Hosts=request.GET['hosts']
        put_string+=Hosts+"@@"

    if not 'sys_param_1' in request.GET:
        Sys_param_1=""
    else:
        Sys_param_1=request.GET['sys_param_1']
        put_string+=Sys_param_1+"@@"

    if not 'sys_param_2' in request.GET:
        Sys_param_2=""
    else:
        Sys_param_2=request.GET['sys_param_2']
        put_string+=Sys_param_2+"@@"
    
    # rypc 执行命令
    try:
        conn=rpyc.connect('192.168.18.131',11511)
        #conn=rpyc.connect('192.168.1.20',11511)

        # 调用 rpyc server 的login方法实现账号, 密码校验,屏蔽恶意链接等等
        conn.root.login('OMuser','KJS23o4ij09gHF734iuhsdfhkGYSihoiwhj38u4h')
    except Exception,e:
        logger.error('connect rpyc server error:'+str(e))
        return HttpResponse('connect rpyc server error:'+str(e))
    
    # 该处使用了base64.b64encode(), base64.b64decode()加上密钥混淆算法(RC4),来实现数据的加密和解密
    # 解密加密算法函数详见libraries.py
    # 数据在omseverweb to rpyc server  传输之前使用tencode加密,密钥为SECRET_KEY
    put_string=tencode(put_string,settings.SECRET_KEY)
    # 数据在rpyc server to omserverweb 返回之后使用tdencode解密,密钥为SECRET_KEY
    OPresult=tdecode(conn.root.Runcommands(put_string),settings.SECRET_KEY)
    return HttpResponse(OPresult)

"""
= module 的添加方法检查
"""
def module_add_post(request):
    if request.method == 'GET':

        #检查表单-应用名称 
        if not request.GET.get('module_name', ''):
            return HttpResponse("模块名称不能为空！")

        #检查表单-监控URL
        if not request.GET.get('module_caption', ''):
            return HttpResponse("模块功能描述不能为空！")
        

        module_name=request.GET['module_name']
        module_caption=request.GET['module_caption']
        module_extend=request.GET['module_extend']

        moduleobj = ModuleList(module_name=module_name, \
            module_caption=module_caption, \
            module_extend=module_extend)
        try:
            moduleobj.save()
            #lastId = moduleobj.objects.order_by('-pk')[0]
            lastId = ModuleList.objects.latest('id')
        except Exception,e:
            return HttpResponse("入库失败，请与管理员联系！"+str(e))
        
        InfoList="祝贺你，模块前端添加成功，模块ID为："+str(lastId.pk)+"，下一步请在服务器端编写模块逻辑！"
        return HttpResponse(InfoList)
        
    else:
        return HttpResponse("非法提交！")
