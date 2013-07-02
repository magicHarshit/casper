__author__ = 'harshit'


from django.db import models
from master.models import City, BasicCofigurationFields
from django.core.validators import MaxLengthValidator, MinLengthValidator, validate_integer
from InstituteInfo.choices import LIST_YEAR,INSTITUTE_TYPE, INSTITUTE_USER
from master.models import *
from django.db.models.signals import post_save
#from image_cropping import ImageRatioField
#from thumbs import ImageWithThumbsField



def imagepath( instance, filename ):
    return "uploads/institute/%s/%s" % ( instance.slug, filename )


class InstitueInfo( BasicCofigurationFields):

    user = models.ForeignKey(User)
    type = models.CharField( max_length = 25, choices = INSTITUTE_TYPE )
    establishment_year = models.IntegerField( blank = True, null = True, choices = LIST_YEAR )
    email = models.EmailField( max_length = 50, blank = True, null = True )
    contact_numbers = models.CommaSeparatedIntegerField( max_length = 50, blank = True, null = True )
    address = models.TextField()
#    website = models.URLField( max_length = 200, blank = True, null = True)
    profile = models.BooleanField(default= False, blank= True)
#co-square
#    connected_institutes = models.ManyToManyField('self',through= InstitutesConnection, symmetrical= False)
#co-square end
    objects = models.Manager()
#    institute_manager = InstituteManager()

    def __unicode__( self ):
        return self.name


def post_save_default_group(sender,instance, **kwargs):
    if kwargs['created'] == True:
        group_instance = StaticGroup(name = 'All', description = 'Default Group', institute = instance)
        group_instance.save()

post_save.connect(post_save_default_group, sender= InstitueInfo)



#co-square
class InstitutesConnection(models.Model):
    parent_insti = models.ForeignKey(InstitueInfo, related_name= 'parent')
    child_insti = models.ForeignKey(InstitueInfo, related_name= 'child')

    def __unicode__(self):
        return str(self.child_insti) + '-' + str(self.parent_insti)
#co-square end

class InstituteUser( models.Model ):
    user_type = models.CharField( max_length = 50, choices = INSTITUTE_USER )
    name = models.CharField( max_length = 150 )
    email = models.EmailField( max_length = 150 )
    contact_number = models.CharField( max_length = 21, validators = [MaxLengthValidator( 10 ), MinLengthValidator( 10 ), validate_integer] )
    institute = models.ForeignKey( InstitueInfo )


class InstituteLocation( models.Model ):

    institute = models.ForeignKey( InstitueInfo )
    location = models.ForeignKey( City, blank = True, null = True, on_delete = models.SET_NULL )
    area = models.ForeignKey( Area, blank = True, null = True, on_delete = models.SET_NULL )
    locality = models.ForeignKey( Locality, blank = True, null = True, on_delete = models.SET_NULL )
    objects = models.Manager()

    def __unicode__( self ):
        try:
            return self.institute.name + '-' + self.location.name
        except:
            return self.institute.name + '-' + 'None'

    class Meta:
        unique_together = ( 'institute', 'location' )

from group_config.models import StaticGroup
class WallPost(models.Model):
    user = models.ForeignKey(User)
    group = models.ForeignKey(StaticGroup)
    wall_post = models.TextField()
    date_posted = models.DateTimeField(default=datetime.datetime.now(), null= True)

    def __unicode__(self):
        return self.wall_post

def signaturepath( instance, filename ):
    """ Computes the infrastructure images upload path """
    return "uploads/student_signature/%s/%s" % ( instance.appldetail.id, str( filename ).replace( " ", "-" ) )

class ExtraDetails( models.Model ):
    appldetail = models.ForeignKey( InstitueInfo, blank = True, null = True )
    type = models.CharField( max_length = 20 )
    #todo CharField was ImageField
    photo = models.ImageField( upload_to=signaturepath )
    objects = models.Manager()



from group_config.models import StaticGroup #todo

def file_path( instance,filename ):
    return "uploads/csv/%s" % ( filename )

class CsvInfo(models.Model):
    institute = models.ForeignKey( InstitueInfo )
    group = models.ForeignKey ( StaticGroup )#group #todo
    file_upload = models.FileField( upload_to = file_path)
    objects = models.Manager()

    def __unicode__(self):
        return str(self.file_upload)