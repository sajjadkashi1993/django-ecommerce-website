from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib import messages
from .forms import UserLoginRegisterForm, VerifyCodeForm

import random  
from .models import OtpCode 
from .utils import send_otp_code 


class LoginRegisteruser(View):
    form_class = UserLoginRegisterForm

    def get(self, request):
        form = self.form_class()
        return render(request, 'accounts/login.html',{'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        print(11111111111111)
        if form.is_valid():
            otp_code = random.randint(1000,9999)
            phone = form.cleaned_data['phone']
            print(1111111111111111111111111111, phone)
            send_otp_code(phone, otp_code)
            OtpCode.objects.create(phone=phone,code=otp_code)
            request.session['user_login_info']={
                'phone':phone
            }
            messages.success(request, 'We sent a code', 'success' )
            return redirect('accounts:verify')
        return render(request, 'accounts/login.html',{'form':form})

class VerifyCodeview(View):
    form_class = VerifyCodeForm

    def get(self, request):
        form = self.form_class()
        return render(request, 'accounts/verify.html',{'form':form})