
from django.conf.urls.defaults import patterns , url
from studentinfo.views import StudentInbox


urlpatterns = patterns( '',
         url( r'^inbox/$', StudentInbox.as_view(), name = 'student_inbox' ),
         # url( r'^faculty/$', StudentInbox.as_view(), name = 'faculty_list' ),
)
