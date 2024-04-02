
from django.urls import path, include
from cart import views
app_name='cart'

urlpatterns = [
    path('cart/<int:p>',views.addtocart,name="addtocart"),
    path('cartview/',views.cartview,name='cartview'),
    path('cartremove/<int:p>',views.removecart,name='removecart'),
    path('cartdelete/<int:p>',views.cartdelete,name='cartdelete'),
    path('orderform/',views.orderform,name='orderform'),
    path('orderview/',views.orderview,name='orderview'),


]
