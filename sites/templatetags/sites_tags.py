"""
Sites
"""

from __future__ import unicode_literals
from django import template
from django.utils.html import mark_safe
import time
import os

from python2sites.settings import WEBSITE_NAME

from sites.models import Site
from tags.models import Tag

register = template.Library()

@register.simple_tag
def version():
    """
    GIT version
    """
    try:
        return time.strftime('%m%d%Y/%u', time.gmtime(os.path.getmtime('.git/')))
    except:
        return 0

@register.simple_tag
def website_name():
    """
    WEBSITE_NAME = "Python2Sites"
    """
    return WEBSITE_NAME

@register.simple_tag
def total_sites():
    """
    """
    return Site.objects.filter(enable=True).count()

@register.simple_tag
def tags():
    """
    To optimize please...
    """
    import collections

    tag = Tag.objects.all()

    tag_list = []

    for i in tag:
        t = i.name.split(',')
        for j in t:
            if not j == '':
                tag_list.append(j.strip())

    results = collections.Counter(tag_list)

    return results


