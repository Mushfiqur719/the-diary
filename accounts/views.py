from django.shortcuts import render, redirect
from . models import Transaction, BillInvoices, Quotations
from . forms import TransactionForm, BillInvoicesForm, QuotationsForm

# Create your views here.

def entry_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('statements')
    else:
        form = TransactionForm()
    return render(request, 'accounts/entry_transaction.html',{'form':form})

def get_statements(request):
    statements = Transaction.objects.all()
    return render(request,'accounts/statements.html', {'statements' : statements})


def bill_invoices(request):
    bill_invoices = BillInvoices.objects.all()
    form = BillInvoicesForm()
    if request.method == 'POST':
        form=BillInvoicesForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'accounts/bill_invoices.html',{'bill_invoices':bill_invoices,'form':form})

def due_bills(request):
    due_bills = BillInvoices.objects.filter(is_paid=0)
    return render(request,'accounts/due.html',{'due_bills':due_bills})


def paid_due_bills(request,pk):
    due_bills = BillInvoices.objects.filter(is_paid=0)
    bills = BillInvoices.objects.get(pk=pk)
    bills.is_paid = True
    bills.save()
    return render(request,'accounts/due.html',{'due_bills':due_bills})

def quotations(request):
    quotations = Quotations.objects.all()
    form = QuotationsForm()
    if request.method == 'POST':
        form=QuotationsForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'accounts/quotations.html',{'quotations':quotations,'form':form})
