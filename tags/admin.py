"""
Sites
"""

from __future__ import unicode_literals
from django.contrib import admin

from .models import Tag

class TagAdmin(admin.ModelAdmin):
    """
    """
    list_display = ('name',)

admin.site.register(Tag, TagAdmin)
