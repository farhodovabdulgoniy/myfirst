"""myshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from home import views 
from product import views as ProductViews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor',include('ckeditor_uploader.urls')),
    path('',views.index,name='index'),
    path('product-detail/<int:pk>/',views.product_detail,name='product_detail'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('addacomment/<int:pk>/',ProductViews.addacomment,name='addacomment'),
    path('register/',views.register,name='register'),
    path('userlogout/',views.userlogout,name='userlogout'),
    path('userlogin/',views.userlogin,name='userlogin'),
    path('category-products/<int:pk>/<slug:slug>/',views.category_products,name='category_products'),
    path('all-products/',views.all_products,name='all_products'),
    path('post/',views.post,name='post'),
    path('lic/',views.lic,name='lic'),
    path('contact/',views.contact,name='contact'),
    path('post-detail/<int:pk>/',views.post_detail,name='post_detail'),
    path('lic-detail/<int:pk>/',views.lic_detail,name='lic_detail'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)