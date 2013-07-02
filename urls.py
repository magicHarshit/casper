from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.defaults import patterns, include, url
from django.views.i18n import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from userapp import urls
from django.conf import settings
from facultyinfo.views import FacultyDetail
admin.autodiscover()

js_info_dict = {
    'packages': ('InstituteInfo',),
}

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myorganisation.views.home', name='home'),
    # url(r'^myorganisation/', include('myorganisation.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),


    #(r'%s' % settings.ASKBOT_URL, include('askbot.urls')),
    #(r'^cache/', include('keyedcache.urls')), - broken views disable for now
    #(r'^settings/', include('askbot.deps.livesettings.urls')),
    #(r'^followit/', include('followit.urls')),
    #(r'^robots.txt$', include('robots.urls')),
    (r'^i18n/', include('django.conf.urls.i18n')),

    (r'^jsi18n/$', 'django.views.i18n.javascript_catalog', js_info_dict),

    (r'^jsi18n/(?P<packages>\S+?)/$', 'django.views.i18n.javascript_catalog'),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),

     url( r'^', include( 'userapp.urls' ) ),

     url( r'^institute/', include( 'InstituteInfo.urls' ) ),
	
     url( r'^group_config/', include( 'group_config.urls' ) ),

     url( r'^student/', include( 'studentinfo.urls' ) ),

     url( r'^faculty/', include( 'facultyinfo.urls' ) ),

    # url( r'^(?P<user_id>[-\d]+)/(?P<username>[-\w]+)/$', FacultyDetail.as_view(), name = 'faculty_detail' ),

     #url( r'^online-exam/', include( 'questionnaire.urls' ) ),

     url( r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT} ),

     url( r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT} ),

     #(r'^photologue/', include('photologue.urls')),
)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^rosetta/', include('rosetta.urls')),
    )
urlpatterns += staticfiles_urlpatterns()