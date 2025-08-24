from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .models import Blog
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,"app/home.html")


def register(request):
    if request.method=="POST":
        data=request.POST
        username=data['username']
        password=data['password']
        if User.objects.filter(username=username).exists():
            messages.error(request,'username is already exists')
            return redirect('login')
        user=User(username=username)
        user.set_password(password)
        user.save()
        return redirect("register")
        
    return render(request,"app/register.html")


def LOGIN(request):
    if request.method=="POST":
        data=request.POST
        username=data['username']
        password=data['password']
        
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("blog")
        else:
            messages.success(request,"गलत पासवर्ड वा प्रयोगकर्ता नाम")
            return redirect('login')
    return render(request,"app/login.html")

def blog(request):
    data=Blog.objects.all()
    return render(request,"app/blog.html",{
        "data":data
    })

@login_required
def create(request):
    if request.method=="POST":
        data=request.POST
        image=request.FILES.get('image')
        title=data['title']
        subtitle=data['subtitle']
        description=data['description']
        bl=Blog(image=image,title=title,subtitle=subtitle,description=description,author_id=request.user)
        bl.full_clean()
        bl.save()
        return redirect("blog")
    return render(request,"app/create.html")


def cont(request,id):
    obj1=Blog.objects.get(id=id)
    return render(request,"app/continue.html",{
        "data":obj1
    }) 

@login_required
def delete_blog(request,id):
  blog=Blog.objects.get(id=id)
  if blog.author_id==request.user:
    blog.delete()
    return HttpResponse("successfully deleted")
  else:
    return redirect("blog")



def edit_blog(reqeust,id):
    blog=Blog.objects.get(id=id)
    if reqeust.method=="POST":
        blog=Blog.objects.get(id=id)
        blog.image=reqeust.FILES.get("image")
        blog.title=reqeust.POST['title']
        blog.subtitle=reqeust.POST['subtitle']
        blog.description=reqeust.POST['description']
        blog.save()
        return redirect("blog")

    return render(reqeust,"app/edit.html",{
        "blog":blog
    })


