from django.contrib import admin
from shop.models import Category,Product
from cart.models import Cart

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)