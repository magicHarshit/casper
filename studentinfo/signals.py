
from django.db.models.signals import post_save
from InstituteInfo.signals import post_save_default_image
from studentinfo.models import StudentInfo

# post_save.connect(post_save_default_image, sender= StudentInfo )