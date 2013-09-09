from django.contrib.auth.forms import AuthenticationForm
from django.template.context import RequestContext
from django.views.generic.base import  View, TemplateView
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User, Group
from django.http import  HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.views.generic.base import RedirectView
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import get_user_model

from .forms import InstituteForm, FacultyForm, StudentForm


class ProfileSubmission(TemplateView):
    template_name = 'master/profile_submission.html'

    def get_context_data(self, **kwargs):
        user = get_user_model().objects.get(username=kwargs.get('username'))
        user_type = user.user_type
        profile = user.profile
        if profile:
            return HttpResponseRedirect(reverse('home', args=(self.request.user.username,)))
        else:
            if user.user_type == 'Institute':
                form = InstituteForm(instance=user)
            elif user.user_type == 'Faculty':
                form = FacultyForm(instance=user)
            elif user.user_type == 'Student':
                form = StudentForm(instance=user)
            return locals()

    def post(self, *args, **kwargs):
        user = self.request.user
        user_type = user.user_type
        if user_type == 'Institute':
            form = InstituteForm(data=self.request.POST, instance=user)
        elif user_type == 'Faculty':
            form = FacultyForm( self.request.POST, instance=user)
        elif user_type == 'Student':
            form = StudentForm(self.request.POST, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home', args=(self.request.user.username,)))
        return render_to_response(self.template_name, locals(), context_instance=RequestContext(self.request))