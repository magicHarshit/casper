from django.template.context import RequestContext
from django.views.generic.base import  View, TemplateView
from django.contrib.auth.models import User, Group
from django.http import  HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from InstituteInfo.forms import BulletinForm

from InstituteInfo.models import *

from InstituteInfo.views import extract_logo_path
from group_config.models import UserGroup

class FacultyDetail( TemplateView):
    template_name = 'facultyinfo/faculty.html'

    def get_context_data(self, **kwargs):
        username = kwargs.get('username')
        user = User.objects.get(username= username)
        bulletinForm = BulletinForm()
        all_bulletins = Bulletin.objects.filter(user = user)



        faculty_obj = FacultyInfo.objects.get(user = user)
        institute = faculty_obj.institute
        groups = UserGroup.objects.filter(owner= institute).values('name','id')
        connected_students = FacultyConnections.objects.filter(faculty=faculty_obj).values('student__user_id','student__user__username','student__images__photo','student__user__first_name')
        if 'Student' in self.request.user.groups.values_list('name',flat=True):
            connected = FacultyConnections.objects.filter(student__user=self.request.user,faculty=faculty_obj).count()
        image_path = extract_logo_path(user)
        return locals()

    def post(self, *args, **kwargs):
        wall_post = BulletinForm(data = self.request.POST)
        if wall_post.is_valid():
            wall_post_obj = wall_post.save(commit= False)
            wall_post_obj.user = self.request.user
            wall_post_obj.save()
            all_wall_posts = Bulletin.objects.filter(user = self.request.user)

            return HttpResponseRedirect("")
        return render_to_response("facultyinfo/faculty.html",locals(),context_instance = RequestContext(self.request))

# def faculty_connected_to_institute(request):
#     if 'Institute' in request.user.groups.values_list('name',flat = True):
#         institute = InstitueInfo.objects.get(user = request.user)
#     else:
#         institute = StudentInfo.objects.get(user=request.user).institute
#     faculties = FacultyInfo.objects.filter(institute = institute,profile = True).values('image__photo','user__first_name','user__last_name','user_id','user__username')
#     # faculties = ImageInfo.objects.filter(user__id__in = connected_faculties_id).values('photo','user__first_name','user__last_name')
#     # import pdb;pdb.set_trace()
#     return  render_to_response('instituteinfo/myfaculty.html', locals(), context_instance = RequestContext(request))

def follow_faculty(request,*args,**kwargs):
    faculty_username = kwargs.get('faculty_username')
    student_instance = StudentInfo.objects.get(user = request.user)
    faculty_instance = FacultyInfo.objects.get(user__username = faculty_username)
    faculty_connection_obj = FacultyConnections(student= student_instance,faculty=faculty_instance)
    faculty_connection_obj.save()
    return HttpResponse('Success')