from django.urls import path

from . import views

urlpatterns = [
    path('entry-transaction/',views.entry_transaction, name='all_transactions'),
    path('statements/',views.get_statements, name='statements'),
    path('delete-statement/<int:id>/',views.delete_transaction, name='delete_statement')
]