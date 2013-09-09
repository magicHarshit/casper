import datetime

from django.db import models
from master.models import MyUser,UserGroup

def blog_file_path( instance, filename ):
    return "uploads/blog/%s" %(filename )


class Bulletin(models.Model):
    user = models.ForeignKey(MyUser)
    group = models.ForeignKey(UserGroup)
    title = models.CharField(max_length=500)
    body = models.TextField()
    attachments = models.FileField(upload_to=blog_file_path,null=True,blank=True)
    date_posted = models.DateTimeField(default=datetime.datetime.now(), null= True)

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    posted_by = models.ForeignKey(MyUser)
    reply = models.CharField(max_length= 1000)
    bulletin = models.ForeignKey(Bulletin)
    posted = models.DateTimeField(auto_now_add=True,default=datetime.datetime.now())

    def __unicode__(self):
        return str(self.bulletin)
