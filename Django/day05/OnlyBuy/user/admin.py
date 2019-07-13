from django.contrib import admin
from .models import *


# Register your models here.
class UserManager(admin.ModelAdmin):
    list_display = ['id', 'uname', 'upwd', 'uphone', 'uemail', 'isActive']
    list_filter = ['isActive']


admin.site.register(User, UserManager)
