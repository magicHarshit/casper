from django import forms
from master.models import ImageInfo



class ImagesInfoForm(forms.ModelForm):
     class Meta:
         model = ImageInfo
         fields = ('photo',)