from functools import wraps
from django.http import Http404

def authenticate_user(view_func):
    def _decorator(request, *args, **kwargs):
        # maybe do something before the view_func call
        if request.user != args.get('username'):
            raise Http404
        response = view_func(request, *args, **kwargs)
        # maybe do something after the view_func call
        return response
    return wraps(view_func)(_decorator)