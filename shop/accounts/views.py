from datetime import timedelta
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic.edit import FormView
from django.contrib import messages
from .forms import UserLoginRegisterForm, VerifyCodeForm
from django.contrib.auth import get_user_model, login, logout
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now
from django.contrib.auth.mixins import LoginRequiredMixin

import random
from .models import OtpCode
from .utils import send_otp_code
from .forms import ProfileForm
User = get_user_model()


class LoginRegisteruser(View):
    form_class = UserLoginRegisterForm
    template_name = 'accounts/login.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            otp_code = random.randint(1000, 9999)
            print(1111111111111111111111111111, otp_code)

            if OtpCode.objects.filter(phone=phone).exists():
                otp = OtpCode.objects.get(phone=phone)
                if otp.is_block():
                    messages.error(request, _('Your phone is blocked for today'), 'danger')
                    return render(request, self.template_name, {'form': form})
                else:
                    otp.code = otp_code
                    otp.number_try += 1
                    otp.save()
            else:
                OtpCode.objects.create(phone=phone, code=otp_code)
            # send_otp_code(phone, str(otp_code))
            request.session['user_login_info'] = {
                'phone': phone
            }
            messages.success(request, _('We sent a code'), 'success')
            return redirect('accounts:verify')
        return render(request, self.template_name, {'form': form})


class VerifyCodeview(View):
    form_class = VerifyCodeForm
    template_name = 'accounts/verify.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    def post(self, request):
        phone = request.session.get('user_login_info').get('phone')
        otp = OtpCode.objects.filter(phone=phone)[0]

        form = self.form_class(request.POST)
        if form.is_valid():
            code = form.cleaned_data.get('code')
            if str(code) == otp.code and otp.created_at - now() <= timedelta(minutes=2):
                if User.objects.filter(phone=phone).exists():
                    user = User.objects.get(phone=phone)
                else:
                    user = User.objects.create_user(phone=phone)

                login(request, user)
                otp.delete()
                messages.success(request, _('log in sucessfully'), 'success')
                return redirect('home:home')
            else:
                messages.error(request, _('this code is wrong or time out'), 'danger')
                return redirect('accounts:verify')
        return render(request, self.template_name, {'form': form})


class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            messages.success(request, _('log out sucessfully'), 'success')
            logout(request)
        return redirect('home:home')


class Accontview(LoginRequiredMixin,View):
    template_name = 'accounts/account.html'

    def get(self, request):
        initial = {
            'first_name' : request.user.first_name,
            'last_name' : request.user.last_name,
            'email' : request.user.email,
        }
        form = ProfileForm(instance=request.user.profile, initial=initial)
        return render(request, self.template_name,{'form':form})


class ProfileFormView(View):
    form_class = ProfileForm

    def post(self,request):
        profile = request.user.profile
        form = ProfileForm(data=request.POST, instance=profile)
        if form.is_valid():
            form.save()
            cd = form.cleaned_data
            request.user.first_name = cd['first_name']
            request.user.last_name = cd['last_name']
            request.user.email = cd['email'] 
            request.user.save()
            return JsonResponse({'msg':'Your profile updated', 'status':'success'}, status=200)
        return JsonResponse(form.errors, status=200)

    


