from rest_framework import serializers
from .models import ServiciosModel, DocenteModel,GradosModel,AlumnoModel,PadreApoderadoModel

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiciosModel
        fields = '__all__'

class DocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocenteModel
        fields = '__all__'

class GradosSerializer(serializers.ModelSerializer):
    class Meta:
        model = GradosModel
        fields = '__all__'

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlumnoModel
        fields = '__all__'

class PadreApoderadoSerializer(serializers.ModelSerializer):
    class Meta:
        model= PadreApoderadoModel
        fields='__all__'