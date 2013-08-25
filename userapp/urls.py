__author__ = 'harshit'

from django.conf.urls.defaults import patterns , url
from django.contrib.auth.views import *
from userapp.views import *
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

         url( r'^(?P<username>[-\w]+)/mygroups/$',get_group_listing, name = 'group_listing'),

         url( r'^(?P<username>[-\w]+)/$', UserProfile.as_view(), name = 'institute_profile' ),

         url( r'^(?P<username>[-\w]+)/connect/$', connect_user, name = 'connect' ),

         url( r'^(?P<username>[-\w]+)/pending_requests/$', PendingStudentListView.as_view(), name = 'pending_request' ),

         # url( r'^(?P<username>[-\w]+)/pending_requests/$', PendingStudentListView.as_view(), name = 'pending_request' ),

         url( r'^(?P<username>[-\w]+)/bulletins_by_faculty/$', fetch_faculty_bulletins, name = 'bulletins_by_faculty' ),

         url( r'^(?P<username>[-\w]+)/students/$', students_connected_to_user , name = 'connected_students' ),

         url( r'^(?P<username>[-\w]+)/faculty/$', faculty_connected_to_user, name = 'connected_faculty' ),

         url( r'^find/user/$', UserListView.as_view(), name = 'search_user' ),

         url( r'^delete/(?P<pk>[-\d]+)/$', MyDeleteView.as_view(), name = 'delete_post' ),
)