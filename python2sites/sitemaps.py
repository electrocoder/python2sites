# -*- coding: utf-8 -*-

from django.contrib.sitemaps import Sitemap
from django.db.models import Q
from sites.models import Site

class SiteSitemap(Sitemap):
    changefreq = "always"
    priority = 0.5

    def items(self):
        return Site.objects.filter(enable=True)

    def lastmod(self, obj):
        return obj.pub_date
