from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from product.forms import CommentForm
from product.models import *
from django.http import HttpResponseRedirect
from django.contrib import messages


@login_required(login_url='/addacomment/')
def addareview(request,pk):
    url = request.META.get('HTTP_REFERER')
    product = Product.objects.get(id=pk)
    comments = Comment.objects.filter(product_id=pk,status='True').order_by('-id')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = Comment()
            data.subject = form.cleaned_data.get('subject')
            data.comment = form.cleaned_data.get('comment')
            data.rate = form.cleaned_data.get('rate')
            data.ip = request.META.get('REMOTE_ADDR')
            data.product = product
            current_user = request.user
            data.user_id = current_user.id
            data.save()
            messages.success(request,'Your review has been sent!')
    context = {
        'product_single':product,
        'comments':comments,
    }
    return render(request,'product_single.html',context)