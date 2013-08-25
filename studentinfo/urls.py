
from django.conf.urls.defaults import patterns , url
from studentinfo.views import StudentInbox,instituteListing,facultyListing


urlpatterns = patterns( '',
         url( r'^(?P<user_id>[-\d]+)/$', StudentInbox.as_view(), name = 'student_inbox' ),

         url( r'^search/$', instituteListing, name = 'institute_listing' ),

         url( r'^search/(?P<insti_id>[-\d]+)$', facultyListing, name = 'faculty_listing' ),
         # url( r'^faculty/$', StudentInbox.as_view(), name = 'faculty_list' ),
)
