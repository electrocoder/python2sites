"""
Tags
"""

from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class Tag(models.Model):
    """
    Tag
    """
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name
