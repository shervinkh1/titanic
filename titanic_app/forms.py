# forms.py
from django import forms
from .models import Titanic

class TitanicForm(forms.ModelForm):
    class Meta:
        model = Titanic
        fields = '__all__'

class ExcelUploadForm(forms.Form):
    excel_file = forms.FileField(label="Upload Excel File")
