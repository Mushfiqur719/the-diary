from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',include('users.urls')),
    path('',include('cases.urls')),
    path('',include('accounts.urls')),
    path('admin/', admin.site.urls),
    # path('',include('django.contrib.auth.urls')),
]
