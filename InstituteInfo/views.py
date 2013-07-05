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
from forms import InstituteInfoForm, WallPostForm
from django.core.urlresolvers import reverse
from studentinfo.models import StudentInfo
from models import WallPost, InstitueInfo, ExtraDetails
from forms import InstituteSearchForm, ExtraDetailsForm
from InstituteInfo.models import *
from crop import crop_image
import copy
from django.utils.decorators import method_decorator
#todo Mairajkhan
#from endless_pagination.decorators import page_template
import settings
from bulletinMail import sendMailThread
from django.core import serializers
from django.forms.models import modelform_factory


class PaginationMixin(object):
    #TODO Mairajkhan
    #@method_decorator(page_template('instituteinfo/pagination.html'))
    def dispatch(self, request, *args, **kwargs):
        return super(PaginationMixin, self).dispatch(request, *args, **kwargs)


class InstituteProfile( PaginationMixin,TemplateView):
    template_name = 'instituteinfo/institute_profile.html'

    def get_context_data(self, **kwargs):
        wall_post = WallPostForm()

        all_wall_posts = WallPost.objects.filter(user = self.request.user).values('wall_post','id','date_posted','group__name','group__id','user__username').order_by('-id')
        institute = InstitueInfo.objects.get(user = self.request.user)

        students = StudentInfo.objects.filter(institute = institute, status = 'Pending').values('user')
        students_ids = [student['user'] for student in students]
        student_users = User.objects.filter(id__in = students_ids).values('username','id')
        image_path = extract_logo_path(institute)
        groups = StaticGroup.objects.filter(institute= institute).values('name','id')
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

def extract_logo_path(institute):
    image_path = ExtraDetails.objects.filter( appldetail = institute).values('photo')
    if image_path:
        image_path = image_path[0]
    return image_path


def delete_post(request, id):
    wall_post = WallPost.objects.get(id = id)
    wall_post.delete()
    return HttpResponseRedirect(reverse('institute_profile'))


class EditImage(TemplateView):
    template_name = 'instituteinfo/crop_image.html'
    def get_context_data(self, **kwargs):
        form = ExtraDetailsForm()
        return locals()


def ajax_save_images( request ):

    app_id = request.user.id
    if app_id:

        app_obj = InstitueInfo.objects.get( user__id = app_id )
        img_crop_dict = copy.deepcopy( eval( request.POST['crop_dictionary'] ) )

        for file_key, file_val in request.FILES.items():
            extra_details = ExtraDetails.objects.filter( appldetail = app_obj, type = file_key )

            if  len( extra_details ) <= 0:
                file_val.name = str( app_obj.id ) + '_' + file_key + '.' + file_val.name.split( '.' )[-1]
                extra_details = ExtraDetails( appldetail = app_obj, type = file_key, photo = file_val )
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

            if img_crop_dict.has_key( 'id_' + file_key ):
                crop_dict = img_crop_dict['id_' + file_key]
                crop_dict['image_name'] = extra_details.photo.name
                path = crop_image( crop_dict )
                extra_details.photo.name = path
                extra_details.save()
#        import pdb;pdb.set_trace()
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


from forms import CsvInfoForm
from models import CsvInfo

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



import csv
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import EmailMultiAlternatives
from django.conf import settings


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
#        csv_fd.writerow( header )
#        import pdb;pdb.set_trace()
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
#                student_instance = StudentInfo(user = user, institute = institute, status = 'Verified',profile = True,insti_group= obj.group)
#                student_instance.save()
#                import pdb;pdb.set_trace()
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
    connected_students = StudentInfo.objects.filter(institute = institute, status = 'Verified', profile = True).values('id','unique_number','user__username','first_name','last_name','insti_group__name','insti_group__id')
    groups = StaticGroup.objects.filter(institute= institute).values('name','id')

    return  render_to_response('instituteinfo/mystudents.html', locals(), context_instance = RequestContext(request))


#def faculty_connected_to_institute(request):
#
#    institute = InstitueInfo.objects.get(user = request.user)
#    connected_faculty = StudentInfo.objects.filter(institute = institute, status = 'Verified', profile = True).values('id','unique_number','user__username','first_name','last_name','insti_group__name','insti_group__id')
#    groups = StaticGroup.objects.filter(institute= institute).values('name','id')
#
#    return  render_to_response('instituteinfo/mystudents.html', locals(), context_instance = RequestContext(request))
#

from facultyinfo.models import FacultyInfo
# def faculty_connected_to_institute(request):
#     institute = InstitueInfo.objects.get(user = request.user)
#     connected_faculty = FacultyInfo.objects.filter(institute = institute,profile = True).values('id','email','contact_number','address','qualification','work_experience','rating')
#     return  render_to_response('instituteinfo/myfaculty.html', locals(), context_instance = RequestContext(request))


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



#release 2
#to be corrected later
#college connection co-square

class InstituteSearch(TemplateView):
    template_name = 'instituteinfo/search.html'
    def get_context_data(self, **kwargs):
        form = InstituteSearchForm()
        return locals()

    def post(self, * args, **kwargs):
        search = self.request.POST.get('search')
        institutes_search_results = InstitueInfo.objects.filter(name__icontains = search).values('name','description','id')
        return render_to_response('instituteinfo/search.html',locals(),context_instance = RequestContext(self.request))

def add_institutes(request):

    parent_insti = InstitueInfo.objects.get(user = request.user)
    child_insti = InstitueInfo.objects.get(id = request.POST.get('institute_id'))
    insti_con_obj = InstitutesConnection(parent_insti = parent_insti, child_insti = child_insti )
    insti_con_obj.save()
    insti_con_obj = InstitutesConnection(parent_insti = child_insti, child_insti = parent_insti )
    insti_con_obj.save()
    return  HttpResponseRedirect(reverse('connected_institutes'))

def connected_institutes(request):
    connected_institutes = InstitutesConnection.objects.filter(parent_insti__user = request.user )
    return  render_to_response('instituteinfo/search.html', locals(), context_instance = RequestContext(request))


def delete_csv(request):
    obj = CsvInfo.objects.get(id = request.POST['csv_obj_id'])
    obj.delete()#todo delete file
    return HttpResponseRedirect(reverse('csv_upload'))