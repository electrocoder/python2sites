"""
Sites
"""

from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

from python2sites.settings import LOGIN_URL, emailmsg, DEFAULT_FROM_EMAIL, WEBSITE_NAME, TO

from sites.models import *
from .forms import SiteForm

from tags.models import Tag

def index(request):
    """
    :param request:
    :return:
    """
    values = Site.objects.filter(enable=True).order_by('-pub_date')

    try:
        sites_with_source = request.GET['source']
        print('source')
        if sites_with_source == 'True':
            print('source true')
            values = values.exclude(source_code_address='')
    except:
        pass

    try:
        tag = request.GET['tag']
        values = values.filter(tags__contains=tag)
    except:
        pass

    paginator = Paginator(values, 18)

    page = request.GET.get('page')
    try:
        values_p = paginator.page(page)
    except PageNotAnInteger:
        values_p = paginator.page(1)
    except EmptyPage:
        values_p = paginator.page(paginator.num_pages)

    return render(request, "index.html", locals())

def detail(request, slug):
    """
    :param request:
    :return:
    """
    value = get_object_or_404(Site, slug=slug)
    value.view_count()

    if request.user == value.user:
        site_edit = True

    return render(request, "detail.html", locals())

def username(request, username):
    """
    :param request:
    :return:
    """
    values = Site.objects.filter(user__username=username, enable=True).order_by('-pub_date')

    username = username

    paginator = Paginator(values, 18)

    page = request.GET.get('page')
    try:
        values_p = paginator.page(page)
    except PageNotAnInteger:
        values_p = paginator.page(1)
    except EmptyPage:
        values_p = paginator.page(paginator.num_pages)

    return render(request, "index.html", locals())

@login_required(login_url=LOGIN_URL)
@csrf_exempt
def site_add(request):
    """
    :param request:
    :return:
    """
    msg_ok = ""
    msg_err = ""

    form = SiteForm()

    if request.method == 'POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()

            Tag(name=f.tags).save()

            # admin
            msg = (u"Hi admin;\n\nNew site submit. {0}\n\n".format(f.title))
            msg += emailmsg
            send_mail("{0} | New web site".format(WEBSITE_NAME), msg, DEFAULT_FROM_EMAIL, TO, True)

            msg_ok = u'Submit site successful.'
        else:
            msg_err = u'Attention! Please correct the mistake!'

    return render(request, "site_add.html", locals())

@login_required(login_url=LOGIN_URL)
@csrf_exempt
def site_update(request, slug):
    """
    :param request:
    :param slug:
    :return:
    """
    val = get_object_or_404(Site, slug=slug)

    form = SiteForm(request.POST or None, instance=val)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            msg_ok = (u'Site update successful.')
        else:
            msg_err = (u'Attention! Please correct the mistake!')

    return render(request, "site_add.html", locals())

def about(request):
    """
    About
    """
    framework_list = []
    for i in FRAMEWORK:
        framework_list.append(i[0])

    operating_system_list = []
    for i in OS:
        operating_system_list.append(i[0])

    webserver_list = []
    for i in WEBSERVERS:
        webserver_list.append(i[0])

    database_list = []
    for i in DATABASES:
        database_list.append(i[0])

    method_list = []
    for i in METHOD:
        method_list.append(i[0])

    python_version_list = []
    for i in PYTHONVERSIONS:
        python_version_list.append(i[0])

    return render (request, "about.html", locals())

def statistics(request):
    """
    Statistics
    """

    return render (request, "statistics.html", locals())

def statistic_language(request):
    """
    Statistics
    """
    from chartit import DataPool, Chart, PivotDataPool, PivotChart
    from django.db.models import F, FloatField, Sum
    from django.db.models import Count
    import datetime

    sites = Site.objects.filter(enable=True)

    ds = PivotDataPool(
        series=[
            {'options': {
                'source': sites,
                'categories': 'language'},
                'terms': {
                    'python': Count('pk')}}])

    language_chart = PivotChart(
        datasource=ds,
        series_options=[
            {'options': {
                'type': 'column'},
                'terms': ['python']}],

        chart_options={
            'title': {
                'text': 'Python : Language'
            },
            'xAxis': {
                'title': {
                    'text': 'Python2Sites : %s' % datetime.datetime.now()
                }
            },
            'yAxis': {
                'title': {
                    'text': 'Value'}
            },
            'legend': {
                'enabled': True},
            'credits': {
                'enabled': False}
        },)

    return render (request, "statistic_language.html", locals())

def statistic_framework(request):
    """
    Statistics
    """
    from chartit import DataPool, Chart, PivotDataPool, PivotChart
    from django.db.models import F, FloatField, Sum
    from django.db.models import Count
    import datetime

    sites = Site.objects.filter(enable=True)

    ds = PivotDataPool(
        series=[
            {'options': {
                'source': sites,
                'categories': 'framework'},
                'terms': {
                    'python': Count('pk')}}])

    framework_chart = PivotChart(
        datasource=ds,
        series_options=[
            {'options': {
                'type': 'column'},
                'terms': ['python']}],

        chart_options={
            'title': {
                'text': 'Python : Framework'
            },
            'xAxis': {
                'title': {
                    'text': 'Python2Sites : %s' % datetime.datetime.now()
                }
            },
            'yAxis': {
                'title': {
                    'text': 'Value'}
            },
            'legend': {
                'enabled': True},
            'credits': {
                'enabled': False}
        },)

    return render (request, "statistic_framework.html", locals())

def statistic_operating_system(request):
    """
    Statistics
    """
    from chartit import DataPool, Chart, PivotDataPool, PivotChart
    from django.db.models import F, FloatField, Sum
    from django.db.models import Count
    import datetime

    sites = Site.objects.filter(enable=True)

    ds = PivotDataPool(
        series=[
            {'options': {
                'source': sites,
                'categories': 'operating_system'},
                'terms': {
                    'python': Count('pk')}}])

    operating_system_chart = PivotChart(
        datasource=ds,
        series_options=[
            {'options': {
                'type': 'column'},
                'terms': ['python']}],

        chart_options={
            'title': {
                'text': 'Python : Operating System'
            },
            'xAxis': {
                'title': {
                    'text': 'Python2Sites : %s' % datetime.datetime.now()
                }
            },
            'yAxis': {
                'title': {
                    'text': 'Value'}
            },
            'legend': {
                'enabled': True},
            'credits': {
                'enabled': False}
        },)

    return render (request, "statistic_operating_system.html", locals())

def statistic_webserver(request):
    """
    Statistics
    """
    from chartit import DataPool, Chart, PivotDataPool, PivotChart
    from django.db.models import F, FloatField, Sum
    from django.db.models import Count
    import datetime

    sites = Site.objects.filter(enable=True)

    ds = PivotDataPool(
        series=[
            {'options': {
                'source': sites,
                'categories': 'webserver'},
                'terms': {
                    'python': Count('pk')}}])

    webserver_chart = PivotChart(
        datasource=ds,
        series_options=[
            {'options': {
                'type': 'column'},
                'terms': ['python']}],

        chart_options={
            'title': {
                'text': 'Python : Webserver'
            },
            'xAxis': {
                'title': {
                    'text': 'Python2Sites : %s' % datetime.datetime.now()
                }
            },
            'yAxis': {
                'title': {
                    'text': 'Value'}
            },
            'legend': {
                'enabled': True},
            'credits': {
                'enabled': False}
        },)

    return render (request, "statistic_webserver.html", locals())

def statistic_database(request):
    """
    Statistics
    """
    from chartit import DataPool, Chart, PivotDataPool, PivotChart
    from django.db.models import F, FloatField, Sum
    from django.db.models import Count
    import datetime

    sites = Site.objects.filter(enable=True)

    ds = PivotDataPool(
        series=[
            {'options': {
                'source': sites,
                'categories': 'database'},
                'terms': {
                    'python': Count('pk')}}])

    database_chart = PivotChart(
        datasource=ds,
        series_options=[
            {'options': {
                'type': 'column'},
                'terms': ['python']}],

        chart_options={
            'title': {
                'text': 'Python : Database'
            },
            'xAxis': {
                'title': {
                    'text': 'Python2Sites : %s' % datetime.datetime.now()
                }
            },
            'yAxis': {
                'title': {
                    'text': 'Value'}
            },
            'legend': {
                'enabled': True},
            'credits': {
                'enabled': False}
        },)

    return render (request, "statistic_database.html", locals())

def statistic_method(request):
    """
    Statistics
    """
    from chartit import DataPool, Chart, PivotDataPool, PivotChart
    from django.db.models import F, FloatField, Sum
    from django.db.models import Count
    import datetime

    sites = Site.objects.filter(enable=True)

    ds = PivotDataPool(
        series=[
            {'options': {
                'source': sites,
                'categories': 'method'},
                'terms': {
                    'python': Count('pk')}}])

    method_chart = PivotChart(
        datasource=ds,
        series_options=[
            {'options': {
                'type': 'column'},
                'terms': ['python']}],

        chart_options={
            'title': {
                'text': 'Python : Method'
            },
            'xAxis': {
                'title': {
                    'text': 'Python2Sites : %s' % datetime.datetime.now()
                }
            },
            'yAxis': {
                'title': {
                    'text': 'Value'}
            },
            'legend': {
                'enabled': True},
            'credits': {
                'enabled': False}
        },)

    return render (request, "statistic_method.html", locals())

def statistic_python_version(request):
    """
    Statistics
    """
    from chartit import DataPool, Chart, PivotDataPool, PivotChart
    from django.db.models import F, FloatField, Sum
    from django.db.models import Count
    import datetime

    sites = Site.objects.filter(enable=True)

    ds = PivotDataPool(
        series=[
            {'options': {
                'source': sites,
                'categories': 'python_version'},
                'terms': {
                    'python': Count('pk')}}])

    python_version_chart = PivotChart(
        datasource=ds,
        series_options=[
            {'options': {
                'type': 'column'},
                'terms': ['python']}],

        chart_options={
            'title': {
                'text': 'Python : Python Version'
            },
            'xAxis': {
                'title': {
                    'text': 'Python2Sites : %s' % datetime.datetime.now()
                }
            },
            'yAxis': {
                'title': {
                    'text': 'Value'}
            },
            'legend': {
                'enabled': True},
            'credits': {
                'enabled': False}
        },)

    return render (request, "statistic_python_version.html", locals())
















