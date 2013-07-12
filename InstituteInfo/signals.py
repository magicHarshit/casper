from django.db.models.signals import post_save
from group_config.models import UserGroup
from InstituteInfo.models import InstitueInfo,ImageInfo,InstituteImages
from django.template.defaultfilters import slugify

def post_save_extra_info(sender,instance, **kwargs):
    if kwargs['created'] == True:
        slug = slugify(instance.name)
        instance.slug = slug
        instance.save()
        group_instance = UserGroup(name = 'All', description = 'Default Group', institute = instance)
        group_instance.save()


def post_save_default_image(sender,instance,**kwargs):
    if kwargs['created'] == True:
        photo = "uploads/user_images/%s/%s" % ( 'default', str( 'images.jpeg' ).replace( " ", "-" ) )
        image_obj = ImageInfo(user=instance.user,active=True,type='Profile',photo=photo)
        image_obj.save()
        institute_image_obj = InstituteImages(image=image_obj,institute=instance)
        institute_image_obj.save()

# post_save.connect(post_save_extra_info, sender= InstitueInfo)
# post_save.connect(post_save_default_image, sender= InstitueInfo)
