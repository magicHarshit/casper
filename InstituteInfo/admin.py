from models import InstitueInfo, InstituteLocation, InstituteUser
from django.contrib import admin


class InstituteLocationInline(admin.StackedInline):
    model = InstituteLocation
    extra = 1

class InstituteUserInline( admin.StackedInline ):
    model = InstituteUser
    extra = 1


class InstituteInfoAdmin( admin.ModelAdmin ):

    model = InstitueInfo
    inlines = [InstituteLocationInline,InstituteUserInline]

admin.site.register( InstitueInfo , InstituteInfoAdmin )
admin.site.register(InstituteLocation)
