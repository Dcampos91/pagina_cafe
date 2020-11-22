from django import forms
from django.forms import ModelForm
from .models import Cafe
from django.contrib.auth.forms import UserCreationForm

class CafeForm(ModelForm):
    class Meta:
        model = Cafe
        fields = ['nombre_cafe','valor','tamaño']

class CustomUserForm(UserCreationForm):
    pass
