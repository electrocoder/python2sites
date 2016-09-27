"""
Sites
"""

from __future__ import unicode_literals
from django import template
from python2sites.settings import WEBSITE_NAME
import time
import os

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
    """
    tag = Tag.objects.all()

    tag_list = ''

    for i in tag:
        t = (i.name.split(','))
        for j in t:
            tag_list += """<a href = "/?tag=%s" > %s </a>""" % (j, j)

    return tag_list

