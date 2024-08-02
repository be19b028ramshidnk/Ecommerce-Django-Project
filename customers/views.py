from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from .models import Customer
# Create your views here.

def show_account(request):
    context ={}
    if request.POST and 'register' in request.POST: # Which means if user post a request,
        context['register'] = True
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            address = request.POST.get('address')
            phone=request.POST.get('phone')
            
            # create a user account
            user = User.objects.create_user(
                username = username,
                password = password,
                email = email
            )
            
            # create customer account
            customer = Customer.objects.create(
                name=username,
                user = user,
                phone = phone,
                address = address
            )
            success_msg ="User registered sucessfully"
            messages.success(request,success_msg)
        except Exception as e:
            messages.error(request, "Duplicate user name or invalid inputs")
   
    if request.POST and 'login' in request.POST :
        context['register'] = False
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            login(request, user)
            messages.success(request,"Login Sucessfully")
            return redirect('home')
        else:
            messages.error(request, "invalid credentials")
    return render(request, 'account.html', context)


def sign_out(request):
    logout(request)
    return redirect('home')