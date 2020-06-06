from django.shortcuts import render, redirect
from django.views.generic import View
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages


class IndexView(View):
    def post(self, *args, **kwargs):
        phone_no = self.request.POST.get('phone')
        name = self.request.POST.get('name')
        subject = 'From My Online Portfolio. Phone: ' + phone_no
        from_email = self.request.POST.get('email')
        message = self.request.POST.get('message') + ' ' +'from: ' + from_email + ' '+ 'Name: ' + name
        try:
            send_mail(subject, message, from_email, ['nkosisiboniso@yahoo.com'])
        except BadHeaderError:
            return redirect('/')
        messages.success(self.request, f'Email sent successfully. Thank you!')
        return redirect('/')

    def get(self, *args, **kwargs):
        return render(self.request, 'core/index.html')
