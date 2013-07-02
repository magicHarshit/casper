__author__ = 'harshit'

def base_items(request):
    try:
        group_type = request.user.groups.get(name = 'Institute').name
    except:
        try:
            group_type = request.user.groups.get(name = 'Student').name
        except:
            group_type = None
    return{
        'group_type':group_type
    }
