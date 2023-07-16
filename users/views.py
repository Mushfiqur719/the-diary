from django.shortcuts import render, redirect
from django.contrib.auth import login,logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserForm, UserLoginForm
from cases.models import Case
from datetime import date, timedelta 

# Create your views here.
def index(request):
    return render(request,'index.html')


@login_required()
def dashboard(request):
    all_cases = Case.objects.count()
    running_cases = Case.objects.filter(status='Running').count()
    todays_cases = Case.objects.filter(date=date.today()).count()
    tomorrows_cases = Case.objects.filter(date=date.today() + timedelta(days=1)).count()
    not_updated_cases = Case.objects.filter(updated=False).count()
    decided_cases = Case.objects.filter(status='Decided').count()
    abandoned_cases = Case.objects.filter(status='Abandoned').count()

    context = {
        'all_cases': all_cases,
        'running_cases':running_cases,
        'todays_cases' : todays_cases,
        'tomorrows_cases' : tomorrows_cases,
        'not_updated_cases':not_updated_cases,
        'decided_cases':decided_cases,
        'abandoned_cases':abandoned_cases,
    }
    return render(request,'dashboard/index.html',context)

def registration(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    context={}
    
    if request.method=="POST":
        form=CustomUserForm(request.POST)
        if form.is_valid():
            user= form.save()
            return redirect('dashboard')
        context['register_form']=form
    else:
        form= CustomUserForm()
        context['register_form']=form
        
    return render(request,'registration/sign_up.html',context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard') 

    context={}
    if request.method=="POST":
        form= UserLoginForm(request.POST)
        if form.is_valid():
            email=request.POST['email']
            password=request.POST['password']
            user=authenticate(request,email=email,password=password)
            
            if user is not None:
                login(request,user)
                return redirect('dashboard')
            
    else:
        form=UserLoginForm()
        context['login_form']=form
    return render(request,'registration/login.html',context)

def logout_user(request):
    logout(request)
    return redirect('login_user')