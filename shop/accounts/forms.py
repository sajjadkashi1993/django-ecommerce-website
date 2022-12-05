from .models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# import re
# from django import forms


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('phone',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('phone',)
