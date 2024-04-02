from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from shop.models import Category,Product

# Create your views here.

#categories

def allcategories(request):

    s=Category.objects.all()
    return render(request,"category.html",{'s':s})

def allproducts(request,n):
    c=Category.objects.get(id=n)
    p=Product.objects.filter(category=c)
    return render(request,"product.html",{'c':c,'p':p})

def showdetail(request,n):
    p=Product.objects.get(id=n)
    return render(request,"detail.html",{'p':p})


def register(request):
    if (request.method == 'POST'):

        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        email = request.POST['email']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']



        if (cpassword == password):
            s = User.objects.create_user(username=username, password=password, first_name=first_name,last_name=last_name, email=email)
            s.save()
            return redirect('shop:login')
        else:
            return HttpResponse("Password Does Not Match")

    return render(request, "register.html")


# def register(request):
#     if (request.method == 'POST'):
#
#         username = request.POST['username']
#         password = request.POST['password']
#         cpassword = request.POST['cpassword']
#         email = request.POST['email']
#         first_name = request.POST['firstname']
#         last_name = request.POST['lastname']
#
#
#
#         if (cpassword == password):
#             if User.objects.filter(username=username).exists():
#                 messages.info(request,"User name is already taiken")
#                 return redirect('shop:register')
#             elif User.objects.filter(email=email).exists():
#                 HttpResponse(request,"email is already taiken")
#                 return redirect('shop:register')
#             else:
#                 s = User.objects.create_user(username=username, password=password, first_name=first_name,last_name=last_name, email=email)
#                 s.save()
#                 return redirect('shop:login')
#         else:
#             return HttpResponse("Password Does Not Match")
#
#     return render(request, "register.html")


def login(request):
        if (request.method == 'POST'):
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request,user)
                return redirect('shop:allcat')

            else:
                return HttpResponse("sorry invalid")

        return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect('shop:login')