from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',include('cases.urls')),
    path('',include('users.urls')),
    path('admin/', admin.site.urls),
    # path('',include('django.contrib.auth.urls')),
]
