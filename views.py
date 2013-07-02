import os
from django.shortcuts import render_to_response

def home(request):
    return render_to_response('home/home.html')

def my_upload_success_handler(request, form, original):
    """
    Success upload handler
    """
    print "Uploda form data", form.cleaned_data
    print "File uploaded to " % original.image.path

    # This handler do nothing, but print parameters

    from django.shortcuts import redirect
    return redirect(original)

def my_crop_success_handler(request, form, original, cropped):
    """
    Custom crop handler
    """
    print "Crop form data", form.cleaned_data
    print "Original object: %s" % original
    print "Original in cropped model (the same in previous line): %s" % cropped.original
    print "Cropped image: %s" % cropped.image

    # For example, we can use cropped image as user profile avatar
    # Perhaps user is authenticated and skip checks ;)

    from django.core.files.base import ContentFile
    from django.contrib import messages
    from django.shortcuts import redirect
    import os

    profile = request.user.get_profile()
    profile.avatar.save(
        os.path.basename(cropped.image.path),
        ContentFile(cropped.image.path)
    )

    messages.success(request, 'Avatar uploaded and cropped')
    return redirect(request.user)

