from django.shortcuts import render, redirect
from . models import Transaction
from . forms import TransactionForm

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
