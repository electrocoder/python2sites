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

def user_login(request):
    """
    Login
    """
    auth_logout(request)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['email']
            password = request.POST['password']
            if '@' in username:
                try:
                    check = User.objects.get(email=username)
                    username = check.username
                except:
                    pass

            user = authenticate(username=username, password=password)

            if user is not None:
                uye = Profile.objects.get(user=user)
                if user.is_active:
                    login(request, user)

                    msg_ok = u"Giriş başarili."

                    # giristen sonra next ile gelen url ye gidiliyor.
                    # uye giris sayfasina <input type="hidden" name="next" value="{{ request.GET.next }}" />   ekle
                    if request.POST['next']:
                        return redirect(request.POST['next'])
                    else:
                        return redirect("/")
                else:
                    salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
                    email = user.email
                    if isinstance(email, unicode):
                        email = email.encode('utf-8')
                    uye = Profile.objects.get(user=user)
                    uye.aktivate_key = hashlib.sha1(salt + email).hexdigest()
                    uye.save()

                    msg = ((u"\nMerhaba ; \n") + "'%s' " + (
                        u"ismi ile üye oldunuz.") + " \n " + (
                        u"Üyeliğinizi aktif etmek icin") + " %s/user/activation/%s/ " + (
                        u"linkine tiklayiniz.") + " \n %s") % (user.username, WEBSITE_NAME, uye.activation_key, WEBSITE_NAME)
                    msg += emailmsg
                    send_mail((u"%s | " + (u"Yeni üye kayıt")) % WEBSITE_NAME, msg, DEFAULT_FROM_EMAIL, [email],
                              True)
                    msg_ok = (u"Mail ile gönderilen linke tıklayınız. Üyelik aktif değil!")
            else:
                msg_err = (u"Kullanıcı adını, email adresini ve şifreni doğru girdiğinden emin misin?")

                return render(request, 'back/login.html', locals())
        else:
            msg_err = (u"Kullanıcı adını, email adresini ve şifreni doğru girdiğinden emin misin?")

            return render(request, 'login.html', locals())
    else:
        form = LoginForm()

    return render(request, 'login.html', locals())

def user_signup(request):
    """
    Register
    """
    auth_logout(request)
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.get(email=request.POST['e_mail'])
                user = ""
                msg_err = (
                    u"Bu mail adresi zaten kullanılmaktadır. Şifrenizi bilmiyorsanız şifremi unuttum linkini kullanınız.")

                return render(request, 'signup.html', locals())

            except:
                user = User.objects.create_user(
                    request.POST['username'],
                    request.POST['email'],
                    request.POST['password']
                )
                user.first_name = request.POST['username']
                user.last_name = request.POST['username']
                user.save()

                # group = Group.objects.get(name='kullanici')
                # user.groups.add(group)

                uye = Profile()
                uye.user = user
                salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
                email = user.email

                if isinstance(email, unicode):
                    email = email.encode('utf-8')

                uye.aktivate_key = hashlib.sha1(salt + email).hexdigest()

                uye.user.groups.add(Group.objects.get(pk=1))  # free plan
                uye.save()

                # for i in request.POST.getlist('konusma_dili'):
                #     uye.konusma_dili.add(KonusmaDili.objects.get(id=i))
                # admin
                msg = ("\n'%s'  " + (u"isimli uye kayit oldu.") + "\n %s") % (user.username, WEBSITE_URL)
                msg += emailmsg
                send_mail(("%s' | " + (u"Yeni üye kayit")) % WEBSITE_NAME, msg, DEFAULT_FROM_EMAIL, TO, True)

                # user
                msg = ((u"Merhaba ;\n") + "'%s' " + (u"ismi ile uye oldunuz.") + "\n " + (
                    u"Uyeliginizi aktif etmek icin") + " %s/user/activation/%s/ " + (
                    u"linkine tiklayiniz.") + "\n %s") % (user.username, WEBSITE_URL, uye.activation_key, WEBSITE_URL)
                msg += emailmsg
                send_mail(("%s " + (u"yeni uye kayit")) % WEBSITE_URL, msg, DEFAULT_FROM_EMAIL, [email], True)

                msg_ok = (u"Tebrikler. Mail ile gelen linke tıklayarak devam edebilirsiniz.")

                return render(request, 'signup.html', locals())
        else:
            msg_err = (u"E-posta adresini ve şifreni doğru girdiğinden emin misin?")

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
                msg = (u"\n" + (u"Sayın") + " %s %s \n " + (u"Şifremi unuttum linkini kullanarak yeni şifre talep ettiniz.") + "\n" + (u"Yeni şifreniz :") + " %s\n\n %s") % (user.first_name, user.last_name, password, WEBSITE_URL)
                msg += emailmsg
                send_mail((u"Yeni şifre talebi"), msg, DEFAULT_FROM_EMAIL, [user.email], True)
                msg=""
                msg_ok = (u"%s " + (u"mail adresinize yeni şifre gönderildi.")) % user.email
                user = ""

                return render(request, 'forget_password.html', locals())

            except:
                msg_err = ((u"DİKKAT :") + " %s " + (u"mail adresi ile kayıtlı bir üyemiz yok!")) % request.POST['email']

                return render(request, 'forget_password.html', locals())
        else:
            mesaj_err = (u"Form hatalı!")

            return render(request, 'forget_password.html', locals())
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
            msg_ok = (u'Profil güncelleme başarılı')
        else:
            msg_err = (u'Dikkat! Lütfen hataları düzeltiniz!')

    return render(request, "profile.html", locals())
