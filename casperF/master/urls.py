from django.conf.urls.defaults import patterns, url
from django.contrib.auth.views import *
from .views import EndUserRegistration, EndUserLogin, logout, ChangePassword
from .forms import Password_Reset_Form
from .profile import ProfileSubmission
from .home import UserDetail, connected_faculties, connected_students
urlpatterns = patterns('',

        url(r'^$', EndUserLogin.as_view(), name='login'),

        url(r'^(?P<username>[-\w]+)/profile/$', ProfileSubmission.as_view(), name='profile'),

        url(r'^signup$', EndUserRegistration.as_view(), name='register'),

        url(r'^forgetpassword/$', 'django.contrib.auth.views.password_reset', {'password_reset_form':Password_Reset_Form}, name = 'forgetpassword' ),

        url(r'^password_reset_done/$', 'django.contrib.auth.views.password_reset_done'),

        url(r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', {'template_name' : 'registration/password_reset.html',  'post_reset_redirect': '/logout/' }),

        url(r'^changepassword/$', ChangePassword.as_view(), name='changepassword'),

        url(r'^logout/$', logout, name='logout'),

        url(r'^(?P<username>[-\w]+)/$', UserDetail.as_view(), name='home'),

        url(r'^(?P<username>[-\w]+)/mystudents/$', connected_students, name='connected_students'),

        url(r'^(?P<username>[-\w]+)/myfaculties/$', connected_faculties, name='connected_faculties'),

        )
