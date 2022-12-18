from django import forms
from core.validators import PhoneValidator
from .models import ProfileUser,User


class UserLoginRegisterForm(forms.Form):
    phone = forms.CharField(validators=(PhoneValidator,))


class VerifyCodeForm(forms.Form):
    code = forms.IntegerField ()


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))

    class Meta:
        model = ProfileUser
        fields = ('gender', 'birthday', 'bio', 'image')
        widgets = {
            'gender':forms.Select(attrs={'class':'form-control'}),
            'birthday':forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'bio':forms.Textarea(attrs={'rows': 4,'class':'form-control' }),
            'image':forms.FileInput(attrs={'class':'form-control','accept':"image/*"})
        }
        