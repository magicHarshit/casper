__author__ = 'harshit'


from django import forms
from group_config.models import UserGroup

class GroupConfigurationForm(forms.ModelForm):
    name = forms.CharField(label=("Name"), max_length=30,
        error_messages = {'invalid': ("Name is Invalid"), },
        widget=forms.TextInput(attrs={'placeholder': 'Name'}))

    class Meta:
        model = UserGroup
        exclude = ('owner',)
