from django.contrib import admin
from cart.models import Order,Account
from django.http import HttpResponse
# Register your models here.


admin.site.register(Order)
admin.site.register(Account)