__author__ = 'harshit'
from django.contrib.auth.forms import AuthenticationForm
from django.template.context import RequestContext
from django.views.generic.base import  View, TemplateView
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User, Group
from django.http import  HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from group_config.forms import  GroupConfigurationForm
from models import UserGroup
from InstituteInfo.models import InstitueInfo
from InstituteInfo.views import extract_logo_path

class UserGroupConfiguration(TemplateView):
    template_name = 'group_config/static_group_config.html'

    def get_context_data(self,**kwargs):
        form = GroupConfigurationForm()
        return locals()

    def post(self, *args,**kwargs):

        form = GroupConfigurationForm( data = self.request.POST)
        if form.is_valid():
            obj = form.save(commit= False)
            obj.owner = InstitueInfo.objects.get(user = self.request.user)
            obj.save()
            'reverse to group listing'
            return HttpResponseRedirect(reverse('static_group_listing'))

def get_group_listing(request):
    institute = InstitueInfo.objects.get(user = request.user)
    image_path = extract_logo_path(request.user)
    groups = UserGroup.objects.filter(owner = institute)
    form = GroupConfigurationForm()
    return render_to_response('group_config/static_group_listing.html', locals(), context_instance = RequestContext(request))

def delete_group(request,*kwargs):
    id = request.POST.get('id')
    group = UserGroup.objects.filter(id = id)
    group.delete()
    return HttpResponseRedirect(reverse('static_group_listing'))
#    return render_to_response('group_config/static_group_listing.html', locals(), context_instance = RequestContext(request))

def edit_group(request,group_id):

    group_instance = UserGroup.objects.get(id = group_id)
    form = GroupConfigurationForm(instance = group_instance )
    return render_to_response('group_config/static_group_config.html', locals(), context_instance = RequestContext(request))





