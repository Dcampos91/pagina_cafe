from rest_framework import serializers
from .models import Cafe

class CafeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cafe
        fields = ['nombre_cafe','valor','tamaño']
