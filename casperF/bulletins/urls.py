from django.conf.urls.defaults import patterns, url
from django.contrib.auth.views import *

from .views import submit_bulletin, submit_comment, delete_bulletin, delete_comment, show_bulletin

urlpatterns = patterns('',
        url(r'^(?P<username>[-\w]+)/bulletin/(?P<bulletin_id>d+)$', show_bulletin, name='show_bulletin'),

        url(r'^(?P<username>[-\w]+)/bulletin/delete/(?P<bulletin_id>d+)$', delete_bulletin, name='delete_bulletin'),

        url(r'^(?P<username>[-\w]+)/bulletin/$', submit_bulletin, name='submit_bulletin'),

        url(r'^(?P<username>[-\w]+)/comment/$', submit_comment, name='submit_comment'),

        url(r'^(?P<username>[-\w]+)/comment/(?P<comment_id>d+)$', delete_comment, name='delete_comment'),

        )
