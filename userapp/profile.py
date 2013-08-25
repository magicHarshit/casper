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
from master.models import UserSelf
from master.forms import InstituteForm, FacultyForm, StudentForm


class ProfileSubmission(TemplateView):
    template_name = 'userapp/profile_submission.html'

    def get_context_data(self, **kwargs ):
        user = get_user_model().objects.get(username=kwargs.get('username'))
        if user.user_type == 'Institute':
            form = InstituteForm(instance=user)
        elif user.user_type == 'Faculty':
            form = FacultyForm(instance=user)
        elif user.user_type == 'Student':
            form = StudentForm(instance=user)
        profile_user = user
        connected_to = UserSelf.objects.filter(target=self.request.user).values('source__first_name','source__last_name')
        return locals()

    def post(self, *args, **kwargs):
        user = self.request.user
        if user.user_type == 'Institute':
            form = InstituteForm(data=self.request.POST, instance=user)
            form.save()
            return HttpResponseRedirect(reverse('institute_profile', args=(self.request.user.username,)))
        elif user.user_type == 'Faculty':
            form = FacultyForm( self.request.POST, instance=user)
            form.save_m2m()
            return HttpResponse('Testing....')
        elif user.user_type == 'Student':
            form = StudentForm(self.request.POST, instance=user)
            form.save()
            return HttpResponseRedirect(reverse('student_inbox', args=(self.request.user.id,)))

        # client_mod = form.save(commit=False)
        # client_mod.save()
        # for groupe in form.cleaned_data.get('groupes'):
        #     clientgroupe = ClientGroupe(client=client_mod, groupe=groupe)
        #     clientgroupe.save()