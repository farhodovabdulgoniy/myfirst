from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.crypto import get_random_string
from home.models import Setting
from order.models import ShopCart
from product.models import Category
from order.forms import OrderForm
from order.models import Order,OrderProduct
from product.models import Product
from user.models import UserProfile


@login_required(login_url='/userlogin/')
def addtoshopcart(request,pk):
    url = request.META.get('HTTP_REFERER')  # get last url
    current_user = request.user  # Access User Session information

    checkproduct = ShopCart.objects.filter(product_id=pk)  # Check product in shopcart
    if checkproduct:
        control = 1  # The product is in the cart
    else:
        control = 0  # The product is not in the cart

    if request.method == 'POST':  # if there is a post
        if control == 1:  # Update shopcart
            data = ShopCart.objects.get(product_id=pk)
            data.save()
        else:  # Insert to Shopcart
            data = ShopCart()
            data.user_id = current_user.id
            data.product_id = pk
            data.save()
        messages.success(request, "Service added to Favorites")
        return HttpResponseRedirect(url)
    else:  # if there is no post
        if control == 1:  # Update shopcart
            data = ShopCart.objects.get(product_id=pk)
            data.save()  #
        else:  # Insert to shopcart
            data = ShopCart()  # model
            data.user_id = current_user.id
            data.product_id = pk
            data.save()  #
        messages.success(request, "Service added to Favorites")
        return HttpResponseRedirect(url)


@login_required(login_url='/userlogin/')
def shopcart(request):
    category = Category.objects.all()
    setting = Setting.objects.all()
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total = 0
    for i in shopcart:
        total += i.product.price 
    context = {
        'shopcart': shopcart,
        'category': category,
        'total': total,
        'setting': setting,
        'total':total,
    }
    return render(request, 'shopcart.html', context)


@login_required(login_url='/userlogin/')  # check login
def deletefromcart(request,pk):
    ShopCart.objects.filter(id=pk).delete()
    messages.success(request, "Your item deleted from Favorites!")
    return HttpResponseRedirect("/shopcart/")


@login_required(login_url='/userlogin/')
def orderproduct(request):
    setting = Setting.objects.all()
    category = Category.objects.all()
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total = 0
    for rs in shopcart:
        total += rs.product.price 
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = Order()
            data.first_name = form.cleaned_data.get('first_name') 
            data.last_name = form.cleaned_data.get('last_name')
            data.address = form.cleaned_data.get('address')
            data.city = form.cleaned_data.get('city')
            data.phone = form.cleaned_data.get('phone')
            data.user_id = current_user.id
            data.total = total
            data.ip = request.META.get('REMOTE_ADDR')
            ordercode = get_random_string(10).upper() 
            data.code = ordercode
            data.save()

            for rs in shopcart:
                detail = OrderProduct()
                detail.order_id = data.id 
                detail.product_id = rs.product_id
                detail.user_id = current_user.id
                detail.price = rs.product.price
                detail.save()
                product = Product.objects.get(id=rs.product_id)
                product.save()               

            ShopCart.objects.filter(user_id=current_user.id).delete()
            request.session['cart_items'] = 0
            messages.success(request, "Your Order Has Been Completed! Thank you!")
            return render(request, 'ordercomplete.html', {'ordercode': ordercode, 'category': category})
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect("/orderproduct/")

    form = OrderForm
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {
        'shopcart': shopcart,
        'category': category,
        'total': total,
        'profile': profile,
        'setting': setting,
        'form': form,
    }

    return render(request, 'orderproduct.html', context)

