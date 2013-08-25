from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from InstituteInfo.choices import INSTITUTE_TYPE,LIST_YEAR,USER_TYPE
from studentinfo.choices import STATUS_CHOICES
from django.db import models
from django.contrib.auth.models import ( AbstractUser)
# from group_config.models import UserGroup


def imagepath(instance, filename):
    """ Computes the infrastructure images upload path """
    return "uploads/user_images/%s/%s" % (instance.user.id, str(filename).replace(" ", "-"))


class MyUser(AbstractUser):
    photo = models.ImageField(upload_to=imagepath)
    user_type = models.CharField(max_length=25, choices=USER_TYPE)
    institute_type = models.CharField(max_length=25, choices=INSTITUTE_TYPE )
    establishment_year = models.IntegerField(blank=True, null=True, choices=LIST_YEAR )
    address = models.TextField()
    profile = models.BooleanField(default=False, blank=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='Pending')
    qualification = models.CharField(max_length=100)
    work_experience = models.CharField(max_length=100)
    rating = models.FloatField(default=0)
    unique_number = models.CharField(max_length=30)
    connections = models.ManyToManyField("self", through='UserSelf', symmetrical=False)

    def __unicode__(self):
        return self.username

def post_save_default_image(sender, instance, **kwargs):
    if kwargs['created'] is True:
        photo = "uploads/user_images/%s/%s" % ('default', str('images.jpeg').replace(" ", "-"))
        instance.photo = photo
        instance.save()

class UserSelf(models.Model):
    source = models.ForeignKey(MyUser, related_name='source')
    target = models.ForeignKey(MyUser, related_name='target')
    group = models.ForeignKey('group_config.UserGroup', null=True, blank=True)

post_save.connect(post_save_default_image, sender= MyUser)