from django.contrib.auth.forms import AuthenticationForm
from django.template.context import RequestContext
from userapp.forms import  LoginAuthenticationForm, RegistrationForm
from django.views.generic.base import  View, TemplateView
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User, Group
from django.http import  HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from studentinfo.forms import StudentInfoForm
from forms import InstituteInfoForm, WallPostForm
from django.core.urlresolvers import reverse
from studentinfo.models import StudentInfo
from models import WallPost, InstitueInfo, ImageInfo
from master.forms import ImagesInfoForm
from InstituteInfo.models import *
from crop import crop_image
import copy
from django.utils.decorators import method_decorator
import settings
from bulletinMail import sendMailThread
from django.core import serializers
from django.forms.models import modelform_factory
from forms import CsvInfoForm
from models import CsvInfo
import csv
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from facultyinfo.models import FacultyInfo
from group_config.models import UserGroup
from django.utils.decorators import method_decorator
from endless_pagination.decorators import page_template


class PaginationMixin(object):
    # @method_decorator(page_template('instituteinfo/pagination.html'))
    def dispatch(self, request, *args, **kwargs):
        return super(PaginationMixin, self).dispatch(request, *args, **kwargs)

class InstituteProfile( PaginationMixin,TemplateView):
    template_name = 'instituteinfo/institute_profile.html'

    def get_context_data(self,extra_context=None, **kwargs):
        wall_post = WallPostForm()
        all_wall_posts = WallPost.objects.filter(user = self.request.user).values('wall_post','id','date_posted','group__name','group__id','user__username').order_by('-id')

        page_template='instituteinfo/pagination.html'
        if self.request.is_ajax():
            self.template_name=page_template

        institute = InstitueInfo.objects.get(user = self.request.user)
        image_path = extract_logo_path(self.request.user)
        students = StudentInfo.objects.filter(institute = institute, status = 'Pending').values('user')
        students_ids = [student['user'] for student in students]
        student_users = User.objects.filter(id__in = students_ids).values('username','id')
        faculty_images = extract_faculty_info(institute)
        student_images = extract_student_info(institute)
        groups = UserGroup.objects.filter(owner= institute).values('name','id')
        return locals()

    def post(self, *args, **kwargs):
        wall_post = WallPostForm(data = self.request.POST)
        if wall_post.is_valid():
            wall_post_obj = wall_post.save(commit= False)
            wall_post_obj.user = self.request.user
            wall_post_obj.save()
            all_wall_posts = WallPost.objects.filter(user = self.request.user).values_list('wall_post',flat=True)
            thread_obj = sendMailThread(self.request)
            thread_obj.start()
            return HttpResponseRedirect(".")
        return render_to_response("instituteinfo/institute_profile.html",locals(),context_instance = RequestContext(self.request))

def extract_logo_path(user):
    image_path = ImageInfo.objects.filter( user = user).values('photo')
    return image_path


def delete_post(request, id):
    wall_post = WallPost.objects.get(id = id)
    wall_post.delete()
    return HttpResponseRedirect(reverse('institute_profile'))


class EditImage(TemplateView):
    template_name = 'instituteinfo/crop_image.html'
    def get_context_data(self, **kwargs):
        form = ImagesInfoForm()
        return locals()


def ajax_save_images( request ):

    if request.user.is_authenticated():

        img_crop_dict = copy.deepcopy( eval( request.POST['crop_dictionary'] ) )
        for file_key, file_val in request.FILES.items():
            extra_details = ImageInfo.objects.filter( user = request.user, type = 'Profile' )

            if  len( extra_details ) <= 0:
                file_val.name = str( request.user.id ) + '_' + file_key + '.' + file_val.name.split( '.' )[-1]
                extra_details = ImageInfo( user = request.user, type = 'Profile', photo = file_val )
                extra_details.save()
            else:
                extra_details = extra_details[0]
                counter = extra_details.photo.name.split( '.' )[0].split( '_' )[-1]
                try:
                    counter = int( counter ) + 1
                except Exception:
                    counter = 0
                old_pic_name = extra_details.photo.name
                temp_list = old_pic_name.split( 'c_' )[-1].split( '.' )[0].split( '_' )
                tmp_var = temp_list[0]
                new_pic_name = tmp_var + '_' + str( counter ) + '.' + old_pic_name.split( '.' )[-1]
                file_val.name = new_pic_name
                extra_details.photo = file_val
                extra_details.save()
            if img_crop_dict.has_key( 'upfile'):
                crop_dict = img_crop_dict['upfile']
                crop_dict['image_name'] = extra_details.photo.name

                path = crop_image( crop_dict )
                extra_details.photo.name = path
                extra_details.save()
        path_image = settings.MEDIA_URL + path
        return HttpResponse( path_image )
    else:
        return HttpResponse( 'error in uploading file' )

class StudentVerification(TemplateView):
    template_name = 'instituteinfo/student_verification.html'

    def get_context_data(self,**kwargs):
        return locals()

    def post(self, *args, **kwargs):
        student = StudentInfo.objects.get(user__id = self.request.POST['student_id'])
        if self.request.POST['status']=='Confirm':
            student.status = 'Verified'
        else:
            student.status = 'Rejected'
        student.save()
        return HttpResponseRedirect(reverse('institute_profile'))


class CsvInfoUpload(TemplateView):
    template_name = 'instituteinfo/search.html'

    def get_context_data(self, **kwargs):
        form = CsvInfoForm()
        institute = InstitueInfo.objects.get(user = self.request.user)
        groups = StaticGroup.objects.filter(institute= institute).values('name','id')
        csv_objs = CsvInfo.objects.filter(institute = institute).values('file_upload','id','group__name')
        return locals()

    def post(self, *args, **kwargs):
        form = CsvInfoForm(self.request.POST, self.request.FILES)#todo check for csv file, size check
        if form.is_valid():
            form_obj = form.save(commit = False)
            form_obj.institute = InstitueInfo.objects.get(user = self.request.user)
            form_obj.save()
        return HttpResponseRedirect(reverse('csv_upload'))





#todo: expensive ;for each user:5 db hit;optimize it
def registrationFromCsv(request):
#todo thread process, check if email id is already registered,add user to student group,add user to StudentInfo
    obj = CsvInfo.objects.get(id = request.POST['csv_obj_id'])
    try:
        csv_reader_fd = csv.reader( open( settings.MEDIA_ROOT+'/'+obj.file_upload.name,'rb' ) )
    except IOError as e:
        return HttpResponse("error in reading the file %s" %(e))
    try:

        header = csv_reader_fd.next()
        for each_row in csv_reader_fd:

            data = dict(zip(header, each_row))
            header = each_row
            exclude_fields = ['username','email']

            model_form = modelform_factory(StudentInfo)


            username = data['username']
            if User.objects.filter(username = data['username']):
                pass
            else:
                random_number = User.objects.make_random_password(length=10, allowed_chars='123456789')#todo static/send password as a mail
                form = UserCreationForm(data = {'username':username,'password1':random_number,'password2':random_number})
                #todo-save group.studentinfo, connect to institute
                form.save()#todo exception handling
                group = Group.objects.get(name = 'student')
                user = User.objects.get(username = username)
                group.user_set.add(user)
                institute = InstitueInfo.objects.get(user = request.user)
                data.update({'institute':institute.id,'status':'Verified','user':user.id,'profile':True})
                form = model_form(data)
                if form.is_valid():
                    form.save()
                subject = "Your New Password!"
                message = random_number
                msg = EmailMultiAlternatives( subject, '', settings.DEFAULT_FROM_EMAIL, (data['email'],) )
                msg.attach_alternative( message, "text/html" )

                try:
                    msg.send()
                except:
                    pass
    except:
        return HttpResponse('Error in reading the file,Please Upload Correct Csv File')
    return HttpResponse('msg sent')

def students_connected_to_institute(request):

    institute = InstitueInfo.objects.get(user = request.user)
    connected_students_ids = StudentInfo.objects.filter(institute = institute, status = 'Verified', profile = True).values_list('user_id',flat=True)
    students = ImageInfo.objects.filter(user__id__in = connected_students_ids).values('photo','user__first_name','user__last_name')
    return  render_to_response('instituteinfo/mystudents.html', locals(), context_instance = RequestContext(request))



def delete_student(request):
    student_instance = StudentInfo.objects.get(id = request.POST['id'])
    student_instance.delete()
    return HttpResponseRedirect(reverse('connected_students'))

def delete_faculty(request):

    faculty_instance = FacultyInfo.objects.get(id = request.POST['id'])
    faculty_instance.delete()
    return HttpResponseRedirect(reverse('connected_faculty'))


def change_wall_group(request,group_id,wall_id):
    '''
    change the group of wall post
    '''
    group_instance = StaticGroup.objects.get(id = group_id)
    wall_obj = WallPost.objects.get(id = wall_id)
    wall_obj.group= group_instance
    wall_obj.save()
    return HttpResponse(True)

def groups(request,group_id,student_id):
    '''
    change student group
    '''
    student_obj = StudentInfo.objects.get(id = student_id)
    group_instance = StaticGroup.objects.get(id = group_id)
    student_obj.insti_group= group_instance
    student_obj.save()
    return HttpResponse(True)

def delete_csv(request):
    obj = CsvInfo.objects.get(id = request.POST['csv_obj_id'])
    obj.delete()#todo delete file
    return HttpResponseRedirect(reverse('csv_upload'))

def extract_student_info(institute):
    students = StudentInfo.objects.filter(institute=institute,status='Verified').values('user_id','user__username').order_by('?')[:4]
    user_ids = [student['user_id'] for student in students]
    image_info = ImageInfo.objects.filter( user__id__in = user_ids).values('photo','user__first_name')
    return image_info


def extract_faculty_info(institute):
    faculties = FacultyInfo.objects.filter(institute=institute).values('user_id','user__username').order_by('?')[:4]
    user_ids = [faculty['user_id'] for faculty in faculties]
    image_info = ImageInfo.objects.filter( user__id__in = user_ids).values('photo','user__first_name')
    return image_info
