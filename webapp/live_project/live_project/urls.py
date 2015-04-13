from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'live_project.views.home', name='home'),
    # url(r'^live_project/', include('live_project.foo.urls')),

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
from liveupdate.models import Update
urlpatterns += patterns('django.views.generic',
    url(r'^$', 'list_detail.object_list',{
        'queryset':Update.objects.all()
    }),
)

urlpatterns += patterns('liveupdate.views',
    url(r'^updates-after/(?P<id>\d+)/$','updates_after'),
)
