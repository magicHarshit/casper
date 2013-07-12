__author__ = 'harshit'


from django.db import models
from django.contrib.auth.models import User
import datetime
from choices import IMAGE_TYPE


class BasicCofigurationFields( models.Model ):
    name = models.CharField( max_length = 250 )
    slug = models.SlugField( default = '', max_length = 100 )
    created_date = models.DateTimeField( default = datetime.datetime.now(), auto_now_add = True )
    modified_date = models.DateTimeField( default = datetime.datetime.now(), auto_now = True )
    display_flag = models.BooleanField( default = True )

    objects = models.Manager()

    class Meta:
        abstract = True


def imagepath( instance, filename ):
    """ Computes the infrastructure images upload path """
    return "uploads/user_images/%s/%s" % ( instance.user.id, str( filename ).replace( " ", "-" ) )



class ImageInfo( models.Model ):
    user = models.ForeignKey(User, blank = True, null = True )
    photo = models.ImageField( upload_to=imagepath )
    active = models.BooleanField(default=False)
    type = models.CharField(max_length=100,choices=IMAGE_TYPE)
    objects = models.Manager()

    def __unicode__(self):
        return self.user + '-' + self.type
