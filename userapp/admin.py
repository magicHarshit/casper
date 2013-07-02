__author__ = 'harshit'

from userapp.models import LoginDetail
from django.contrib import admin



class LoginDetailAdmin( admin.ModelAdmin ):

    model = LoginDetail
    list_display = ( 'user', 'last_login', 'ip_address' )
    list_filter = [  'user', 'last_login', 'ip_address']
    search_fields = ['user']


admin.site.register(LoginDetail,LoginDetailAdmin)

