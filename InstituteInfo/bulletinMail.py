
import threading
from django.core.mail import EmailMultiAlternatives
from studentinfo.models import StudentInfo
from InstituteInfo.models import InstitueInfo
import settings

class sendMailThread(threading.Thread):
    def __init__(self,request):
        self.request=request
        threading.Thread.__init__( self )

    def run(self):
        request = self.request
        sending_mail(request)


def sending_mail(request):

    institute = InstitueInfo.objects.get(user = request.user)
    students_connected = StudentInfo.objects.filter(institute = institute, status = 'Verified', profile = True).values_list('user__username',flat= True)
    for student in students_connected:
        message = request.POST['wall_post']
        msg = EmailMultiAlternatives( 'subject-New Wall Post', '', settings.EMAIL_HOST_USER, [student] )
        msg.attach_alternative( message, "text/html" )
        try:
            msg.send()
        except:
            pass

