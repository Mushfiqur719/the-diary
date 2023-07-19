from django.urls import path

from . import views

urlpatterns = [
    path('entry-transaction/',views.entry_transaction, name='transaction'),
    path('statements/',views.get_statements, name='statements'),
]