from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bookms.views.home', name='home'),
    # url(r'^bookms/', include('bookms.foo.urls')),

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

#urlpatterns += patterns('',
#    url(r'^bookapp/', include('bookapp.urls')),
#)

urlpatterns += patterns ('',
 (r'^bookapp/', include('bookapp.urls')),
)
