from typing import Set
from django.conf import settings
from django.core.checks import messages
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from home.models import *
from user.models import *
from product.models import *
from order.models import *
from django.contrib.auth.decorators import login_required
from user.forms import *
from django.contrib.auth import authenticate,login,logout
from product.forms import *
from django.contrib import messages
from home.forms import ContactForm


def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=password)
            login(request,user)
            current_user = request.user 
            data = UserProfile()
            data.user_id = current_user.id 
            data.image = "user_images/user.png"
            data.save()
            return HttpResponseRedirect('/')
        else:
            messages.warning(request,form.errors)
            return HttpResponseRedirect('/register/')
    form = SignUpForm()
    category = Category.objects.all()
    setting = Setting.objects.all()
    context = {
        'category':category,
        'form':form,
        'setting':setting,
    }
    return render(request,'register.html',context)


def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            current_user = request.user
            userprofile = UserProfile.objects.get(user_id=current_user.id)
            request.session['userimage']=userprofile.image.url
            return HttpResponseRedirect('/')
        else:
            messages.warning(request,'Login error!Username or password incorrect!')
            return HttpResponseRedirect('/userlogin/')
    category = Category.objects.all()
    setting = Setting.objects.all()
    context = {
        'setting':setting,
        'category':category,
    }
    return render(request,'userlogin.html',context)


def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/')