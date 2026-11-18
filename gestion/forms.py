from django import forms
from .models import Maquinaria


class MaquinariaForm(forms.ModelForm):
    class Meta:
        model = Maquinaria
        fields = ['nombre', 'patente_serie', 'tipo', 'anio_fabricacion', 'horas_uso', 'operativa', 'observaciones']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Tractor John Deere 5075E'}),
            'patente_serie': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: ABCD-12'}),
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'anio_fabricacion': forms.NumberInput(attrs={'class': 'form-control', 'min': 1970, 'max': 2026}),
            'horas_uso': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'min': 0}),
            'operativa': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }