
from django.db import models
from django.contrib.auth.models import User
from InstituteInfo.models import InstitueInfo
from studentinfo.models import StudentInfo
from studentinfo.choices import STATUS_CHOICES
from master.models import ImageInfo


class FacultyInfo(models.Model):

    user = models.ForeignKey(User)
    institute = models.ForeignKey( InstitueInfo )
    email = models.EmailField()
    status = models.CharField(max_length = 100, choices = STATUS_CHOICES, default = 'Pending' )
    profile = models.BooleanField(default= False, blank= True )
    contact_number = models.CharField(max_length = 12)
    address = models.CharField(max_length = 100)
    qualification = models.CharField(max_length = 100)
    work_experience = models.CharField(max_length = 100)
    rating = models.FloatField(default= 0)
    # image = models.ManyToManyField( ImageInfo, through='FacultyImages' )
    connections = models.ManyToManyField( StudentInfo, through='FacultyConnections' )

    def __unicode__(self):
        return str(self.user)


class FacultyConnections(models.Model):
    faculty = models.ForeignKey(FacultyInfo)
    student = models.ForeignKey(StudentInfo)

    def __unicode__(self):
        return str(self.faculty) + '-'+ str(self.student)



# class FacultyImages(models.Model):
#     institute = models.ForeignKey(InstitueInfo)
#     image = models.ForeignKey(ImageInfo)
#
#     def __unicode__(self):
#         return self.institute + '-' +  self.image

