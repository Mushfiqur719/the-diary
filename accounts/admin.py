from django.contrib import admin
from .models import Transaction,BillInvoices,Quotations

# Register your models here.

admin.site.register(Transaction)
admin.site.register(BillInvoices)
admin.site.register(Quotations)