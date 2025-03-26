from rest_framework import serializers
from .models import MatriculaModel, PagosModel

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatriculaModel
        fields = '__all__'

class PagosSerializer(serializers.ModelSerializer):
    class Meta:
        model = PagosModel
        fields = '__all__'