__author__ = 'harshit'


from django import forms
from models import FacultyInfo

class FacultyInfoForm(forms.ModelForm):

    class Meta:
        model = FacultyInfo
        exclude = ('user','rating','profile','status','connections',)