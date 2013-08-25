__author__ = 'harshit'

from django.conf.urls.defaults import patterns , url
from group_config.views import  UserGroupConfiguration,delete_group,edit_group

urlpatterns = patterns( '',

#         url( r'^$', GroupConfiguration.as_view(), name = 'group_config' ),

         url( r'^group_config/$', UserGroupConfiguration.as_view(), name = 'static_group_config' ),

#         url( r'^group_listing/$', StaticGroupListing.as_view(), name = 'static_group_listing' ),

         # url( r'^group_listing/$', get_group_listing, name = 'static_group_listing' ),

         url( r'^delete/$', delete_group, name = 'delete_group' ),

         url( r'^edit/(?P<group_id>[-\d]+)/$', edit_group, name = 'edit_group' ),
)
