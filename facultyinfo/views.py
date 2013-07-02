from django.template.context import RequestContext
from django.views.generic.base import  View, TemplateView
from django.contrib.auth.models import User, Group
from django.http import  HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from InstituteInfo.forms import WallPostForm
from studentinfo.models import StudentInfo
from InstituteInfo.models import *
from models import FacultyInfo


class FacultyDetail( TemplateView):
    template_name = 'facultyinfo/faculty.html'

    def get_context_data(self, **kwargs):
        wall_post = WallPostForm()
        all_wall_posts = WallPost.objects.filter(user = self.request.user).values('wall_post','id','date_posted','group__name','group__id').order_by('-id')
        institute = FacultyInfo.objects.get(user = self.request.user).institute
        groups = StaticGroup.objects.filter(institute= institute).values('name','id')
        return locals()

    def post(self, *args, **kwargs):
        wall_post = WallPostForm(data = self.request.POST)
        if wall_post.is_valid():
            wall_post_obj = wall_post.save(commit= False)
            wall_post_obj.user = self.request.user
            wall_post_obj.save()
            all_wall_posts = WallPost.objects.filter(user = self.request.user).values_list('wall_post',flat=True)
            return HttpResponseRedirect(".")#todo new
        return render_to_response("facultyinfo/faculty.html",locals(),context_instance = RequestContext(self.request))


