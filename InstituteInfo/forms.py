__author__ = 'harshit'


from django import forms
from InstituteInfo.models import  Bulletin
from models import CsvInfo


class BulletinForm(forms.ModelForm):
    class Meta:
        model = Bulletin
        fields = ('title','body','attachments','group')


class CsvInfoForm(forms.ModelForm):
     class Meta:
         model = CsvInfo
         exclude = ('institute',)

     def clean_file_upload(self):
         file_obj = self.cleaned_data['file_upload']
         if file_obj.size > 51200:
             raise forms.ValidationError("You can upload a file of size 50 KB")
         return file_obj



