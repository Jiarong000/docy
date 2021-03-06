from django.forms import ModelForm
from django import forms

from scan.models import Patient, Scan


class DateInput(forms.DateInput):
    input_type = 'date'


class PatientForm(ModelForm):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    Chemo = forms.BooleanField(required=False)
    smoker = forms.BooleanField(required=False)
    diabetes = forms.BooleanField(required=False)
    insulin = forms.BooleanField(required=False)

    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'birth_date': DateInput(),
            'Last_Chemo': DateInput()
        }


class ScanForm(ModelForm):
    file = forms.FileField(required=False)

    class Meta:
        model = Scan
        fields = ['sid','diag_date','diagnosis','reason', 'scan']
        widgets = {
            'diag_date': DateInput()
        }
