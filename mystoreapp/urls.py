from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('index', views.index,name='index'),
    path('blog',views.blog,name='blog'),
    path('checkout',views.checkout,name='checkout'),
    path('blog-details',views.blog_detail,name='blog_detail'),
    path('contact',views.contact,name='contact'),
    path('product-details',views.product_detail,name='product_detail'),    
    path('shop-cart',views.shop_cart,name='shop_cart'),
    path('shop/<str:category_name>',views.shop,name='shop'),
    path('register', views.register,name='register'),
    path('submit_register', views.submit_register),
    path('submit_login',views.submit_login),
    path('login', views.login,name='login'),
    path('logout', views.logout, name='logout'),
    path('product/<product_name>',views.product,name='product'),
    path('mail',views.mail),
]
