__author__ = 'harshit'
from django import forms
from models import City,Region

class CityAdminForm( forms.ModelForm ):
    class Meta:
        model = City

class RegionAdminForm( forms.ModelForm ):
    class Meta:
        model = Region