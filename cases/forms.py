# forms.py
from django import forms
from .models import Case, CaseType , Court, PoliceStation, Client


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
        exclude =['user']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class ClientBulkUploadForm(forms.Form):
    excel_file = forms.FileField(label="Select Excel File")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['excel_file'].required = True

    def clean_excel_file(self):
        excel_file = self.cleaned_data['excel_file']
        if not excel_file.name.endswith('.xlsx'):
            raise forms.ValidationError('Please upload a valid Excel file.')

        return excel_file