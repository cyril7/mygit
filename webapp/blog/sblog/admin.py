# -*- coding: utf-8 -*-
from django.contrib import admin
from sblog.models import Author, Blog, Tag

class TagAdmin(admin.ModelAdmin):
    """docstring for AuthorAdmin"""
    list_display = ('tag_name', 'create_time')
    search_fields = ('tag_name',)

class AuthorAdmin(admin.ModelAdmin):
    """docstring for AuthorAdmin"""
    list_display = ('name', 'email', 'website')
    search_fields = ('name','email',)

class BlogAdmin(admin.ModelAdmin):
    """docstring for BlogAdmin"""
    list_display = ('caption', 'id', 'author','publish_time')
    search_fields = ('caption','author__name')
    list_filter = ('publish_time',)
    date_hierarchy = 'publish_time'
    ordering = ('-publish_time',)
    filter_horizontal = ('tags',)
    # raw_id_fields = ('author',)  # 它是一个包含外键字段名称的元组，它包含的字段将被展现成`` 文本框`` ，而不再是`` 下拉框`` 。   


admin.site.register(Tag,TagAdmin)
#admin.site.register(Tag)
admin.site.register(Author, AuthorAdmin)
#admin.site.register(Author)
admin.site.register(Blog, BlogAdmin)
#admin.site.register(Blog)
