# -*- coding: utf-8 -*-

from django.contrib.syndication.views import Feed

from sites.models import Site

from python2sites.settings import WEBSITE_NAME, WEBSITE_DESCRIPTION

class Feed(Feed):
    """
    RSS
    """
    title = WEBSITE_NAME
    link = "/rss/"
    description = WEBSITE_DESCRIPTION

    def items(self):
        return Site.objects.filter(enable=True)[:20]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description[0:50]

    def item_link(self, item):
        return item.get_absolute_url()
