# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Update(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __unicode__(self):
        return "[%s] %s" % (
                
                # DJANGO的时区设置在数据库中都是0时区时间，settings.py里面的时区设置
                #       需要经过urls.py进来后才会生效，AJAX直接从数据库去就是0时区时间.
                # views.py 里面的updates_after 函数应该render_response返回html片段
                #        不应该返回JSON，这样AJAX直接渲染HTML即可，不需要JS再对时间戳处理
                
                self.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                self.text
        )

    class Meta:
        ordering = ['-id']


