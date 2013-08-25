from django.db import models
# from InstituteInfo.models import InstitueInfo
from django.utils.encoding import smart_str



from master.models import MyUser
class UserGroup( models.Model):
    name = models.CharField(max_length = 100,)
    description = models.TextField()
    owner = models.ForeignKey(MyUser,blank=True,null=True)

    def __unicode__(self):
        return str(self.name)+ '-'  + str(self.owner)