from django.db.models.signals import post_save
from InstituteInfo.signals import post_save_default_image
from facultyinfo.models import FacultyInfo,FacultyImages
from master.models import ImageInfo

def post_save_default_image(sender,instance,**kwargs):
    if kwargs['created'] == True:
        photo = "uploads/user_images/%s/%s" % ( 'default', str( 'images.jpeg' ).replace( " ", "-" ) )
        image_obj = ImageInfo(user=instance.user,active=True,type='Profile',photo=photo)
        image_obj.save()
        faculty_image_obj = FacultyImages(image=image_obj,faculty=instance)
        faculty_image_obj.save()