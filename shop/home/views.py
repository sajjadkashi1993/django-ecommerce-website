from django.shortcuts import render
from django.views.generic import View
from django.contrib import messages
from django.core.mail import send_mail

from .forms import ContactForm


class ContactUsView(View):
    form_class = ContactForm
    template_name = 'contact-us.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd =form.cleaned_data
            message = cd['name'] + '\n' +cd['comment'] +'\nemail:' + cd['email']
            try:
                send_mail('contact us', message, 'sajjad.kashi29@gmail.com', ['sajjad.kashi29@gmail.com'])
                messages.success(request,'Your comment sended', 'success')
            except:
                messages.error(request,'Unfortunately, your comment was not sent', 'danger')

        return render(request, self.template_name, {'form':form})
