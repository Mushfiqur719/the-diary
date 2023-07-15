from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('registration/',views.registration, name="registration"),
    path('home/',views.dashboard,name='dashboard'),
    path('login/',views.login_view,name='login_user'),
    path('logout/',views.logout_user,name='logout_user'),
]
