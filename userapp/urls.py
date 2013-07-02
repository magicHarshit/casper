__author__ = 'harshit'

from django.conf.urls.defaults import patterns , url
from django.contrib.auth.views import *
from userapp.views import EndUserLogin, EndUserRegistration ,ChangePassword, logout
from userapp.profile import ProfileSubmission
from userapp.forms import Password_Reset_Form


urlpatterns = patterns( '',

         url( r'^$', EndUserLogin.as_view(), name = 'login' ),

         url( r'^signup$', EndUserRegistration.as_view(), name = 'register' ),

         url( r'^profile_submission/$', ProfileSubmission.as_view(), name = 'profile_submission' ),

         url( r'^forgetpassword/$', 'django.contrib.auth.views.password_reset', {'password_reset_form':Password_Reset_Form}, name = 'forgetpassword' ),

         url( r'^password_reset_done/$', 'django.contrib.auth.views.password_reset_done'),

         url( r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', {'template_name' : 'registration/password_reset.html',  'post_reset_redirect': '/logout/' }),

         url( r'^changepassword/$', ChangePassword.as_view() , name = 'changepassword' ),

         url( r'^logout/$', logout , name = 'logout' ),

    #new url
         url( r'^(?P<user_id>[-\d]+)/profile/(?P<username>[-\w]+)',ProfileSubmission.as_view(), name = 'profile'),
)