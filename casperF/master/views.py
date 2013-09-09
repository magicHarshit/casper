from django.contrib.auth.forms import AuthenticationForm
from django.template.context import RequestContext
from django.views.generic.base import  View, TemplateView
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User, Group
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.views.generic.base import RedirectView
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import get_user_model
from .forms import LoginAuthenticationForm, RegistrationForm

class EndUserRegistration(TemplateView):
    template_name = 'master/signup.html'

    def post( self, request, *args, **kwargs ):
        registration_form = RegistrationForm(data=self.request.POST)
        if registration_form.is_valid():
            registration_form.save()
            user = User.objects.get(username=request.POST['username'])
            user.save()
            form = AuthenticationForm(data =request.POST )
            auth_login(request, authenticate(username=request.POST['username'], password = request.POST['password1']))
            return HttpResponseRedirect(reverse('profile', args=(self.request.user.username,)))
        else:
            return render_to_response(self.template_name, locals(), context_instance=RequestContext(self.request))

class EndUserLogin(TemplateView):
    template_name = 'master/index.html'

    def get(self,request,**kwargs):
        if self.request.user.is_authenticated():
            return HttpResponseRedirect(reverse('profile', args=(self.request.user.username,)))
        else:
            login_form = LoginAuthenticationForm()
            registration_form = RegistrationForm()
            return render_to_response(self.template_name, locals(), context_instance=RequestContext(self.request))

    def post(self, request, *args, **kwargs):
        self.request = request
        login_form = LoginAuthenticationForm(data=self.request.POST)
        registration_form = RegistrationForm()
        if login_form.is_valid():
            self.redirect_to = self.request.POST.get('next', '/')
            auth_login(self.request, login_form.get_user())
            if self.request.session.test_cookie_worked():
                self.request.session.delete_test_cookie()
            return HttpResponseRedirect(reverse('profile', args=(self.request.user.username,)))
        else:
            err_msg = 'Enter a Valid Username password'
            return render_to_response(self.template_name, locals(), context_instance=RequestContext(self.request))


def logout( request ):
    from django.contrib.auth import logout
    logout( request )
    response = HttpResponseRedirect('/')
    return response


class ChangePassword(TemplateView):
    template_name = 'master/change_password.html'

    def get_context_data( self, *kwargs):
        change_password_form = SetPasswordForm(self.request.user)
        return locals()

    def post(self, request, *args, **kwargs):
        change_password_form = SetPasswordForm(self.request.user, self.request.POST)
        if change_password_form.is_valid():
            change_password_form.save()
        return HttpResponse('Password Changed Successfully')




