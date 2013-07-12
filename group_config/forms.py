__author__ = 'harshit'


from django import forms
from group_config.models import UserGroup




class GroupConfigurationForm(forms.ModelForm):
    class Meta:
        model = UserGroup
        exclude = ('owner',)
