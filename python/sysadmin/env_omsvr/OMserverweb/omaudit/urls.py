# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('omaudit.views',
    (r'^$','index'),
    # omaudit_pull --> 实现客户端数据上报接口
    (r'omaudit_pull/$','omaudit_pull'),
    # omaudit_run --> 实现前端实时查询
    (r'omaudit_run/$','omaudit_run'),
)
