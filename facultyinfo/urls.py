__author__ = 'harshit'

from django.conf.urls.defaults import patterns , url
from facultyinfo.views import FacultyDetail



urlpatterns = patterns( '',

    url( r'^(?P<user_id>[-\d]+)/(?P<username>[-\w]+)$', FacultyDetail.as_view(), name = 'faculty_detail' ),
    )
