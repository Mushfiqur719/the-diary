from django.urls import path

from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('case-type/',views.casetype_setup, name='case-type'),
    path('case-type/<int:casetype_id>/',views.casetype_update, name='edit-case-type'),
    path('courts/',views.court_setup, name='courts'),
    path('courts/<int:court_id>/',views.court_update, name='edit-courts'),
    path('create/',views.createCase, name='create-case'),
    path('all-cases/',views.getAllCases,name='all-cases'),
    path('today-cases/',views.getAllCases,name='today-cases'),
    path('tomorrow-cases/',views.getAllCases,name='tomorrow-cases'),
]