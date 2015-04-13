from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'simpleToDo.views.home', name='home'),
    # url(r'^simpleToDo/', include('simpleToDo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

from django.contrib import admin
admin.autodiscover()
urlpatterns += patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

from django.conf.urls import *

urlpatterns += patterns(('simpleToDo.views'),
    url(r'^$', 'todolist', name='todo'),
    url(r'^addtodo/$', 'addTodo', name='add'),
    url(r'^todofinish/(?P<id>\d+)/$', 'todofinish', name='finish'),
    url(r'^todobackout/(?P<id>\d+)/$', 'todoback',  name='backout'),
    url(r'^updatetodo/(?P<id>\d+)/$', 'updatetodo', name='update'),
    url(r'^tododelete/(?P<id>\d+)/$', 'tododelete', name='delete'),
)

''' 
from django.conf.urls import *

urlpatterns += patterns(('simpleToDo.views'),
    url(r'^$', 'todolist', name='todo'),
    url(r'^addtodo/$', 'addTodo', name='add'),
    url(r'^todofinish/(?P<id>\d+)/$', 'todofinish', name='finish'),
    url(r'^todobackout/(?P<id>\d+)/$', 'todoback',  name='backout'),
    url(r'^updatetodo/(?P<id>\d+)/$', 'updatetodo', name='update'),
    url(r'^tododelete/(?P<id>\d+)/$', 'tododelete', name='delete'),
)
'''
