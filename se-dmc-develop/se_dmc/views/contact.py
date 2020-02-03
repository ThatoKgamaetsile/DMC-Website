from django.views.generic import TemplateView
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

class Contact(TemplateView):
    template_name = 'se_dmc/contact.html'

    def index(request):

        if request.method == 'POST':
            message = request.POST['message']
            send_mail('Contact Form',
                      message,
                      settings.EMAIL_HOST_USER,
                      ['thatokgamaetsile@gmail.com'],
                      fail_silently=False)
        return render(request, 'se_dmc/contact.html')





