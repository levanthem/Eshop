from django.contrib.auth import views as auth_views
from django.urls import path,include
from . import views
from .views import Cart1, CheckOut, OrderView,Test, Cart, signup, Login,logout
from .middlewares.auth import  auth_middleware
urlpatterns = [
    path('',views.index,name ="index"),
    path('signup/', signup.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout , name='logout'),
    path('contact/',views.contact,name='contact'),
    path('shop/',views.shop,name='shop'),
    # path('cart1/',views.Cart.cart1,name='cart1'),
    path('cart/',Cart.as_view(),name='cart'),
    path('cart1/',Cart1.as_view(),name='cart1'),
    # path('cart1', auth_middleware(Cart1.as_view()) , name='cart1'),
    path('check-out/', CheckOut.as_view() , name='checkout'),
    path('orders/', OrderView.as_view() , name='orders'),
    path('test/', Test.as_view() , name='test'),
    path('payment/', views.payment , name='payment'),
    path('paymentSuccess/', views.paymentSuccess , name='paymentSuccess'),
    
   
]