from django.conf.urls.defaults import patterns , url
from InstituteInfo.views import  StudentVerification,EditImage\
    , ajax_save_images, CsvInfoUpload, registrationFromCsv,\
    delete_student,groups,change_wall_group, delete_faculty,delete_csv,showCsvData,registerStudent,BulletinInfo,messages

urlpatterns = patterns( '',

     # url( r'^(?P<insti_id>[-\d]+)/$', InstituteProfile.as_view(), name = 'institute_profile' ),


	 url(r'^student_verification/$', StudentVerification.as_view(), name = 'student_verification' ),
	 # url( r'^delete/(?P<id>[-\d]+)$', delete_post, name = 'delete_post' ),

	 url( r'^edit_image/$', EditImage.as_view(), name = 'edit_image' ),

	 url( r'^ajax-save-image/$', ajax_save_images, name = 'ajax_save_image' ),

	 url( r'^csv/$', CsvInfoUpload.as_view(), name = 'csv_upload' ),

	 url( r'^register_users/$', registrationFromCsv, name = 'register_users' ),

	 # url( r'^connected_students/$', students_connected_to_institute , name = 'connected_students' ),

	 url( r'^delete_student/$', delete_student , name = 'delete_student' ),

     url( r'^delete_faculty/$', delete_faculty , name = 'delete_faculty' ),

	 url( r'^groups/(?P<group_id>[-\d]+)/(?P<student_id>[-\d]+)$', groups , name = 'groups' ),

	 url( r'^wallgroup/(?P<group_id>[-\d]+)/(?P<wall_id>[-\d]+)$', change_wall_group , name = 'change_wall_group' ),

     url( r'^delete_csv$', delete_csv , name = 'delete_csv' ),

     url( r'^csv_data/(?P<csv_id>[-\d]+)/$', showCsvData , name = 'show_csv_data' ),

     url( r'^register_student/$', registerStudent , name = 'register_student' ),

     url(r'^bulletin/(?P<bulletin_id>[-\d]+)/$',BulletinInfo.as_view(), name='show_bulletin'),

     url(r'^messages/$',messages, name='messages')

)