__author__ = 'harshit'


from django import forms
from InstituteInfo.models import InstitueInfo, WallPost, ExtraDetails


class InstituteInfoForm(forms.ModelForm):
     class Meta:
         model = InstitueInfo
         exclude = ('user','display_map','profile','slug','display_flag')


class WallPostForm(forms.ModelForm):
#    wall_post = forms.TextInput(max_length= 100,)
    class Meta:
        model = WallPost
        fields = ('wall_post','group')


class InstituteSearchForm(forms.Form):
    search = forms.CharField(max_length= 250)

class ExtraDetailsForm(forms.ModelForm):
     class Meta:
         model = ExtraDetails
         fields = ('photo',)

#todo new
from models import CsvInfo
class CsvInfoForm(forms.ModelForm):
     class Meta:
         model = CsvInfo
         exclude = ('institute',)

     def clean_file_upload(self):
         file_obj = self.cleaned_data['file_upload']
         if file_obj.size > 51200:
             raise forms.ValidationError("You can upload a file of size 50 KB")
         return file_obj



