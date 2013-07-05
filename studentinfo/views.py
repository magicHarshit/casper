__author__ = 'harshit'


from django.contrib.auth.forms import AuthenticationForm
from django.template.context import RequestContext
from userapp.forms import  LoginAuthenticationForm, RegistrationForm
from django.views.generic.base import  View, TemplateView
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User, Group
from django.http import  HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from studentinfo.forms import StudentInfoForm
from InstituteInfo.forms import InstituteInfoForm, WallPostForm
from django.core.urlresolvers import reverse
from studentinfo.models import StudentInfo
from InstituteInfo.models import WallPost, InstitueInfo
from django.views.static import serve
from InstituteInfo.views import extract_logo_path
from facultyinfo.models import FacultyConnections
from django.db.models import Q



class StudentProfile(TemplateView):
    template_name = 'studentinfo/profile.html'

    def get_context_data(self, **kwargs):     
        return locals()
    
    def post(self, *args, **kwargs):
        return HttpResponse('stuentinfo/profile.html',locals(),context_instance = RequestContext(self.request))


class StudentInbox(TemplateView):
    template_name = 'studentinfo/inbox.html'

    def get_context_data(self, **kwargs):
        if StudentInfo.objects.get(user = self.request.user).status == 'Pending':
            message = 'Please Wait! your request is Under Process'
            return locals()
        elif StudentInfo.objects.get(user = self.request.user).status == 'Rejected':
            message = 'Your request is rejected by institute'
            return locals()
        student_instance = StudentInfo.objects.get(user = self.request.user, status = 'Verified')
        institute = student_instance.institute
        connected_faculty_user = FacultyConnections.objects.filter(student= student_instance).values_list('faculty__user',flat=True)
        all_wall_posts = WallPost.objects.filter(Q(user__in = connected_faculty_user,group__name__icontains = 'All') |
                                                Q(group = student_instance.insti_group)|
                                                Q(user=student_instance.institute.user,group__name__icontains = 'All')).values('wall_post','user__username','group__name')

        image_path = extract_logo_path(institute)
        return locals()

