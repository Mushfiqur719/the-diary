# forms.py
from django import forms
from .models import Case

class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'class': 'datepicker'}),
        }
