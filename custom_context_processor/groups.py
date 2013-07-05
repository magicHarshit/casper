__author__ = 'harshit'

def base_items(request):
    if request.user.is_authenticated():
        group_names = request.user.groups.values_list('name',flat=True)
        if 'Faculty' in group_names:
            return {'group_type':'Faculty'}
        if 'Institute' in group_names:
            return {'group_type':'Institute'}
        if 'Student' in group_names:
            return {'group_type':'Student'}
    return {'group_type':None}
