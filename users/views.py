from django.shortcuts import render, redirect
from django.contrib.auth import login,logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserForm, UserLoginForm

# Create your views here.

@login_required(login_url='login/')
def home(request):
    return render(request,'home.html')

def registration(request):
    if request.user.is_authenticated:
        return redirect('home')
    context={}
    
    if request.method=="POST":
        form=CustomUserForm(request.POST)
        if form.is_valid():
            user= form.save()
            return redirect('home')
        context['register_form']=form
    else:
        form= CustomUserForm()
        context['register_form']=form
        
    return render(request,'registration/sign_up.html',context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home') 

    context={}
    if request.method=="POST":
        form= UserLoginForm(request.POST)
        if form.is_valid():
            email=request.POST['email']
            password=request.POST['password']
            user=authenticate(request,email=email,password=password)
            
            if user is not None:
                login(request,user)
                return redirect('home')
    else:
        form=UserLoginForm()
        context['login_form']=form
    return render(request,'registration/login.html',context)

def logout_user(request):
    logout(request)
    return redirect('login')