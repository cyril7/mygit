from django.contrib import admin

from Asset.models import asset_system

class serversadm(admin.ModelAdmin):
    list_display =('ip_info','serv_info','cpu_info','disk_info','mem_info','load_info','mark_info')
    search_fields = ('ip_info','cpu_info')

admin.site.register(asset_system,serversadm)

