
from django.shortcuts import render, redirect
from .forms import CaseForm
from .models import Case
from datetime import date, timedelta

# Create your views here.

def home(request):
    return render(request, 'cases/home.html')

def createCase(request):
    if request.method == 'POST':
        form = CaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    else:
        form = CaseForm()
    
    return render(request,'cases/create_case.html',{'form':form})

# All Cases
def getAllCases(request):
    cases = Case.objects.all()
    return render(request, 'cases/all_cases.html', {'cases': cases})

# Todays Cases
def todays_case_list(request):
    today = date.today()
    cases = Case.objects.filter(date=today)
    return render(request, 'cases/todays_cases.html', {'cases': cases})

# Tomorrows Cases
def tomorrows_case_list(request):
    tomorrow = date.today() + timedelta(days=1)
    cases = Case.objects.filter(date=tomorrow)
    return render(request, 'cases/tomorrows_cases.html', {'cases': cases})



# Running Cases


# Decided Cases
# Abandoned Cases
# Not updated Cases
# Todays    

