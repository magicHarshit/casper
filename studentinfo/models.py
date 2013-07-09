from django.db import models
from InstituteInfo.models import InstitueInfo
from django.contrib.auth.models import User
from choices import STATUS_CHOICES
from group_config.models import UserGroup


class StudentInfo(models.Model):

    user = models.ForeignKey(User)
    institute = models.ForeignKey( InstitueInfo )
    status = models.CharField(max_length = 100, choices = STATUS_CHOICES, default = 'Pending' )
    profile = models.BooleanField(default= False, blank= True )
    unique_number = models.CharField(max_length= 30 )
    groups= models.ManyToManyField( UserGroup, through='StudentGroup' )

    def __unicode__(self):
        return str(self.user)


class StudentGroup(models.Model):
    student = models.ForeignKey(StudentInfo)
    group = models.ForeignKey(UserGroup)