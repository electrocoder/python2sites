"""
Profiles
"""

from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.db import models

@python_2_unicode_compatible
class Profile(models.Model):
    """
    Profile
        User:
            + username:
            + password:
            + email:
            + first_name:
            + last_name:
            + groups:
            + user_permissions:
            + is_staff:
            + is_active:
            + is_superuser:
            + last_login:
            + date_joined:
    """
    user                     = models.OneToOneField(User, on_delete=models.CASCADE)
    github_address           = models.URLField(max_length=70, blank=True)
    bitbucket_address        = models.URLField(max_length=70, blank=True)
    twitter_profile_name     = models.CharField(max_length=20, null=True, blank=True)
    facebook_profile_name    = models.CharField(max_length=20, null=True, blank=True)
    google_plus_profile_name = models.CharField(max_length=20, null=True, blank=True)
    views                    = models.PositiveSmallIntegerField(default=0)
    activation_key           = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.user.username
