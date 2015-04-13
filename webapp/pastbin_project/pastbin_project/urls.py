from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pastbin_project.views.home', name='home'),
    # url(r'^pastbin_project/', include('pastbin_project.foo.urls')),

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

from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import create_object
from pastebin.models import Paste

display_info = {'queryset': Paste.objects.all()}
create_info = {'model':Paste}

urlpatterns += patterns('',
    url(r'^$', object_list, dict(display_info, allow_empty=True)),
    url(r'^paste/(?P<object_id>\d+)/$', object_detail, display_info),
    url(r'^paste/add/$', create_object, create_info),
)
