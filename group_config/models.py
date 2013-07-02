__author__ = 'harshit'



from django.db import models
from InstituteInfo.models import InstitueInfo
from django.utils.encoding import smart_str


class Group(models.Model):
    '''
    model for dynamic group configuraion
    '''

    name = models.CharField ( max_length = 100 )
    institute = models.ForeignKey ( InstitueInfo  )#TO-DO
    tag_to = models.ForeignKey( 'self', null= True , blank= True )


    def __unicode__(self):
        return self.name

#        return smart_str(self.name + self.tag_to)

#from studentinfo.models import StudentInfo
#class StudentGroupInfo( models.Model ):
#
#    student = models.ForeignKey ( StudentInfo )
#    group = models.ForeignKey(Group )
#
#    def __unicode__(self):
#        return str(self.student)
#        return smart_str( self.student + self.group)

class StaticGroup( models.Model):
    '''
    model for static group configuration through form

    '''
    name = models.CharField(max_length = 100)
    description = models.TextField()
    institute = models.ForeignKey(InstitueInfo, null= True, blank= True)

    def __unicode__(self):
        return str(self.name)+ '-'  + str(self.institute)