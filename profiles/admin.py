"""
Profiles
"""

from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'

class UserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ("username","first_name", "last_name", "email", "is_active", "last_login",)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
