from django import forms


class ContactForm(forms.Form):
    comment = forms.CharField()
    name = forms.CharField()
    email = forms.EmailField()