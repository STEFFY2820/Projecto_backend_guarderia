from rest_framework import serializers, viewsets
from rest_framework.serializers import PrimaryKeyRelatedField
from .models import MatriculaModel, PagosModel
from services.serializers import (AlumnoSerializer, ServiceSerializer)
from services.models import ServiciosModel, AlumnoModel
from authentication.models import UserModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ("name","email","role")
        ref_name = 'TransactionsUserSerializer'

class MatriculaSerializer(serializers.ModelSerializer):
    # id_servicio=PrimaryKeyRelatedField(queryset=ServiciosModel.objects.all())
    # user=PrimaryKeyRelatedField(queryset=UserModel.objects.all())
    # id_alumno=PrimaryKeyRelatedField(queryset=AlumnoModel.objects.all())
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['id_servicio'] = ServiceSerializer(instance.id_servicio).data
        representation['user'] = UserSerializer(instance.user).data
        representation['id_alumno'] = AlumnoSerializer(instance.id_alumno).data
        return representation

    class Meta:
        model = MatriculaModel
        fields = ("fecha_matricula","observacion","user","id_servicio","id_alumno")
        
class PagosSerializer(serializers.ModelSerializer):
    class Meta:
        model = PagosModel
        fields = '__all__'