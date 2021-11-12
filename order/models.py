from django.db import models
from django.contrib.auth.models import User
from product.models import Product 


class ShopCart(models.Model):

    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    # quantity = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.product.title

    @property
    def price(self):
        return (self.product.price)

    # @property
    # def amount(self):
    #     return (self.quantity*self.product.price)

    
class Order(models.Model):

    STATUS = (
        ('New','Yangi'),
        ('Accepted','Qabul qilingan'),
        ('OnShipping','Yetkazib berishga'),
        ('Completed','Tugallangan'),
        ('Cancelled','Bekor qilingan'),
    )

    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    code = models.CharField(max_length=5,editable=False)
    first_name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155)
    phone = models.CharField(max_length=20,blank=True)
    address = models.CharField(blank=True,max_length=255)
    city = models.CharField(blank=True,max_length=255)
    country = models.CharField(blank=True,max_length=255)
    total = models.FloatField()
    status = models.CharField(max_length=15,choices=STATUS,default='New')
    ip = models.CharField(blank=True,max_length=25)
    adminnote = models.CharField(max_length=100,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name


class OrderProduct(models.Model):

    STATUS = (
        ('New','Yangi'),
        ('Accepted','Qabul qilingan'),
        ('Cancelled','Bekor qilingan'),
    )

    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    # quantity = models.IntegerField()
    price = models.FloatField()
    # amount = models.FloatField()
    status = models.CharField(max_length=15,choices=STATUS,default='New')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.title