from django.db import models
import datetime
from master.models import BasicCofigurationFields,ImageInfo
from InstituteInfo.choices import LIST_YEAR,INSTITUTE_TYPE,USER_TYPE
# from group_config.models import UserGroup
from django.contrib.auth.models import User
from django.db.models.signals import post_save


def file_path( instance,filename ):
    return "uploads/csv/%s" % ( filename )


class InstitueInfo( BasicCofigurationFields):

    user = models.ForeignKey(User)
    type = models.CharField( max_length = 25, choices = INSTITUTE_TYPE )
    establishment_year = models.IntegerField( blank = True, null = True, choices = LIST_YEAR )
    email = models.EmailField( max_length = 50, blank = True, null = True )
    contact_numbers = models.CommaSeparatedIntegerField( max_length = 50, blank = True, null = True )
    address = models.TextField()
    profile = models.BooleanField(default= False, blank= True)
    image = models.ManyToManyField( ImageInfo, through='InstituteImages' )
    objects = models.Manager()

    def __unicode__( self ):
        return str(self.user)

class InstituteImages(models.Model):
    institute = models.ForeignKey(InstitueInfo)
    image = models.ForeignKey(ImageInfo)

    def __unicode__(self):
        return self.institute + '-' +  self.image

class WallPost(models.Model):
    user = models.ForeignKey(User)
    group = models.ForeignKey('group_config.UserGroup')#todo
    wall_post = models.TextField()
    date_posted = models.DateTimeField(default=datetime.datetime.now(), null= True)

    def __unicode__(self):
        return self.wall_post


class CsvInfo(models.Model):
    institute = models.ForeignKey( InstitueInfo )
    group = models.ForeignKey ( 'group_config.UserGroup' )
    type = models.CharField(max_length = 100,choices=USER_TYPE)
    file_upload = models.FileField( upload_to = file_path)
    objects = models.Manager()

    def __unicode__(self):
        return str(self.file_upload)




from InstituteInfo.signals import post_save_default_image,post_save_extra_info
post_save.connect(post_save_default_image, sender= InstitueInfo)
post_save.connect(post_save_extra_info, sender= InstitueInfo)
