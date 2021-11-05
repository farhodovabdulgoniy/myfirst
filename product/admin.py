from django.contrib import admin
from product.models import *


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Images)
admin.site.register(Comment)