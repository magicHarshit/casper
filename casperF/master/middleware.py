from django.contrib import auth

class AuthenticationMiddleware(object):
    def process_request(self, request):
        assert hasattr(request, 'session'),\
            "The Django authentication middleware requires session middleware to be installed. Edit your MIDDLEWARE_CLASSES setting to insert 'django.contrib.sessions.middleware.SessionMiddleware'."
        request.user = auth.get_user(request)