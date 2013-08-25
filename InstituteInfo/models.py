from django.db import models
import datetime
from InstituteInfo.choices import USER_TYPE
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from master.models import MyUser


def file_path( instance,filename):
    return "uploads/csv/%s" %(filename )

def blog_file_path( instance, filename ):
    return "uploads/blog/%s" %(filename )


class Bulletin(models.Model):
    user = models.ForeignKey(MyUser)
    group = models.ForeignKey('group_config.UserGroup')#todo
    title = models.CharField(max_length=500)
    body = models.TextField()
    attachments = models.FileField(upload_to=blog_file_path,null=True,blank=True)
    date_posted = models.DateTimeField(default=datetime.datetime.now(), null= True)

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(MyUser)
    reply = models.CharField(max_length= 1000)
    bulletin = models.ForeignKey(Bulletin)
    posted = models.DateTimeField(auto_now_add=True,default=datetime.datetime.now())

    def __unicode__(self):
        return str(self.bulletin)

class CsvInfo(models.Model):
    # institute = models.ForeignKey( InstitueInfo )
    group = models.ForeignKey ( 'group_config.UserGroup' )
    type = models.CharField(max_length = 100,choices=USER_TYPE)
    file_upload = models.FileField( upload_to = file_path)
    objects = models.Manager()

    def __unicode__(self):
        return str(self.file_upload)
