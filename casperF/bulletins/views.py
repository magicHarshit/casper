from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import Http404

from .models import Bulletin, Comment
from .forms import BulletinForm, commentform
from .decorators import authenticate_user

def show_bulletin(request, bulletin_id):
    bulletin = Bulletin.objects.get(id=bulletin_id)
    comments = Comment.objects.filter(bulletin=bulletin).values('posted_by', 'reply', 'posted')
    return render_to_response('bulletins/bulletin.html', locals(), context_instance=RequestContext(request))

@authenticate_user
def submit_bulletin(request):
    bulletin_form = BulletinForm(data=request.POST)
    if bulletin_form.is_valid():
        bulletin = bulletin_form.save(commit=False)
        bulletin.user = request.user
        bulletin.save()
    else:
        return render_to_response('bulletins/new_bulletin.html', locals(), context_instance=RequestContext(request))
    return HttpResponseRedirect(reverse('home', args=(request.user.username,)))

@authenticate_user
def delete_bulletin(request, bulletin_id):
    bulletin = Bulletin.objects.get(id=bulletin_id)
    bulletin.delete()
    return HttpResponseRedirect(reverse('home', args=(request.user.username,)))


def submit_comment(request):
    comment_form= Comment(data = request.POST)
    if comment_form.is_valid():
        comment = comment_form(commit=False)
        comment.user = request.user
        comment.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def delete_comment(request,comment_id):
    comment = Comment.objects.get(id=comment_id)
    if comment.posted_by == request.user or comment.owner__user == request.user:
        comment.delete()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        raise Http404






