
from django.shortcuts import render, redirect
from .forms import CaseForm
from .models import Case

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

def getAllCases(request):
    cases = Case.objects.all()
    return render(request, 'cases/all_cases.html', {'cases': cases})

# All Cases
# Running Cases
# Todays Cases
# Tomorrows Cases
# Decided Cases
# Abandoned Cases
# Not updated Cases
# Todays    

