# forms.py
from django import forms
from .models import Case, CaseType , Court, PoliceStation


class CaseTypeForm(forms.ModelForm):
    class Meta:
        model = CaseType
        fields = '__all__'

class CourtForm(forms.ModelForm):
    class Meta:
        model = Court
        fields = '__all__'

class PoliceStationForm(forms.ModelForm):
    class Meta:
        model = PoliceStation
        fields = '__all__'

class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'class': 'datepicker'}),
        }