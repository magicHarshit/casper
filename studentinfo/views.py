__author__ = 'harshit'
from django.contrib.auth.forms import AuthenticationForm
from django.template.context import RequestContext
from userapp.forms import  LoginAuthenticationForm, RegistrationForm
from django.views.generic.base import  View, TemplateView
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User, Group
from django.http import  HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse

from InstituteInfo.models import Bulletin
from django.views.static import serve
from InstituteInfo.views import extract_logo_path

from django.db.models import Q
from django.contrib.auth import get_user_model
from master.models import UserSelf



class StudentProfile(TemplateView):
    template_name = 'studentinfo/profile.html'

    def get_context_data(self, **kwargs):     
        return locals()
    
    def post(self, *args, **kwargs):
        return HttpResponse('stuentinfo/profile.html',locals(),context_instance = RequestContext(self.request))


class StudentInbox(TemplateView):
    template_name = 'studentinfo/inbox.html'

    def get_context_data(self, **kwargs):

        user_id = kwargs.get('user_id')
        user = get_user_model().objects.get(id=user_id)
        connections = UserSelf.objects.filter(target=self.request.user)
        if len(connections) == 0:
            message = 'Connect Yourself with Institute,search from search box'
            return locals()
        if user.status == 'Pending':
            message = 'Please Wait! your request is Under Process'
            return locals()
        elif user.status == 'Rejected':
            message = 'Your request is rejected by institute'
            return locals()
        # connected_faculty_user = UserSelf.objects.filter(target=self.request.user, source__user_type='Faculty').\
        #     values('source__first_name', 'source__last_name', 'source__photo')

        # all_bulletins = Bulletin.objects.filter(user = institute.user)#todo

        return locals()

def instituteListing(request):
    institutes = InstitueInfo.objects.all()
    return render_to_response('studentinfo/institute_listing.html',locals(),context_instance = RequestContext(request))

def facultyListing(request,insti_id):
    faculties = FacultyInfo.objects.filter(institute__id=insti_id)
    return render_to_response('studentinfo/faculty_listing.html',locals(),context_instance = RequestContext(request))