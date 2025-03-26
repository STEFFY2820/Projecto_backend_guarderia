from rest_framework import generics
from rest_framework.response import Response
from .models import ServiciosModel, DocenteModel, GradosModel,AlumnoModel
from .serializers import ServiceSerializer, DocenteSerializer, GradosSerializer,AlumnoSerializer
from django.http import Http404
from rest_framework import status

class ServicesListView(generics.ListCreateAPIView):
    queryset = ServiciosModel.objects.all()
    serializer_class = ServiceSerializer

    def list(self,request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response({
            'object': 'list_services',
            'data': response.data
        }, status=status.HTTP_200_OK)

class ServicesCreateView(generics.CreateAPIView):
    serializer_class = ServiceSerializer

    def create(self,request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'object': 'create_service',
            'data': response.data
        }, status=status.HTTP_200_OK)

class ServiceUpdateView(generics.UpdateAPIView):
    queryset = ServiciosModel.objects.all()
    serializer_class = ServiceSerializer

    def update(self,request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)
            return Response({
                'object': 'update_service',
                'data': response.data
            }, status=status.HTTP_200_OK)
        except Http404:
            return Response({
                'object': 'update_service',
                'data': 'Servicio no encontrado'
            }, status=status.HTTP_400_BAD_REQUEST)

class ServiceDestroyView(generics.DestroyAPIView):
    queryset = ServiciosModel.objects.all()
    serializer_class = ServiceSerializer

    def destroy(self,request, *args, **kwargs):
        try:
            super().destroy(request, *args, **kwargs)

            return Response({
                'object': 'delete_service',
                'data': 'Servicio eliminado'
            }, status=status.HTTP_200_OK)
        except Http404:
            return Response({
                'object': 'delete_service',
                'data': 'Servicio no encontrado'
            }, status=status.HTTP_400_BAD_REQUEST)
        
class ServiceRetrieveView(generics.RetrieveAPIView):
    queryset = ServiciosModel.objects.all()
    serializer_class = ServiceSerializer

    def retrieve(self,request, *args, **kwargs):
        try:
            response = super().retrieve(request, *args, **kwargs)
            return Response({
                'object': 'retrieve_service',
                'data': response.data
            }, status=status.HTTP_200_OK)
        except Http404:
            return Response({
                'object': 'retrieve_service',
                'data': 'Servicio no encontrado'
            }, status=status.HTTP_400_BAD_REQUEST)

class DocenteListView(generics.ListCreateAPIView):
    queryset = DocenteModel.objects.all()
    serializer_class = DocenteSerializer

    def list(self,request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response({
            'object': 'list_docente',
            'data': response.data
        }, status=status.HTTP_200_OK)

class DocenteCreateView(generics.CreateAPIView):
    serializer_class = DocenteSerializer

    def create(self,request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'object': 'create_docente',
            'data': response.data
        }, status=status.HTTP_200_OK)

class DocenteUpdateView(generics.UpdateAPIView):
    queryset = DocenteModel.objects.all()
    serializer_class = DocenteSerializer

    def update(self,request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)
            return Response({
                'object': 'update_docente',
                'data': response.data
            }, status=status.HTTP_200_OK)
        except Http404:
            return Response({
                'object': 'update_docente',
                'data': 'Docente no encontrado'
            }, status=status.HTTP_400_BAD_REQUEST)

class DocenteDestroyView(generics.DestroyAPIView):
    queryset = DocenteModel.objects.all()
    #serializer_class = DocenteSerializer

    def destroy(self,request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.status = False
            instance.save()

            #serializer_class = DocenteSerializer(instance)

            return Response({
                'object': 'delete_docente',
                # 'data': serializer_class.data
            }, status=status.HTTP_200_OK)
        except Http404:
            return Response({
                'object': 'delete_docente',
                'data': 'Docente no encontrado'
            }, status=status.HTTP_400_BAD_REQUEST)
        
class DocenteRetrieveView(generics.RetrieveAPIView):
    queryset = DocenteModel.objects.all()
    serializer_class = DocenteSerializer

    def retrieve(self,request, *args, **kwargs):
        try:
            response = super().retrieve(request, *args, **kwargs)
            return Response({
                'object': 'retrieve_docente',
                'data': response.data
            }, status=status.HTTP_200_OK)
        except Http404:
            return Response({
                'object': 'retrieve_docente',
                'data': 'Docente no encontrado'
            }, status=status.HTTP_400_BAD_REQUEST)
        
class GradoListView(generics.ListCreateAPIView):
    queryset = GradosModel.objects.all()
    serializer_class = GradosSerializer

    def list(self,request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response({
            'object': 'list_grado',
            'data': response.data
        }, status=status.HTTP_200_OK)
    
class GradoCreateView(generics.CreateAPIView):
    serializer_class = GradosSerializer

    def create(self,request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'object': 'create_grado',
            'data': response.data
        }, status=status.HTTP_200_OK)
    
class GradoUpdateView(generics.UpdateAPIView):
    queryset = GradosModel.objects.all()
    serializer_class = GradosSerializer

    def update(self,request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)
            return Response({
                'object': 'update_grado',
                'data': response.data
            }, status=status.HTTP_200_OK)
        except Http404:
            return Response({
                'object': 'update_grado',
                'data': 'Grado no encontrado'
            }, status=status.HTTP_400_BAD_REQUEST)
        
class GradoDestroyView(generics.DestroyAPIView):
    queryset = GradosModel.objects.all()
    #serializer_class = GradosSerializer

    def destroy(self,request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.status = False
            instance.save()

            #serializer_class = GradosSerializer(instance)

            return Response({
                'object': 'delete_grado',
                # 'data': serializer_class.data
            }, status=status.HTTP_200_OK)
        
        except Http404:
            return Response({
                'object': 'delete_grado',
                'data': 'Grado no encontrado'
            }, status=status.HTTP_400_BAD_REQUEST)
        
class AlumnoListView(generics.ListCreateAPIView):
    queryset = AlumnoModel.objects.all()
    serializer_class = AlumnoSerializer

    # def get_queryset(self):
    #     return AlumnoModel.objects.filter(status=True)

    def list(self,request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response({
            'object': 'list_alumno',
            'data': response.data
        }, status=status.HTTP_200_OK)
    
class AlumnoPorGradoListView(generics.ListCreateAPIView):
    queryset = AlumnoModel.objects.all()
    serializer_class = AlumnoSerializer

    def get_queryset(self):
        grado = self.kwargs.get('id_grado')
        return self.queryset.filter(
            id_grado=grado,
        ).distinct()

    def list(self,request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response({
            'object': 'list_alumno_grado',
            'data': response.data
        }, status=status.HTTP_200_OK)
    
class AlumnoCreateView(generics.CreateAPIView):
    serializer_class = AlumnoSerializer

    def create(self,request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'object': 'create_alumno',
            'data': response.data
        }, status=status.HTTP_200_OK)
    
class AlumnoUpdateView(generics.UpdateAPIView):
    queryset = AlumnoModel.objects.all()
    serializer_class = AlumnoSerializer

    def update(self,request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)
            return Response({
                'object': 'update_alumno',
                'data': response.data
            }, status=status.HTTP_200_OK)
        except Http404:
            return Response({
                'object': 'update_alumno',
                'data': 'Alumno no encontrado'
            }, status=status.HTTP_400_BAD_REQUEST)
        
class AlumnoDestroyView(generics.DestroyAPIView):
    queryset = AlumnoModel.objects.all()
    
    def destroy(self,request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.status = False
            instance.save()

            #serializer_class = AlumnoSerializer(instance)

            return Response({
                'object': 'delete_alumno',
                # 'data': serializer_class.data
            }, status=status.HTTP_200_OK)
        
        except Http404:
            return Response({
                'object': 'delete_alumno',
                'data': 'Alumno no encontrado'
            }, status=status.HTTP_400_BAD_REQUEST)
        
class AlumnoRetrieveView(generics.RetrieveAPIView):
    queryset = AlumnoModel.objects.all()
    serializer_class = AlumnoSerializer

    def retrieve(self,request, *args, **kwargs):
        try:
            response = super().retrieve(request, *args, **kwargs)
            return Response({
                'object': 'retrieve_alumno',
                'data': response.data
            }, status=status.HTTP_200_OK)
        except Http404:
            return Response({
                'object': 'retrieve_alumno',
                'data': 'Alumno no encontrado'
            }, status=status.HTTP_400_BAD_REQUEST)