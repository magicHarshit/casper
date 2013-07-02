__author__ = 'harshit'


from django.db import models
from InstituteInfo.models import InstitueInfo
from django.contrib.auth.models import User
from choices import STATUS_CHOICES
from group_config.models import StaticGroup

class StudentInfo(models.Model):

    user = models.ForeignKey(User)
    institute = models.ForeignKey( InstitueInfo )
    status = models.CharField(max_length = 100, choices = STATUS_CHOICES, default = 'Pending' )
    profile = models.BooleanField(default= False, blank= True )
    unique_number = models.CharField(max_length= 30 )
    first_name = models.CharField( max_length = 100 )
    last_name = models.CharField(max_length= 100)
    insti_group = models.ForeignKey(StaticGroup,null=True,blank=True)

    def __unicode__(self):
        return str(self.user)


