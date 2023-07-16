
from django.shortcuts import render, redirect
from .forms import CaseForm, CaseTypeForm, CourtForm, PoliceStationForm, ClientForm
from .models import Case, CaseType, Court, PoliceStation, Client
from datetime import date, timedelta

# Create your views here.

def cases(request):
    return render(request, 'cases/cases.html')

def casetype_setup(request):
    if request.method == 'POST':
        form = CaseTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('case-type')
    else:
        form = CaseTypeForm()

    casetypes = CaseType.objects.all()

    return render(request, 'cases/case_type.html',{'form':form, 'casetypes': casetypes})

def casetype_update(request, casetype_id):
    casetype = CaseType.objects.get(id=casetype_id)

    if request.method == 'POST':
        form = CaseTypeForm(request.POST, instance=casetype)
        if form.is_valid():
            form.save()
            return redirect('case-type')
    else:
        form = CaseTypeForm(instance=casetype)

    casetypes = CaseType.objects.all()

    return render(request, 'cases/case_type.html', {'form': form, 'casetypes': casetypes})

###############################

def court_setup(request):
    if request.method == 'POST':
        form = CourtForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courts')
    else:
        form = CourtForm()

    courts = Court.objects.all()

    return render(request, 'cases/courts.html',{'form':form, 'courts': courts})

def court_update(request, court_id):
    court = Court.objects.get(id=court_id)

    if request.method == 'POST':
        form = CourtForm(request.POST, instance=court)
        if form.is_valid():
            form.save()
            return redirect('courts')
    else:
        form = CourtForm(instance=court)

    courts = Court.objects.all()

    return render(request, 'cases/courts.html',{'form':form, 'courts': courts})

# Poice Station

def police_station_setup(request):
    if request.method == 'POST':
        form = PoliceStationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stations')
    else:
        form = PoliceStationForm()
    stations = PoliceStation.objects.all()
    return render(request, 'cases/police_stations.html',{'form':form, 'stations': stations})

def police_station_update(request, station_id):
    station = PoliceStation.objects.get(id=station_id)

    if request.method == 'POST':
        form = PoliceStationForm(request.POST, instance=station)
        if form.is_valid():
            form.save()
            return redirect('stations')
    else:
        form = PoliceStationForm(instance=station)

    stations = PoliceStation.objects.all()
    return render(request, 'cases/police_stations.html',{'form':form, 'stations': stations})



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

def todays_case_list(request):
    today = date.today()
    cases = Case.objects.filter(date=today)
    return render(request, 'cases/todays_cases.html', {'cases': cases})

# Tomorrows Cases
def tomorrows_case_list(request):
    tomorrow = date.today() + timedelta(days=1)
    cases = Case.objects.filter(date=tomorrow)
    return render(request, 'cases/tomorrows_cases.html', {'cases': cases})

def addClient(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ClientForm()
    
    return render(request, 'cases/add_client.html', {'form':form})

def client_update(request, client_id):
    client = Client.objects.get(id=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ClientForm(instance=client)
    
    return render(request, 'cases/add_client.html', {'form':form})

def getAllClients(request):
    clients = Client.objects.all()
    return render(request, 'cases/all_client.html', {'clients': clients})


# Todays Cases
# Running Cases
# Decided Cases
# Abandoned Cases
# Not updated Cases
# Todays    

