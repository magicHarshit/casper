from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models
from django.contrib.auth.models import AbstractUser

from .choices import INSTITUTE_TYPE, LIST_YEAR, USER_TYPE, STATUS_CHOICES


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

class UserGroup( models.Model):
    name = models.CharField(max_length = 100,)
    description = models.TextField()
    owner = models.ForeignKey(MyUser, blank=True, null=True)

    def __unicode__(self):
        return str(self.name)+ '-'  + str(self.owner)

class CsvInfo(models.Model):
    # institute = models.ForeignKey( InstitueInfo )
    group = models.ForeignKey ( UserGroup )
    type = models.CharField(max_length = 100,choices=USER_TYPE)
    file_upload = models.FileField( upload_to = file_path)
    objects = models.Manager()

    def __unicode__(self):
        return str(self.file_upload)

def file_path( instance,filename):
    return "uploads/csv/%s" %(filename)

class UserSelf(models.Model):
    source = models.ForeignKey(MyUser, related_name='source')
    target = models.ForeignKey(MyUser, related_name='target')
    group = models.ForeignKey(UserGroup, null=True, blank=True)

post_save.connect(post_save_default_image, sender= MyUser)