"""
Profiles
"""

from __future__ import unicode_literals
from django.forms import ModelForm
from django import forms

from .models import Profile

class LoginForm(forms.Form):
    email    = forms.CharField(required=True)
    password = forms.CharField(required=True)

class SignupForm(forms.Form):
    username = forms.CharField(required=True)
    email    = forms.CharField(required=True)
    password = forms.CharField(required=True)
    news     = forms.BooleanField(required=True)

class ForgetPasswordForm(forms.Form):
    email  = forms.EmailField(required=True)

class ProfileForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Profile
        exclude = [
            'user',
            'activation_key',
            'views',
        ]

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            if i not in ['enable',]:
                self.fields[i].widget.attrs['class'] = 'form-control'
                self.fields[i].widget.attrs['name'] = i
