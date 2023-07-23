
from django.shortcuts import render, redirect
from .forms import CaseForm, CaseTypeForm, CourtForm, PoliceStationForm, ClientForm
from .models import Case, CaseType, Court, PoliceStation, Client
from datetime import date, timedelta
# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas

def cases(request):
    return render(request, 'cases/cases.html')
# Case Types
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
            form.instance.user = request.user
            form.save()
            return redirect('dashboard')
    else:
        form = CaseForm()
    return render(request, 'cases/create_case.html', {'form': form})

def getAllCases(request):
    current_user = request.user
    cases = Case.objects.filter(user=current_user)
    return render(request, 'cases/all_cases.html', {'cases': cases})

def addClient(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('dashboard')
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
    current_user = request.user
    clients = Client.objects.filter(user=current_user)
    return render(request, 'cases/all_client.html', {'clients': clients})

# Todays Cases
def todays_case_list(request):
    current_user = request.user
    today = date.today()
    todays_cases = Case.objects.filter(date=today, user=current_user)
    return render(request, 'cases/todays_cases.html', {'todays_cases': todays_cases})

# Tomorrows Cases
def tomorrows_case_list(request):
    current_user = request.user
    tomorrow = date.today() + timedelta(days=1)
    tomorrows_cases = Case.objects.filter(date=tomorrow, user=current_user)
    return render(request, 'cases/tomorrows_cases.html', {'tomorrows_cases': tomorrows_cases})

# Running Cases
def running_case_list(request):
    current_user = request.user
    running_cases = Case.objects.filter(status='Running', user=current_user)
    return render(request, 'cases/running_cases.html', {'running_cases': running_cases})

# Abandoned Cases
def abandoned_case_list(request):
    current_user = request.user
    abandoned_cases = Case.objects.filter(status='Abandoned', user=current_user)
    return render(request, 'cases/abandoned_cases.html', {'abandoned_cases': abandoned_cases})

# Decided Cases
def decided_case_list(request):
    current_user = request.user
    decided_cases = Case.objects.filter(status='Decided', user=current_user)
    return render(request, 'cases/decided_cases.html', {'decided_cases': decided_cases})

# Not Updated Cases
def not_updated_case_list(request):
    current_user = request.user
    not_updated_cases = Case.objects.filter(updated=False, user=current_user)
    return render(request, 'cases/not_updated_cases.html', {'not_updated_cases': not_updated_cases})

# def generate_pdf(request):
#     from io import BytesIO

#     # Get the data from the Case model (you may need to modify this query based on your use case)
#     cases = Case.objects.all()

#     # Create a BytesIO buffer to hold the PDF
#     buffer = BytesIO()

#     # Create the PDF canvas with the buffer and set the page size to letter
#     p = canvas.Canvas(buffer, pagesize=letter)

#     # Add content to the PDF
#     p.setFont("Helvetica", 12)
#     p.drawString(100, 800, "Case List")

#     # Iterate through the cases and add the data to the PDF
#     y = 780  # Initial y position for the content
#     for case in cases:
#         p.drawString(100, y, f"Case No: {case.case_no}")
#         p.drawString(100, y - 20, f"Status: {case.status}")
#         # Add more data here if needed
#         y -= 40  # Decrement y position for the next case

#     # Save the PDF
#     p.save()

#     # Get the value of the buffer and create the HTTP response with PDF content
#     pdf_data = buffer.getvalue()
#     buffer.close()

#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="case_list.pdf"'
#     response.write(pdf_data)

#     return response



