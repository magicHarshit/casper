from django.db import models
from django.contrib.auth.models import User

# Create your models here.

REGISTRATION_CHOICES = (
    ('Institute','Institute'),
    ('Student','Student')
    )

class LoginDetail( models.Model ):

    user = models.ForeignKey( User, related_name = 'user_detail' )
    name = models.CharField( max_length = 500 )
    last_login = models.DateTimeField()
    ip_address = models.CharField( max_length = 150, blank = True, null = True )


