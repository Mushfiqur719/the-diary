from django.urls import path

from . import views

urlpatterns = [
    path('cases/', views.cases , name='cases'),
    path('case-type/',views.casetype_setup, name='case-type'),
    path('case-type/<int:casetype_id>/',views.casetype_update, name='edit-case-type'),

    path('courts/',views.court_setup, name='courts'),
    path('courts/<int:court_id>/',views.court_update, name='edit-court'),

    path('stations/',views.police_station_setup, name='stations'),
    path('stations/<int:station_id>/',views.police_station_update, name='edit-stations'),

    path('add-client/',views.addClient, name='add-client'),
    path('update-client/<int:client_id>',views.client_update, name='update-client'),

    path('all-client/',views.getAllClients, name='all-client'),


    path('create/',views.createCase, name='create-case'),
    path('all-cases/',views.getAllCases,name='all-cases'),
    path('today-cases/',views.getAllCases,name='today-cases'),
    path('tomorrow-cases/',views.getAllCases,name='tomorrow-cases'),
]