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
from InstituteInfo.forms import InstituteInfoForm
from django.core.urlresolvers import reverse
from studentinfo.models import StudentInfo
from group_config.forms import GroupConfigurationForm, StaticGroupConfigurationForm
from models import StaticGroup
from InstituteInfo.models import InstitueInfo

class StaticGroupConfiguration(TemplateView):
    template_name = 'group_config/static_group_config.html'

    def get_context_data(self,**kwargs):
        form = StaticGroupConfigurationForm()
        return locals()

    def post(self, *args,**kwargs):

        form = StaticGroupConfigurationForm( data = self.request.POST)
        if form.is_valid():
            obj = form.save(commit= False)
            obj.institute = InstitueInfo.objects.get(user = self.request.user)
            obj.save()
            'reverse to group listing'

        return HttpResponseRedirect(reverse('static_group_listing'))

def get_group_listing(request):
    institute = InstitueInfo.objects.get(user = request.user)
    groups = StaticGroup.objects.filter(institute = institute)
    return render_to_response('group_config/static_group_listing.html', locals(), context_instance = RequestContext(request))

def delete_group(request,*kwargs):
    id = request.POST.get('id')
    group = StaticGroup.objects.filter(id = id)
    group.delete()
    return HttpResponseRedirect(reverse('static_group_listing'))
#    return render_to_response('group_config/static_group_listing.html', locals(), context_instance = RequestContext(request))

def edit_group(request,group_id):

    group_instance = StaticGroup.objects.get(id = group_id)
    form = StaticGroupConfigurationForm(instance = group_instance )
    return render_to_response('group_config/static_group_config.html', locals(), context_instance = RequestContext(request))





