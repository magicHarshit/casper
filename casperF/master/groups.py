from django.contrib.auth.forms import AuthenticationForm
from django.template.context import RequestContext
from django.views.generic.base import  View, TemplateView
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User, Group
from django.http import  HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from .forms import GroupConfigurationForm
from .models import UserGroup

class UserGroupConfiguration(TemplateView):
    template_name = 'master/group_config.html'

    def get_context_data(self, **kwargs):
        form = GroupConfigurationForm()
        return locals()

    def post(self, *args, **kwargs):
        form = GroupConfigurationForm(data=self.request.POST)
        if form.is_valid():
            obj = form.save(commit= False)
            obj.owner = self.request.user
            obj.save()
            return HttpResponseRedirect(reverse('group_listing', args=(self.request.user.username,)))


def get_group_listing(request, **kwargs):
    username = kwargs.get('username')
    user = get_user_model().objects.get(username=username)
    groups = UserGroup.objects.filter(owner=user).values('name', 'description')
    return render_to_response('master/group_listing.html', locals(), context_instance=RequestContext(request))


def delete_group(request, *kwargs):
    group_id = request.POST.get('id')
    group = UserGroup.objects.filter(id=group_id)
    group.delete()
    return HttpResponseRedirect(reverse('group_listing', args=(request.user.username,)))


def edit_group(request, group_id):
    group_instance = UserGroup.objects.get(id=group_id)
    form = GroupConfigurationForm(instance=group_instance)
    return render_to_response('master/group_config.html', locals(), context_instance=RequestContext(request))
