from django.shortcuts import render,redirect
from .models import Posts
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout
from . import models
# Create your views here.
def loginn(request):
    if request.method == "POST":
        name=request.POST.get("lusername")
        password=request.POST.get("lpassword")
        userr=authenticate(request,username=name,password=password)
        if userr is not None:
            auth_login(request,userr)
            return redirect('/home')
        else:
            return redirect('/login')
    return render(request,"login.html")
def register(request):
   if request.method =='POST':
       name=request.POST.get("rusername")
       email=request.POST.get("remail")
       password=request.POST.get("rpassword")
       newuser=User.objects.create_user(username=name,email=email,password=password)
       newuser.save()
       return redirect('/login')
   return  render(request,"register.html")
def home(request):
    context={
        "posts":Posts.objects.all()
    }
    return render(request,'homepage.html',context)
def logoutt(request):
    logout(request)
    return redirect('/login')
def newPost(request):
    if request.method == 'POST':
        title=request.POST.get('title')
        content=request.POST.get('content')
        npost=models.Posts(title=title,content=content,author=request.user)
        npost.save()
        return redirect('/home')
    return render(request,'newpost.html')
def myposts(request):
    context={
        'posts':Posts.objects.filter(author=request.user)
    }
    return render(request,'mypost.html',context)
def Contact(request):
    return render(request,'contact.html')