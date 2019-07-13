from django.contrib import admin
from .models import Author, Book, Publisher, Wife


# Register your models here.
# 声明管理器类
class AuthorManager(admin.ModelAdmin):
    # 定义在列表页面展示的字段
    list_display = ['id', 'name', 'age', 'email', 'isActive']
    # 定义在列表页中能链接到详情页的字段(list_display_links中的值必须出现在list_display中)
    list_display_links = ['id', 'name', 'email']
    # 定义在列表页就可编辑的字段(应为超链接不能编辑，所以list_editable中的值不能同时出现在list_display_links中)
    list_editable = ['age']
    # 在页面右侧自定义过滤器(这里以isAvtive为过滤条件)
    list_filter = ['isActive']
    # 在上方自定义搜索框(这里以name，email为搜索字段)
    search_fields = ['name', 'email']
    # 指定详情页面的显示的字段以及顺序(不能显示id)
    # fields = ['name', 'email', 'age', 'isActive']
    # 自定义分组(fieldsets和fields有冲突，两者这能有一个，不能同时出现)
    fieldsets = [
        ('基本选项', {
            'fields': ('name', 'age'),
            'classes': ('collapes')
        }),
        ('可选选项', {
            'fields': ('email', 'isActive'),
            'classes': ('collapes')
        })
    ]


class BookManager(admin.ModelAdmin):
    list_display = ['id', 'title', 'pub_date']
    date_hierarchy = 'pub_date'


class PublisherManager(admin.ModelAdmin):
    list_display = ['id', 'name', 'city', 'address', 'website']
    list_editable = ['address']
    list_filter = ['city']
    search_fields = ['name', 'address']
    fieldsets = [
        ('基本字段', {
            'fields': ('name', 'city'),
            'classes': ('collapes')
        }),
        ('高级字段', {
            'fields': ('address', 'website'),
            'classes': ('collapes')
        })]


# 注册Author模型类时 与 管理器AuthorManager关联
admin.site.register(Author, AuthorManager)
admin.site.register(Book, BookManager)
admin.site.register(Publisher, PublisherManager)
admin.site.register(Wife)
