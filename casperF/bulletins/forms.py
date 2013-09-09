from django import forms
from django.forms.models import modelform_factory

from .models import Bulletin, Comment

class BulletinForm(forms.ModelForm):
    class Meta:
        model = Bulletin
        fields = ('title', 'body', 'attachments', 'group')

commentform = modelform_factory(Comment,fields=('reply',))

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('reply',)