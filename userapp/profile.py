from django.contrib.auth.forms import AuthenticationForm
from django.template.context import RequestContext
from userapp.forms import  LoginAuthenticationForm, RegistrationForm
from django.views.generic.base import  View, TemplateView
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User, Group
from django.http import  HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from studentinfo.forms import StudentInfoForm
from InstituteInfo.forms import InstituteInfoForm
from django.core.urlresolvers import reverse
from studentinfo.models import StudentInfo
from InstituteInfo.models import *
from InstituteInfo.views import extract_logo_path
from django.views.generic.base import RedirectView
from django.contrib.auth.forms import SetPasswordForm
from facultyinfo.models import FacultyInfo
from facultyinfo.forms import FacultyInfoForm


class ProfileSubmission(TemplateView):
    template_name = 'userapp/profile_submission.html'

    #TODO code repetion for getting instance in get and post remove it and fine solution '''
    def get_context_data( self, **kwargs ):
        institute_instance=None
        if 'Institute' in self.request.user.groups.values_list('name',flat = True):

            try:
                institute_instance = InstitueInfo.objects.get(user = self.request.user)
            except:
                institute_instance = None
            form = InstituteInfoForm( instance = institute_instance )

        elif 'Student' in self.request.user.groups.values_list('name',flat = True) :
            try:
                student_instance = StudentInfo.objects.get(user = self.request.user)
                institute_instance = student_instance.institute
            except:
                student_instance = None
                institute_instance = None

            form = StudentInfoForm( instance = student_instance )

        elif 'Faculty' in self.request.user.groups.values_list('name',flat = True) :
            try:
                faculty_instance = FacultyInfo.objects.get(user = self.request.user)
            except:
                faculty_instance = None
            form = FacultyInfoForm( instance = faculty_instance )
        # todo image only for institute,make it for all three
        # import pdb;pdb.set_trace()
        # import pdb;pdb.set_trace()
        image_path = extract_logo_path(self.request.user)
        return locals()

    def post(self, *args, **kwargs):

        if 'Institute' in self.request.user.groups.values_list('name',flat = True):
            try:
                institute_instance = InstitueInfo.objects.get(user = self.request.user)
            except:
                institute_instance = None
            form = InstituteInfoForm( self.request.POST, self.request.FILES ,instance= institute_instance)#request.files for banner and logo
        elif 'Student' in self.request.user.groups.values_list('name',flat = True):
            try:
                student_instance = StudentInfo.objects.get(user = self.request.user)
            except:
                student_instance = None
            form = StudentInfoForm ( data = self.request.POST, instance= student_instance)
        elif 'Faculty' in self.request.user.groups.values_list('name',flat = True):
            try:
                faculty_instance = FacultyInfo.objects.get(user = self.request.user)
            except:
                faculty_instance = None
            form = FacultyInfoForm( data = self.request.POST,instance = faculty_instance )


        if form.is_valid():
            obj = form.save( commit= False )
            obj.user = self.request.user
            obj.profile = True
            obj.save()
        else:
            return render_to_response('userapp/profile_submission.html',locals(),context_instance= RequestContext(self.request))

        if 'Institute' in self.request.user.groups.values_list('name',flat = True):
            return HttpResponseRedirect(reverse('institute_profile'))
        elif 'Student' in self.request.user.groups.values_list('name',flat = True):
            return HttpResponseRedirect(reverse('student_inbox'))
        elif 'Faculty' in self.request.user.groups.values_list('name',flat = True):
            # return HttpResponseRedirect(reverse('student_inbox'))
            return HttpResponse('Testing....')#todo