from django.core.checks import messages
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from home.models import *
from user.models import *
from product.models import *
from order.models import *
from django.contrib.auth.decorators import login_required
from user.forms import *
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from product.forms import *
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm 


def register(request):
    if request.method == 'POST':
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
            data.image = 'user_images/'
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


@login_required(login_url='/userlogin/')
def profile_update(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST,instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'Sizning profilingiz muvoffaqiyatli yangilandi!')
            return HttpResponseRedirect('/profile/')
    else:
        category = Category.objects.all()
        setting = Setting.objects.all()
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
        context = {
            'category':category,
            'setting':setting,
            'user_form':user_form,
            'profile_form':profile_form,
        }
        return render(request,'user_profile.html',context)


@login_required(login_url='/userlogin/')
def profile(request):
    setting = Setting.objects.all()
    category = Category.objects.all()
    current_user = request.user 
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {
        'category':category,
        'profile':profile,
        'setting':setting,
    }
    return render(request,'profile.html',context)


@login_required(login_url='/userlogin/')
def user_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            messages.success(request,'Sizning parolingiz muvaffaqiyatli o\'zgartirildi!')
            return HttpResponseRedirect('/profile/')
        else:
            messages.error(request,form.errors)
            return HttpResponseRedirect('/password/')
    else:
        category = Category.objects.all()
        setting = Setting.objects.all()
        form = PasswordChangeForm(request.user)
        return render(request,'user_password.html',{'form':form,'category':category,'setting':setting})


@login_required(login_url='/userlogin/')
def user_comments(request):
    setting = Setting.objects.all()
    category = Category.objects.all()
    current_user = request.user
    # product_single = Product.objects.get(id=pk)
    comment = Comment.objects.filter(user_id=current_user.id)
    context = {
        'comment':comment,
        'setting':setting,
        'category':category,
    }
    return render(request,'user_comments.html',context)


@login_required(login_url='/userlogin/')
def deletecomment(request,pk):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    Comment.objects.filter(user_id=current_user.id,id=pk).delete()
    messages.success(request,'Your comment deleted successfullly!')
    return HttpResponseRedirect(url)