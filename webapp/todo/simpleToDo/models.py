# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
#from django_openid_auth.models import User
#之前我用过openid 这里换成 from django.contrib.auth.models import User 就可以了
from django.contrib.auth.models import User

class Todo(models.Model):
    user = models.ForeignKey(User)
    todo = models.CharField(max_length=50)
    # flag 标记是否完成 默认为1表示未完成
    flag = models.CharField(max_length=2, default='1')
    priority = models.CharField(max_length=2, default='0')
    pubtime = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%d %s %s' % (self.id, self.todo, self.flag)

    class Meta:
        ordering = ['priority', 'pubtime']
