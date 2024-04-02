from django.contrib.auth.models import User
from django.db import models
from shop.models import Product


# Create your models here.

class Cart(models.Model):
     product=models.ForeignKey(Product,on_delete=models.CASCADE)
     user=models.ForeignKey(User,on_delete=models.CASCADE)
     quantity=models.IntegerField()
     date_added=models.DateTimeField(auto_now_add=True)

     def subtotal(self):
          return self.quantity*self.product.price

     def __str__(self):
         return self.product.name




class Order(models.Model):
     product=models.ForeignKey(Product,on_delete=models.CASCADE)
     user=models.ForeignKey(User,on_delete=models.CASCADE)
     no_of_items=models.IntegerField()
     phone=models.BigIntegerField()
     address=models.TextField()
     ordered_date=models.DateTimeField(auto_now_add=True)
     order_status=models.CharField(max_length=35,default='Pending')
     delivery_status=models.CharField(max_length=35,default='Pending')

     def __str__(self):
          return self.user.username


class Account(models.Model):
     acctnum=models.IntegerField()
     accttype=models.CharField(max_length=25)
     amount=models.IntegerField()

     def __str__(self):
          return str(self.acctnum)