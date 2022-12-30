from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import Message
def home(request):
    if request.user.is_authenticated:
        messages=Message.objects.all()
        return render(request,"home.html",{'data':messages})
    return render(request,"home.html")


def login_user(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            user=User.objects.get(username=username)
        except:
            return render(request,'home.html',{"error":"Invalid username"})
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home') 
        else:
            return render(request,'home.html',{"error":"Invalid Password"})
def logout_user(request):
    logout(request)
    return redirect('home')