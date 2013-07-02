__author__ = 'harshit'



from models import FacultyInfo
from django.contrib import admin



class FacultyInfoAdmin( admin.ModelAdmin ):
    model = FacultyInfo

admin.site.register( FacultyInfo , FacultyInfoAdmin )
