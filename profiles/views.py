"""
Profiles
"""

from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect
from django.contrib.auth.models import User, Group, Permission
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

import hashlib, random

from python2sites.settings import LOGIN_URL, emailmsg, DEFAULT_FROM_EMAIL, WEBSITE_NAME, WEBSITE_URL, TO

from .forms import LoginForm, SignupForm, ForgetPasswordForm
from .models import Profile
from .forms import ProfileForm

@csrf_exempt
def user_login(request):
    """
    Login
    """
    msg_err = ""

    auth_logout(request)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['email']
            password = form.cleaned_data['password']
            if '@' in username:
                try:
                    check = User.objects.get(email=username)
                    username = check.username
                except:
                    pass

            user = authenticate(username=username, password=password)

            if user is not None:
                profile = Profile.objects.get(user=user)
                if user.is_active:
                    login(request, user)

                    msg_ok = u"Login successful."

                    if request.POST['next']:
                        return redirect(request.POST['next'])
                    else:
                        return redirect("/")
                else:
                    salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
                    email = user.email
                    if isinstance(email, str):
                        email = email.encode('utf-8')
                    profile = Profile.objects.get(user=user)
                    profile.activation_key = hashlib.sha1(salt + email).hexdigest()
                    profile.save()

                    msg = (u"Hi {0};\n\nHello, Python lovers!\nPlease confirm your email address.\n\nLogin to {1}, could you kindly just confirm your email address by clicking on the link below :\n{2}/user/activation/{3}/\n\n".format(user.username, WEBSITE_NAME, WEBSITE_URL, profile.activation_key))
                    msg += emailmsg
                    send_mail(u"{0} | Please confirm".format(WEBSITE_NAME), msg, DEFAULT_FROM_EMAIL, [email], True)
                    msg_ok = u"Please confirm your email address."

                    return render(request, 'message.html', locals())
            else:
                msg_err = (u"Invalid password or account does not exists.")

                return render(request, 'login.html', locals())
        else:
            msg_err = (u"Please fill out this field.")
    else:
        form = LoginForm()

    return render(request, 'login.html', locals())

@csrf_exempt
def user_signup(request):
    """
    Register
    """
    auth_logout(request)
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.get(email=form.cleaned_data['email'])
                msg_err = u"This email is already in use."

                return render(request, 'signup.html', {'msg_err': msg_err})

            except:
                user = User.objects.create_user(
                    request.POST['username'],
                    request.POST['email'],
                    request.POST['password']
                )
                user.first_name = request.POST['username']
                user.last_name = request.POST['username']
                user.is_active=False
                user.save()

                # group = Group.objects.get(name='user')
                # user.groups.add(group)

                profile = Profile()
                profile.user = user
                salt = hashlib.sha1(str(random.random()).encode()).hexdigest()[:5]
                email = user.email
                if isinstance(email, str):
                    email = email.encode('utf-8')

                profile.activation_key = hashlib.sha1(str(salt).encode() + email).hexdigest()
                profile.save()

                # admin
                msg = (u"Hi admin;\n\nNew user registration.{0}\n\n".format(user.username))
                msg += emailmsg
                send_mail("{0} | New user".format(WEBSITE_NAME), msg, DEFAULT_FROM_EMAIL, TO, True)

                # user
                msg = (
                u"Hi {0};\n\nHello, Python lovers!\nPlease confirm your email address.\n\nLogin to {1}, could you kindly just confirm your email address by clicking on the link below :\n{2}/user/activation/{3}/\n\n".format(
                    user.username, WEBSITE_NAME, WEBSITE_URL, profile.activation_key))
                msg += emailmsg
                send_mail("{0} | Please confirm".format(WEBSITE_NAME), msg, DEFAULT_FROM_EMAIL, [email], True)

                msg_ok = u"Please confirm your email address."

                return render(request, 'message.html', locals())
        else:
            msg_err = (u"Please fill out this field.")

    else:
        form = SignupForm()

    return render(request, 'signup.html', locals())

@login_required(login_url = LOGIN_URL)
def user_logout(request):
    """
    Logout
    """
    auth_logout(request)

    return redirect('/')

@csrf_exempt
def user_forget_password(request):
    """
    Forget password
    """
    if request.method == 'POST':
        form = ForgetPasswordForm(request.POST)
        if form.is_valid():
            try:
                user = Profile.objects.get(email = request.POST['email'])
                password = Profile.objects.make_random_password()
                user.set_password(password)
                user.save()
                msg = (u"Hi {0}\nForgot password link is clicked.\nNew password is : {1}".format (user.first_name, password))
                msg += emailmsg
                send_mail(u"New password", msg, DEFAULT_FROM_EMAIL, [user.email], True)
                msg_ok = ("New password send is email address.".format(user.email))

                return render(request, 'message.html', {'msg_ok': msg_ok})

            except:
                msg_err = (u"Invalid password or account does not exists.")

                return render(request, 'message.html', {'msg_err': msg_err})
        else:
            msg_err = u"Invalid form."
    else:
        form = ForgetPasswordForm()

    return render(request, 'forget_password.html', locals())

@login_required(login_url=LOGIN_URL)
@csrf_exempt
def profile(request):
    """
    :param request:
    :param:
    :return:
    """
    val = get_object_or_404(Profile, user=request.user)

    form = ProfileForm(request.POST or None, instance=val)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            msg_ok = (u'Profile updated')
        else:
            msg_err = u"Invalid form."

    return render(request, "profile.html", locals())

def user_activation(request, key):
    """
    """
    profile = get_object_or_404(Profile, activation_key=key)
    user = User.objects.get(username=profile)
    user.is_active = True
    user.save()

    user.backend = 'django.contrib.auth.backends.ModelBackend'
    login(request, user)

    msg_ok = u"Thanks... User account is enabled..."

    return render(request, 'message.html', locals())
