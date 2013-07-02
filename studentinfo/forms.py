__author__ = 'harshit'


from django import forms
from models import StudentInfo

class StudentInfoForm(forms.ModelForm):

    class Meta:
        model = StudentInfo
        exclude = ('user','status','profile',)