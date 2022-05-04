from django.shortcuts import render,redirect
from . import forms 
from django.contrib.auth.models import User 
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    
    form = forms.RegisterForm(request.POST or None)
    if form.is_valid(): # clean methodu çağrılacak
             username = form.cleaned_data.get("username")
             password = form.cleaned_data.get("password")
             newUser = User(username = username)
             newUser.set_password(password)
             newUser.save()
             auth.login(request,newUser)
             messages.success(request,"Başarılı..")
             return redirect("index")
    else:
        context = {
             "form":form
        }
        return render(request,"register.html",context)
    # if request.method == "POST":
    #     form = forms.RegisterForm(request.POST)
    #     if form.is_valid(): # clean methodu çağrılacak
    #         username = form.cleaned_data.get("username")
    #         password = form.cleaned_data.get("password")
    #         newUser = User(username = username)
    #         newUser.set_password(password)
    #         newUser.save()
    #         auth.login(request,newUser)
    #         return redirect("index")
    #     context = {
    #         "form":form
    #     }
    #     return render(request,"register.html",context)
    # else:
    #     form = forms.RegisterForm()
    #     context = {
    #         "form":form
    #     }
    #     return render(request,"register.html",context)
    
    
def login(request):
    form = forms.LoginForm(request.POST or None)
    context =  {
        "form":form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = auth.authenticate(request,username=username,password=password)
        if user is None:
            messages.info(request)
            return render(request,"login.html",context)
        messages.success(request,"Başarılı Giriş")
        auth.login(request,user)
        return redirect("index")
    return render(request,"login.html",context)
@login_required(login_url="user:login")
def logout(request):
    auth.logout(request)
    messages.success(request,"Başarılı...")
    return redirect("index")

 