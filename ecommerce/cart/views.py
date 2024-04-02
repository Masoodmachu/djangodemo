import pdb

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from shop.models import Product
from cart.models import Cart,Account,Order


# Create your views here.

@login_required
def cartview(request):
    u=request.user
    total=0
    c=Cart.objects.filter(user=u)
    for i in c:
        total=total+i.quantity*i.product.price
    return render(request,"cart.html",{'c':c,'total':total})


@login_required
def addtocart(request,p):

    p=Product.objects.get(id=p)
    u=request.user
    try:
        cart=Cart.objects.get(user=u,product=p)
        if(p.stock>0):
            cart.quantity+=1
            cart.save()
            p.stock-=1
            p.save()
    except:
        if (p.stock > 0):
            cart =Cart.objects.create(user=u,product=p,quantity=1)
            cart.save()
            p.stock-=1
            p.save()

    return cartview(request)

def removecart(request,p):
    # p=Product.objects.get(id=p)
    # u=request.user
    # if (p.stock > 0):
    #     cart=Cart.objects.get(user=u,product=p)
    #     cart.quantity-=1
    #     p.stock+=1
    #     cart.save()
    #     p.save()
    # return cartview(request)
    p=Product.objects.get(id=p)
    u=request.user
    try:
        cart=Cart.objects.get(user=u,product=p)
        if(cart.quantity>1):
            cart.quantity-=1
            cart.save()
            p.stock+=1
            p.save()
        else:
            cart.delete()
            p.stock+=1
            p.save()
    except:
            cart =Cart.objects.create(user=u,product=p,quantity=1)
            cart.save()
            p.stock-=1
            p.save()

    return cartview(request)

def cartdelete(request,p):
    p = Product.objects.get(id=p)
    u = request.user

    cart = Cart.objects.get(user=u, product=p)
    cart.delete()
    p.stock += cart.quantity
    p.save()


    return cartview(request)



def orderform(request):
    u = request.user
    c = Cart.objects.filter(user=u)

    if (request.method == 'POST'):

        phone = request.POST['phonenumber']
        address = request.POST['address']
        acc = request.POST['accountnumber']

        total = 0
        for i in c:
            total = total + i.quantity * i.product.price

        try:
            acc = Account.objects.get(acctnum=acc)
            acc.save()

            if (acc.amount >= total):
                o = Order.objects.create(user=u,product=i.product,phone=phone,address=address,no_of_items=i.quantity,order_status='paid')
                o.save()
                acc.amount = acc.amount - total
                acc.save()
                c.delete()

                msg = "orederd successfully"
                return render(request, "order.html", {'message': msg})

            else:
                msg = "Inefficient Amount"
                return render(request, "order.html", {'message': msg})
        except:
            pass

    return render(request, "orderform.html")



def orderview(request):

    u=request.user
    o=Order.objects.filter(user=u)



    return render(request,"ordeview.html",{'o':o,'u':u.username})







