from django.urls import path
from . import views

urlpatterns = [
    path('registration/',views.registration, name="registration"),
    path('home/',views.home,name='home'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_user,name='logout'),
]
