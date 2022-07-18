from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from testapp1.views import create_view
from tkinter import messagebox

# Create your views here.
from django.template.defaulttags import csrf_token

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/member/add')
        else:
            messages.info(request,"password not matching")
            return redirect('register')

    return render(request,'login.html')
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        password1= request.POST['password1']
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"user name already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"user email already taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=first_name,email=email,last_name=last_name)
                user.save();
                print("user created")
                messages.info(request,"user created")
                return redirect("login")
        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('register')


    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')


