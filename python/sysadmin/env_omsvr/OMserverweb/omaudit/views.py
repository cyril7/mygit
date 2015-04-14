# -*- coding: utf-8 -*-
#
#--------------------------------------------------------------------------
# views.py
#--------------------------------------------------------------------------
# auther:
# Email:
# update:
#
#---------------------------------------------------------------------------

import os,sys,time
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context
from django.template.loader import get_template
from omaudit.models import ServerHistory
from django.conf import settings
from django.template import RequestContext
from public.views import *
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.utils.log import logger


def index(request):
    res_template_dist={'system_name': settings.SYSTEM_NAME}
    return render_to_response('autoadmin/omaudit.html',res_template_dist)


"""
=事件任务前端加载方法
"""
"""
前端实时展示方法:
关于前端数据实时展示的实现原理,通过前端javascript的setInterval()方法实现定时函数调用,首次请求
默认返回ID倒序最新5条记录,并记录下LastID(最新记录ID),后面的定时调用将传递LastID参数,数据库查询
条件是"ID > LastID",从而达到实时获取最新记录的目的.同时也支持选择主机作为过滤条件.
"""
def omaudit_run(request):

    # 获取上次查询的最新记录ID
    if not 'LastID' in request.GET:
        LastID=""
    else:
        LastID=request.GET['LastID']
    
    # 获取选择的主机地址信息
    if not 'hosts' in request.GET:
        Hosts=""
    else:
        Hosts=request.GET['hosts']

    ServerHistory_string=""
    host_array=target_host(Hosts,"IP").split(';')

    """
    符合第一次提交条件,查询不加"id > lastID"条件,反之
    符合没有选择主机条件,查询不加 "history_ip in host_array" 条件,反之
    """
    if LastID=="0":
        if Hosts=="":
            ServerHistoryObj = ServerHistory.objects \
            .order_by('-id')[:5]
        else:
            ServerHistoryObj = ServerHistory.objects \
            .filter(history_ip__in=host_array).order_by('-id')[:5]
    else:
        if Hosts=="":
            ServerHistoryObj = ServerHistory.objects \
            .filter(id__gt=LastID).order_by('-id')
        else:
            ServerHistoryObj = ServerHistory.objects \
            .filter(id__gt=LastID,history_ip__in=host_array).order_by('-id')
    lastid=""
    i=0

    # 遍历查询结果,返回给前端
    for e in ServerHistoryObj:
        if i==0:
            lastid=e.id
        ServerHistory_string+="<font color=#cccccc>"+e.history_ip+ \
        "</font>&nbsp;&nbsp;\t"+ e.history_user+"&nbsp;&nbsp;\t"+str(e.db_datetime)+"\t # <font color=#ffffff>"+e.history_command+"</font>*"
        i+=1

    # 通过"@@"字符分隔事件记录与lastid,前端拆分
    ServerHistory_string+="@@"+str(lastid)
    return HttpResponse(ServerHistory_string)
    

"""
=事件任务pull方法
"""
def omaudit_pull(request):
    
    # 校验GET请求参数的合法性
    if request.method == 'GET':

        if not request.GET.get('history_id', ''):
            return HttpResponse("history_id null")

        if not request.GET.get('history_ip', ''):
            return HttpResponse("history_ip null")
        
        if not request.GET.get('history_user', ''):
            return HttpResponse("history_user null")

        if not request.GET.get('history_datetime', ''):
            return HttpResponse("history_datetime null")
            
        if not request.GET.get('history_command', ''):
            return HttpResponse("history_command null")
            
        # 获取各个字段的值
        history_id=request.GET['history_id']
        history_ip=request.GET['history_ip']
        history_user=request.GET['history_user']
        history_datetime=request.GET['history_datetime']
        history_command=request.GET['history_command']

        # 数据入库
        historyobj = ServerHistory(history_id=history_id, \
            history_ip=history_ip, \
            history_user=history_user, \
            history_datetime=history_datetime, \
            history_command=history_command)
        try:
            historyobj.save()
        except Exception,e:
            return HttpResponse("入库失败，请与管理员联系！"+str(e))
        
        # 输出OK 作为成功标志
        Response_result="OK"
        return HttpResponse(Response_result)
        
    else:
        return HttpResponse("非法提交！")
