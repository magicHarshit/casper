__author__ = 'harshit'



from models import StudentInfo
from django.contrib import admin



class StudentInfoAdmin( admin.ModelAdmin ):
    model = StudentInfo

admin.site.register( StudentInfo , StudentInfoAdmin )
