from django import forms
from django.forms import ModelForm
from .models import Cafe

class CafeForm(ModelForm):
    class Meta:
        model = Cafe
        fields = ['nombre_cafe','valor','tamaño']
