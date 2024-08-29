# forms.py
from django import forms
from .models import Titanic


class TitanicForm(forms.ModelForm):
    SEX_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    
    EMBARKED_CHOICES = [
        ('C', 'Cherbourg'),
        ('Q', 'Queenstown'),
        ('S', 'Southampton'),
    ]

    sex = forms.ChoiceField(choices=SEX_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    embarked = forms.ChoiceField(choices=EMBARKED_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Titanic
        fields = '__all__'
        widgets = {
            'passenger_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'pclass': forms.NumberInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'sibsp': forms.NumberInput(attrs={'class': 'form-control'}),
            'parch': forms.NumberInput(attrs={'class': 'form-control'}),
            'ticket': forms.TextInput(attrs={'class': 'form-control'}),
            'fare': forms.NumberInput(attrs={'class': 'form-control'}),
            'cabin': forms.TextInput(attrs={'class': 'form-control'}),
            'survived': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class ExcelUploadForm(forms.Form):
    excel_file = forms.FileField(label="Upload Excel File")
