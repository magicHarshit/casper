from django.db.models.signals import post_save
from InstituteInfo.signals import post_save_default_image
from facultyinfo.models import FacultyInfo

post_save.connect(post_save_default_image, sender= FacultyInfo)