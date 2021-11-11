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
from home.forms import ContactForm,SearchForm


def index(request):
    setting = Setting.objects.all()
    category = Category.objects.all()
    product_latest = Product.objects.all().order_by('-id')[:8]
    product_picked = Product.objects.all().order_by('?')[:8]
    post = Post.objects.all().order_by('-id')[:3]
    context = {
        'setting':setting,
        'post':post,
        'category':category,
        'product_picked':product_picked,
        'product_latest':product_latest,
    }
    return render(request,'index.html',context)


def product_detail(request,pk):
    setting = Setting.objects.all()
    category = Category.objects.all()
    product_picked = Product.objects.all().order_by('?')[:8]
    product_single = Product.objects.get(id=pk)
    comments = Comment.objects.filter(product_id=pk,status='True').order_by('-id')
    context = {
            'setting':setting,
            'category':category,
            'comments':comments,
            'product_picked':product_picked,
            'product_single':product_single,

    }
    return render(request,'product_single.html',context)


def aboutus(request):
    setting = Setting.objects.all()
    category = Category.objects.all()
    product_picked = Product.objects.all().order_by('-id')[:8]
    context = {
        'setting':setting,
        'category':category,
        'product_picked':product_picked,
    }
    return render(request,'aboutus.html',context)


def category_products(request,pk,slug):
    setting = Setting.objects.all()
    category = Category.objects.all()
    product = Product.objects.filter(category_id=pk)
    context = {
        'setting':setting,
        'category':category,
        'product':product,
    }
    return render(request,'category_products.html',context)


def all_products(request):
    product = Product.objects.all().order_by('?')
    setting = Setting.objects.all()
    category = Category.objects.all()
    context = {
        'product':product,
        'setting':setting,
        'category':category,
    }
    return render(request,'all_products.html',context)


def post(request):
    post = Post.objects.all().order_by('-id')
    setting = Setting.objects.all()
    category = Category.objects.all()
    product_picked = Product.objects.all().order_by('?')[:8]
    context = {
        'setting':setting,
        'category':category,
        'post':post,
        'product_picked':product_picked,
    }
    return render(request,'post.html',context)


def post_detail(request,pk):
    setting = Setting.objects.all()
    category = Category.objects.all()
    post_single = Post.objects.get(id=pk)
    context = {
        'setting':setting,
        'category':category,
        'post_single':post_single,
    }
    return render(request,'post_detail.html',context)


def lic(request):
    lic = License.objects.all().order_by('?')
    setting = Setting.objects.all()
    category = Category.objects.all()
    product_picked = Product.objects.all().order_by('?')[:8]
    context = {
        'lic':lic,
        'setting':setting,
        'category':category,
        'product_picked':product_picked,
    }
    return render(request,'lic.html',context)


def lic_detail(request,pk):
    lic_single = License.objects.get(id=pk)
    setting = Setting.objects.all()
    category = Category.objects.all()
    product_picked = Product.objects.all().order_by('?')[:8]
    context = {
        'lic_single':lic_single,
        'setting':setting,
        'category':category,
        'product_picked':product_picked,
    }
    return render(request,'lic_detail.html',context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data.get('name')
            data.email = form.cleaned_data.get('email')
            data.subject = form.cleaned_data.get('subject')
            data.message = form.cleaned_data.get('message')
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request,'Your Message has been sent!')
            return HttpResponseRedirect('/contact/')
        else:
            messages.warning(request,'Please fill in the form correctly and carefully!')
            return HttpResponseRedirect('/contact/')

    form = ContactForm
    category = Category.objects.all()
    setting = Setting.objects.all()
    product_picked = Product.objects.all().order_by('?')[:8]
    context = {
        'form':form,
        'category':category,
        'setting':setting,
        'product_picked':product_picked,
    }
    return render(request,'contactus.html',context)


def contact_single_page(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data.get('name')
            data.email = form.cleaned_data.get('email')
            data.subject = form.cleaned_data.get('subject')
            data.message = form.cleaned_data.get('message')
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request,'Your Message has been sent!')
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)


def search(request):
    setting = Setting.objects.all()
    if request.method == 'POST': #Check post
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data.get('query') #get form input data
            catid = form.cleaned_data.get('catid')
            if catid==0:
                product = Product.objects.filter(title__icontains=query) #SELECT *FROM product WHERE title LIKE '%query%'
            else:
                product = Product.objects.filter(title__icontains=query, category_id=catid)

            category = Category.objects.all()
            context = {
                'product': product,
                'query':query,
                'category': category,
                'setting': setting,
               }
            return render(request, 'search.html', context)
    return HttpResponseRedirect('/')