# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
class ServerHistory(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    # 事件ID
    history_id = models.IntegerField()
    # 事件IP地址
    history_ip = models.CharField(max_length=45)
    # 事件用户名
    history_user = models.CharField(max_length=45)
    # 事件时间
    history_datetime = models.DateTimeField()
    # 入库时间
    db_datetime = models.DateTimeField()
    # 时间命令
    history_command = models.CharField(max_length=765)
    class Meta:
        db_table = u'server_history'
