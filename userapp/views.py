# Create your views here.
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



class EndUserRegistration( TemplateView ):
    template_name = 'userapp/signup.html'


    def post( self, request, *args, **kwargs ):

        registration_form = RegistrationForm( data = self.request.POST )

        if  registration_form.is_valid():
            registration_form.save()
            user = User.objects.get(username = request.POST['username'])
            user.first_name = request.POST['first_name']
            user.first_name = request.POST['first_name']
            user.save()

            group = Group.objects.get(name = self.request.POST['groups'])
            group.user_set.add(user)
            form = AuthenticationForm( data = request.POST )

            auth_login( request, authenticate( username = request.POST['username'], password = request.POST['password1'] ) )
#            return HttpResponseRedirect(reverse('profile_submission'))
            return HttpResponseRedirect(reverse('profile', args = (self.request.user.id,self.request.user.username)))
        else:
            return render_to_response( 'userapp/signup.html', locals(), context_instance = RequestContext( self.request ) )


class EndUserLogin( TemplateView ):
    template_name = 'userapp/index.html'


    def get(self,request,**kwargs):
        if self.request.user.is_authenticated():
            if 'Institute' in self.request.user.groups.values_list('name',flat = True):
                try:
                    InstitueInfo.objects.get(user = request.user).profile
                    return HttpResponseRedirect(reverse('institute_profile'))
                except:
                    return HttpResponseRedirect(reverse('profile', args = (self.request.user.id,self.request.user.username)))
            elif 'Student' in self.request.user.groups.values_list('name',flat = True) :
                try:
                    StudentInfo.objects.get(user = request.user).profile
                    return HttpResponseRedirect(reverse('student_inbox'))
                except:
                    return HttpResponseRedirect(reverse('profile', args = (self.request.user.id,self.request.user.username)))

            elif 'Faculty' in self.request.user.groups.values_list('name',flat = True) :
               try:
                   FacultyInfo.objects.get(user = request.user).profile
                   return HttpResponseRedirect(reverse('faculty_detail', args = (self.request.user.id,self.request.user.username)))
               except:
                return HttpResponseRedirect(reverse('profile', args = (self.request.user.id,self.request.user.username)))

        else:
            login_form = LoginAuthenticationForm()
            registration_form = RegistrationForm()
            return render_to_response( 'userapp/index.html', locals(), context_instance = RequestContext( self.request ) )

    def post(self,request,*args,**kwargs):
        self.request = request
        login_form = LoginAuthenticationForm(data= self.request.POST)
        registration_form = RegistrationForm()
        if  login_form.is_valid():
            self.redirect_to = self.request.POST.get('next','/')
            auth_login( self.request, login_form.get_user() )

            if self.request.session.test_cookie_worked():
                self.request.session.delete_test_cookie()

            self.user = User.objects.get( username = self.request.POST['username'] )

            if 'Institute' in self.request.user.groups.values_list('name',flat = True):
                try:
                    InstitueInfo.objects.get(user = request.user).profile
                    return HttpResponseRedirect(reverse('institute_profile'))
                except:
                    return HttpResponseRedirect(reverse('profile', args = (self.request.user.id,self.request.user.username)))
            elif 'Student' in self.request.user.groups.values_list('name',flat = True) :
                try:
                    StudentInfo.objects.get(user = request.user).profile
                    return HttpResponseRedirect(reverse('student_inbox'))
                except:
                    return HttpResponseRedirect(reverse('profile', args = (self.request.user.id,self.request.user.username)))

            elif 'Faculty' in self.request.user.groups.values_list('name',flat = True) :
#                try:
#                    return  HttpResponse('Tetsing Process ..')
#                    StudentInfo.objects.get(user = request.user).profile
#                    return HttpResponseRedirect(reverse('student_inbox'))
#                except:
                return HttpResponseRedirect(reverse('profile', args = (self.request.user.id,self.request.user.username)))
#

        else:
            err_msg = 'Enter a Valid Username password'
            return render_to_response('userapp/index.html',locals(),context_instance = RequestContext(self.request))



class ChangePassword( TemplateView ):
     template_name = 'userapp/change_password.html'

     def get_context_data( self, *kwargs):
         change_password_form = SetPasswordForm(self.request.user)
         return locals()

     def post(self, request, *args , **kwargs):
         change_password_form = SetPasswordForm(self.request.user, self.request.POST )
         if change_password_form.is_valid():
             change_password_form.save()

         return HttpResponse('Password Changed Successfully')


def logout( request ):
    from django.contrib.auth import logout
    logout( request )
    response = HttpResponseRedirect( '/' )
    return response
