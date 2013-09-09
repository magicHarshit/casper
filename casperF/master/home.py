from django.contrib.auth.forms import AuthenticationForm
from django.template.context import RequestContext
from django.views.generic.base import  View, TemplateView
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User, Group
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.views.generic.base import RedirectView
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import get_user_model

from bulletins.models import Bulletin
from .models import UserGroup, UserSelf, MyUser


class UserDetail(TemplateView):
    template_name = 'master/home.html'

    def get_context_data(self,extra_context=None, **kwargs):
        username = self.request.user.get('username')
        all_bulletins = Bulletin.objects.filter(user__username=username).values('title', 'id', 'body').order_by('-id')
        page_template = 'bulletins/pagination.html'
        if self.request.is_ajax():
            self.template_name = page_template
        user = get_user_model().objects.get(username=username)
        groups = UserGroup.objects.filter(owner__username=username).values('name','id')
        return locals()

    # def post(self, *args, **kwargs):
    #     wall_post = WallPostForm(data = self.request.POST)
    #     if wall_post.is_valid():
    #         wall_post_obj = wall_post.save(commit= False)
    #         wall_post_obj.user = self.request.user
    #         wall_post_obj.save()
    #         all_wall_posts = WallPost.objects.filter(user = self.request.user).values_list('wall_post',flat=True)
    #         thread_obj = sendMailThread(self.request)
    #         thread_obj.start()
    #         return HttpResponseRedirect(".")
    #     return render_to_response("instituteinfo/institute_profile.html",locals(),context_instance = RequestContext(self.request))

def connected_students(request, username):
    group = request.POST.get('group', None)
    connected_students = UserSelf.objects.filter(source__username=username)
    if group:
        connected_students = connected_students.objects.filter(group=group)
    connected_students = connected_students.values('target__photo', 'target__first_name', 'target__last_name','taget__unique_number')
    return render_to_response('master/connected_students.html', locals(), context_instance=RequestContext(request))



def connected_faculties(request,username):
    group = request.POST.get('group', None)
    connected_faculties = UserSelf.objects.filter(source__username=username)
    if group:
        connected_students = connected_faculties.objects.filter(group=group)
    connected_students = connected_faculties.values('target__photo', 'target__first_name', 'target__last_name', 'target__qualification')
    return render_to_response('master/connected_faculties.html', locals(), context_instance=RequestContext(request))


