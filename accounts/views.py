from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . import models

# Create your views here.
class Login(View):    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

    def get(self,request):
        return render(request,"accounts/login.html")

    def post(self,request):
        usr = authenticate(request,
            username = request.POST.get("username"),
            password = request.POST.get("password")
        )
        if usr is None:
            return render(request,"accounts/login.html",{"error":"Username or Password is wrong!"})
        else:
            login(request,usr)
            return redirect(request.POST.get("next") or 'home')

class Signin(View):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

    def get(self,request):
        uform = UserCreationForm()
        return render(request,"accounts/signin.html",{"uform":uform})

    def post(self,request):
        print(request.POST)
        uform = UserCreationForm(request.POST)
        if request.POST.get('password1') != request.POST.get('password2'):
            return render(request,"accounts/signin.html",{"error":"Passwords should match!"})
        
        if uform.is_valid():
            user = uform.save(commit=True)
            prof = models.Profile(
                user = user,
                utype = request.POST.get("utype")
            )
            prof.save()

            return redirect(request.POST.get("next") or 'home')
        else:
            errors =(uform.errors)
            print(errors)
            return render(request,"accounts/signin.html",{"error":errors})


def logout_user(request):
    logout(request)
    return redirect('home')
    