from django.urls import path

from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('create/',views.createCase, name='create-case'),
    path('all-cases/',views.getAllCases,name='all-cases'),
    path('today-cases/',views.getAllCases,name='today-cases'),
    path('tomorrow-cases/',views.getAllCases,name='tomorrow-cases'),
]