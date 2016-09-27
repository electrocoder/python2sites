"""
Sites
"""

from __future__ import unicode_literals
from django.contrib import admin

from .models import Site

class SiteAdmin(admin.ModelAdmin):
    """
    """
    list_display = ('pk', 'user', 'title', 'language', 'framework', 'operating_system', 'webserver', 'database', 'method', 'python_version', 'enable', 'views',)
    prepopulated_fields = {"slug": ("web_site_address",)}

admin.site.register(Site, SiteAdmin)
