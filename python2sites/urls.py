"""
python2sites URL Configuration
"""

from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from django.http import HttpResponse
from django.contrib.sitemaps.views import sitemap

from sites import views as sites
from profiles import views as profiles

from .feeds import * # rss
from .sitemaps import * # sitemaps

urlpatterns = [
    url(r'^$', sites.index, name='index'),
    url(r'^detail/(?P<slug>[^/]*)/$', sites.detail, name='detail'),
    url(r'^@(?P<username>[^/]*)/$', sites.username, name='username'),
    url(r'^submit-site/$', sites.site_add, name='site_add'),
    url(r'^site-update/(?P<slug>[^/]*)/$', sites.site_update, name='site_update'),

    url(r'^statistics/$', sites.statistics, name='statistics'),
    url(r'^statistic-language/$', sites.statistic_language, name='statistic_language'),
    url(r'^statistic-framework/$', sites.statistic_framework, name='statistic_framework'),
    url(r'^statistic-operating-system/$', sites.statistic_operating_system, name='statistic_operating_system'),
    url(r'^statistic-webserver/$', sites.statistic_webserver, name='statistic_webserver'),
    url(r'^statistic-database/$', sites.statistic_database, name='statistic_database'),
    url(r'^statistic-method/$', sites.statistic_method, name='statistic_method'),
    url(r'^statistic-python-version/$', sites.statistic_python_version, name='statistic_python_version'),

    # user profile
    url(r'^login/$', profiles.user_login, name='login'),
    url(r'^signup/$', profiles.user_signup, name='signup'),
    url(r'^logout/$', profiles.user_logout, name='logout'),
    url(r'^forget-password/$', profiles.user_forget_password, name='user_forget_password'),
    url(r'^user/activation/(?P<key>[^/]*)/$', profiles.user_activation, name='user_activation'),
    url(r'^profile/$', profiles.profile, name='profile'),

    url(r'^about/$', sites.about, name='about'),

    url(r'^admin/', include(admin.site.urls)),

    # yandex mail
    url(r'^a0214dcfb209\.html$', lambda r: HttpResponse("e485605de1a2", content_type="text/plain")),  # yandex mail

    url(r'^rss/$', Feed()),  # rss

    url(r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /static/", content_type="text/plain")),
]

sitemaps = {
    'sites': SiteSitemap,
}

urlpatterns += [
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

urlpatterns += [
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT, }),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
