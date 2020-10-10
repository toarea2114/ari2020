'''
Created on 2020/09/21

@author: shung
'''
from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_name')

admin.site.register(User, UserAdmin)