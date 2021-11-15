from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from home import views 
from product import views as ProductViews
from user import views as UserViews
from order import views as OrderViews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor',include('ckeditor_uploader.urls')),
    path('',views.index,name='index'),
    path('product-detail/<int:pk>/',views.product_detail,name='product_detail'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('addareview/<int:pk>/',ProductViews.addareview,name='addareview'),
    path('register/',UserViews.register,name='register'),
    path('userlogout/',UserViews.userlogout,name='userlogout'),
    path('userlogin/',UserViews.userlogin,name='userlogin'),
    path('category-products/<int:pk>/<slug:slug>/',views.category_products,name='category_products'),
    path('all-products/',views.all_products,name='all_products'),
    path('post/',views.post,name='post'),
    path('lic/',views.lic,name='lic'),
    path('contact/',views.contact,name='contact'),
    path('contact-single-page/',views.contact_single_page,name='contact_single_page'),
    path('post-detail/<int:pk>/',views.post_detail,name='post_detail'),
    path('addtoshopcart/<int:pk>/',OrderViews.addtoshopcart,name='addtoshopcart'),
    path('lic-detail/<int:pk>/',views.lic_detail,name='lic_detail'),
    path('shopcart/',OrderViews.shopcart,name='shopcart'),
    path('deletefromcart/<int:pk>/',OrderViews.deletefromcart,name='delete_from_cart'),
    path('search/',views.search,name='search'),
    path('profile/',UserViews.profile,name='profile'),
    path('profile-update',UserViews.profile_update,name='profile_update'),
    path('password/',UserViews.user_password,name='user_password'),
    path('delete-comment/<int:pk>/',UserViews.deletecomment,name='delete_comment'),
    path('user-comments/',UserViews.user_comments,name='user_comments'),
    path('orderproduct/',OrderViews.orderproduct,name='orderproduct'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)