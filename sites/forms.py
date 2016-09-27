# -*- coding: utf-8 -*-

from django.forms import ModelForm
from .models import *

class SiteForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Site
        exclude = [
            'user',
            'slug',
            'enable',
            'views',
            'img',
        ]

    def __init__(self, *args, **kwargs):
        super(SiteForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            if i not in ['enable',]:
                self.fields[i].widget.attrs['class'] = 'form-control'
                self.fields[i].widget.attrs['name'] = i

