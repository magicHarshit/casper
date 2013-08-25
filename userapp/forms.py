from django.contrib.auth.forms import  AuthenticationForm
from django import forms
from django.core.validators import email_re
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site
from django.template import Context, loader
from django.utils.http import int_to_base36

from InstituteInfo.models import USER_TYPE
from master.models import MyUser
from django.contrib.auth import get_user_model

class RegistrationForm(UserCreationForm):

    username = forms.CharField(label=_("Username"), max_length=30,
        help_text = _("Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only."),
        error_messages = {'invalid': _("Enter a valid email address"), },
        widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(label=_("Password"), widget=forms.PasswordInput(attrs={'placeholder':'Pasword'}))
    password2 = forms.CharField(label=_("Password confirmation"), widget=forms.PasswordInput(attrs={'placeholder':'Re-enter Pasword'}),
    help_text = _("Enter the same password as above, for verification."))

    first_name = forms.CharField(max_length= 100,widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length= 100,widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    user_type = forms.ChoiceField(choices=USER_TYPE)

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'user_type')

    def clean_password1(self):
        password1 = self.cleaned_data["password1"]
        if len(password1) < 10:
            raise forms.ValidationError("Enter a password of min 10 charcters")
        return password1

    def clean_username(self):
        username = self.cleaned_data["username"]
        if len(username) < 6:
            raise forms.ValidationError("Enter username of min 6 charcters")
        return username

class LoginAuthenticationForm( AuthenticationForm ):

    """
    Base class for authenticating users. Extend this to get a form that accepts
    username/password logins.
    """
    username = forms.CharField( max_length = 30, widget=forms.TextInput(attrs={'placeholder': 'Username','class':'span12'}) )
    password = forms.CharField( widget = forms.PasswordInput(attrs ={'placeholder':'Password','class':'span12'}) )


    def __init__( self, request = None, *args, **kwargs ):
        """
        If request is passed in, the form will validate that cookies are
        enabled. Note that the request (a HttpRequest object) must have set a
        cookie with the key TEST_COOKIE_NAME and value TEST_COOKIE_VALUE before
        running this validation.
        """
        self.request = request
        self.user_cache = None
        super( AuthenticationForm, self ).__init__( *args, **kwargs )

#class Change_Password_Form(forms.Form):
#    old_password = forms.CharField( widget = forms.PasswordInput )
#    new_password = forms.CharField( widget = forms.PasswordInput )
#    new_password_2 = forms.CharField( widget = forms.PasswordInput)
#
#    def clean_password2(self):
#        """
#        check whether new_pasword and new_password1 are matched or not
#        """
#        new_password = self.cleaned_data["new_password"]
#        new_password1 = self .cleaned_data["new_password1"]
#
#        if new_password != new_password1:
#            raise forms.ValidationError( _("Password Mismatch!!Enter Again") )
#        return new_password





class Password_Reset_Form( forms.Form ):
    email = forms.EmailField( label = _( "E-mail" ), max_length = 75 )

    def clean_email( self ):
        """
        Validates that a user exists with the given e-mail address.
        """
        email = self.cleaned_data["email"]
        self.users_cache = User.objects.filter( email__iexact = email )
        if len( self.users_cache ) == 0:
            raise forms.ValidationError( _( "This e-mail address doesn't have an associated user account. Are you sure you've registered?" ) )
        elif not( self.users_cache[0].is_active ):
            raise forms.ValidationError( _( "You have register but did not activate your account. Please activate your account, just click on the link sent to your Email while Registration." ) )
        return email

    def save( self, domain_override = None, email_template_name = 'registration/password_reset_email.html',
              use_https = False, token_generator = default_token_generator, from_email=None, request=None ):
        """
        Generates a one-use only link for resetting password and sends to the user
        """
        from django.core.mail import EmailMultiAlternatives
        from django.conf import settings
        for user in self.users_cache:
            if not domain_override:
                current_site = Site.objects.get_current()
                site_name = current_site.name
                domain = current_site.domain
            else:
                site_name = domain = domain_override
            t = loader.get_template( email_template_name )
            c = {
                'email': user.email,
                'domain': domain,
                'site_name': site_name,
                'uid': int_to_base36( user.id ),
                'user': user,
                'token': token_generator.make_token( user ),
                'protocol': use_https and 'https' or 'http',
                }
            subject = "Your New " + site_name + " Password!"
            message = t.render( Context( c ) )
            msg = EmailMultiAlternatives( subject, '', settings.DEFAULT_FROM_EMAIL, [user.email] )
            msg.attach_alternative( message, "text/html" )
            msg.send()

#            '''testing'''
#            from django.core.mail import send_mail

#            send_mail( subject, msg, 'from@example.com',
#                ['harshit.java@gmail.com'], fail_silently=False)
