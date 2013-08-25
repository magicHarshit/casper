from django import forms
from master.models import MyUser
from django.forms.models import modelform_factory
from master.models import UserSelf


StudentForm = modelform_factory(MyUser, fields=('unique_number', 'address',))

FacultyForm = modelform_factory(MyUser, fields=('qualification','work_experience', 'rating', 'address'))

InstituteForm = modelform_factory(MyUser, fields=('institute_type','establishment_year','address'))




#todo middleware

from django.contrib import auth

class AuthenticationMiddleware(object):
    def process_request(self, request):
        assert hasattr(request, 'session'), "The Django authentication middleware requires session middleware to be installed. Edit your MIDDLEWARE_CLASSES setting to insert 'django.contrib.sessions.middleware.SessionMiddleware'."

        request.user = auth.get_user(request)