from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils.crypto import get_random_string
from home.models import Setting
from order.models import ShopCart
from product.models import Category, Product
from user.models import UserProfile
from order.forms import ShopCartForm


def index(request):
    return HttpResponse('Order Page')


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
        form = ShopCartForm(request.POST)
        if form.is_valid():
            if control == 1:  # Update shopcart
                data = ShopCart.objects.get(product_id=pk)
                data.quantity += form.cleaned_data.get('quantity')
                data.save()
            else:  # Insert to Shopcart
                data = ShopCart()
                data.user_id = current_user.id
                data.product_id = pk
                data.quantity = form.cleaned_data.get('quantity')
                data.save()
        messages.success(request, "Product added to ShopCart")
        return HttpResponseRedirect(url)
    else:  # if there is no post
        if control == 1:  # Update shopcart
            data = ShopCart.objects.get(product_id=pk)
            data.quantity += 1
            data.save()  #
        else:  # Insert to shopcart
            data = ShopCart()  # model
            data.user_id = current_user.id
            data.product_id = pk
            data.quantity = 1
            data.save()  #
        messages.success(request, "Product added to ShopCart")
        return HttpResponseRedirect(url)


@login_required(login_url='/userlogin/')
def shopcart(request):
    category = Category.objects.all()
    setting = Setting.objects.all()
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total = 0
    for i in shopcart:
        total += i.product.price * i.quantity
    # return HttpResponse(str(total))
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
    messages.success(request, "Your item deleted from Shop Cart!")
    return HttpResponseRedirect("/shopcart")


# def orderproduct(request):
#     category = Category.objects.all()
#     current_user = request.user
#     shopcart = ShopCart.objects.filter(user_id=current_user.id)
#     total = 0
#     for rs in shopcart:
#         if rs.product.variant == 'None':
#             total += rs.product.price * rs.quantity
#         else:
#             total += rs.variant.price * rs.quantity   
#     # return HttpResponse(str(total))
#     if request.method == 'POST':  # if there is a post
#         form = OrderForm(request.POST)
#         if form.is_valid():

#             data = Order()
#             data.first_name = form.cleaned_data['first_name']  # get product quantity from form
#             data.last_name = form.cleaned_data['last_name']
#             data.address = form.cleaned_data['address']
#             data.city = form.cleaned_data['city']
#             data.phone = form.cleaned_data['phone']
#             data.user_id = current_user.id
#             data.total = total
#             data.ip = request.META.get('REMOTE_ADDR')
#             ordercode = get_random_string(10).upper()  # random code
#             data.code = ordercode
#             data.save()

#             # Move Shopcart items to Order Product items
           
#             for rs in shopcart:
#                 detail = OrderProduct()
#                 detail.order_id = data.id  # Order id
#                 detail.product_id = rs.product_id
#                 detail.user_id = current_user.id
#                 detail.quantity = rs.quantity
#                 if rs.product.variant == 'None':
#                     detail.price = rs.product.price 
#                 else:
#                     detail.price = rs.variant.price 
#                 detail.variant_id = rs.variant_id
#                 detail.amount = rs.amount
#                 detail.save()
#                 if rs.product.variant == 'None':
#                     product = Product.objects.get(id=rs.product_id)
#                     product.amount -= rs.quantity
#                     product.save()
#                 else:
#                     variant = Variants.objects.get(id=rs.product_id)
#                     variant.quantity -= rs.quantity
#                     variant.save()
#                 # Reduce quantity of sold product from Amount of Product
               

#             ShopCart.objects.filter(user_id=current_user.id).delete()
#             request.session['cart_items'] = 0
#             messages.success(request, "Your Order Has Been Completed! Thank you!")
#             return render(request, 'ordercomplete.html', {'ordercode': ordercode, 'category': category})
#         else:
#             messages.warning(request, form.errors)
#             return HttpResponseRedirect("/order/orderproduct")

#     form = OrderForm
#     profile = UserProfile.objects.get(user_id=current_user.id)
#     context = {
#         'shopcart': shopcart,
#         'category': category,
#         'total': total,
#         'profile': profile,
#         'form': form,
#     }

#     return render(request, 'order_form.html', context)