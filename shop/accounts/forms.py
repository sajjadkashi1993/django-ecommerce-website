from django import forms
from core.validators import PhoneValidator
from .models import ProfileUser,User


class UserLoginRegisterForm(forms.Form):
    phone = forms.CharField(validators=(PhoneValidator,))


class VerifyCodeForm(forms.Form):
    code = forms.IntegerField ()


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = ProfileUser
        fields = ('gender', 'birthday', 'bio', 'image')