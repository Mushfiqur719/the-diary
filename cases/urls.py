from django.urls import path

from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('create/',views.createCase, name='create-case'),
    path('all-case/',views.getAllCases,name='all-case'),
]