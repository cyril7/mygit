# -*- coding: utf-8 -*-

from django.contrib import admin
from pastebin.models import Paste

class PasteAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'title', 'poster', 'syntax', 'timestamp')
    list_filter = ('timestamp', 'syntax')


admin.site.register(Paste, PasteAdmin)
