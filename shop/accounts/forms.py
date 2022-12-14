from django import forms
from core.validators import PhoneValidator



class UserLoginRegisterForm(forms.Form):
    phone = forms.CharField(validators=(PhoneValidator,))


class VerifyCodeForm(forms.Form):
    code = forms.IntegerField ()


