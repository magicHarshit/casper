__author__ = 'harshit'


from django import forms
from group_config.models import Group, StaticGroup


class GroupConfigurationForm(forms.ModelForm):
    class Meta:
        model = Group


class StaticGroupConfigurationForm(forms.ModelForm):
    class Meta:
        model = StaticGroup
        exclude = ('institute',)
