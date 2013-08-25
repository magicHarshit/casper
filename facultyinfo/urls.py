__author__ = 'harshit'

from django.conf.urls.defaults import patterns , url
from facultyinfo.views import FacultyDetail,follow_faculty


urlpatterns = patterns( '',

    url( r'^(?P<user_id>[-\d]+)/(?P<username>[-\w]+)',FacultyDetail.as_view(), name = 'faculty_detail'),

    # url( r'^connected_faculty/$', faculty_connected_to_institute, name = 'connected_faculty' ),

    url(r'^follow_faculty/(?P<faculty_username>[-\w]+)/$',follow_faculty ,name='follow_faculty')
    )
