

from studentinfo.models import StudentInfo
from master.models import ImageInfo
from studentinfo.models import StudentImages


def post_save_default_image(sender,instance,**kwargs):
    if kwargs['created'] == True:
        photo = "uploads/user_images/%s/%s" % ( 'default', str( 'images.jpeg' ).replace( " ", "-" ) )
        image_obj = ImageInfo(user=instance.user,active=True,type='Profile',photo=photo)
        image_obj.save()
        institute_image_obj = StudentImages(image=image_obj,institute=instance)
        institute_image_obj.save()

