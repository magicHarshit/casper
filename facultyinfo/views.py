from django.template.context import RequestContext
from django.views.generic.base import  View, TemplateView
from django.contrib.auth.models import User, Group
from django.http import  HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from InstituteInfo.forms import WallPostForm
from studentinfo.models import StudentInfo
from InstituteInfo.models import *
from models import FacultyInfo,FacultyConnections


class FacultyDetail( TemplateView):
    template_name = 'facultyinfo/faculty.html'

    def get_context_data(self, **kwargs):
        username = kwargs.get('username')
        id = kwargs.get('id')
        wall_post = WallPostForm()
        all_wall_posts = WallPost.objects.filter(user__username = username).values('wall_post','id','date_posted','group__name','group__id').order_by('-id')
        faculty_obj = FacultyInfo.objects.get(user__username = username)
        institute = faculty_obj.institute
        groups = StaticGroup.objects.filter(institute= institute).values('name','id')
        if 'Student' in self.request.user.groups.values_list('name',flat=True):
            connected = FacultyConnections.objects.filter(student__user=self.request.user,faculty=faculty_obj).count()
        return locals()

    def post(self, *args, **kwargs):
        wall_post = WallPostForm(data = self.request.POST)
        if wall_post.is_valid():
            wall_post_obj = wall_post.save(commit= False)
            wall_post_obj.user = self.request.user
            wall_post_obj.save()
            all_wall_posts = WallPost.objects.filter(user = self.request.user).values_list('wall_post',flat=True)

            return HttpResponseRedirect("")
        return render_to_response("facultyinfo/faculty.html",locals(),context_instance = RequestContext(self.request))

#login require,for faculty and student(group_required)
def faculty_connected_to_institute(request):
    if 'Institute' in request.user.groups.values_list('name',flat = True):
        institute = InstitueInfo.objects.get(user = request.user)
    else:
        institute = StudentInfo.objects.get(user=request.user).institute
    connected_faculty = FacultyInfo.objects.filter(institute = institute,profile = True).values('id','email','contact_number','address','qualification','work_experience','rating')
    return  render_to_response('instituteinfo/myfaculty.html', locals(), context_instance = RequestContext(request))


#decorator-login_required and group_required_student
def follow_faculty(request,*args,**kwargs):
    faculty_username = kwargs.get('faculty_username')
    student_instance = StudentInfo.objects.get(user = request.user)
    faculty_instance = FacultyInfo.objects.get(user__username = faculty_username)
    faculty_connection_obj = FacultyConnections(student= student_instance,faculty=faculty_instance)
    faculty_connection_obj.save()
    return HttpResponse('Success')