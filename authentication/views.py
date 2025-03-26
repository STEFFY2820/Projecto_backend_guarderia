from rest_framework import status,generics
from .models import *
from .serializers import *
from rest_framework.response import Response
from django.http import Http404
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.views import TokenObtainPairView

class RoleListViews(generics.ListAPIView):
    queryset = RoleModel.objects.all()
    serializer_class = RoleSerializer

    def list(self, request, *args, **kwargs):
       response = super().list(request, *args, **kwargs)

       return Response({
           'object': 'list_roles',
              'data': response.data
       },status=status.HTTP_200_OK)
    
class RolesCreateView(generics.CreateAPIView):
    serializer_class = RoleSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        return Response({
            'object': 'create_roles',
            'data': response.data
        }, status=status.HTTP_201_CREATED)
    
class RolesUpdateView(generics.UpdateAPIView):
    queryset = RoleModel.objects.all()
    serializer_class = RoleSerializer

    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)
            
            return Response({
                'object': 'update_roles',
                'data': response.data
            }, status=status.HTTP_200_OK)
        
        except Http404:
            return Response({
                'object': 'update_roles',
                'data': 'role not found'
            }, status=status.HTTP_400_BAD_REQUEST)
        
class RolesDestroyView(generics.DestroyAPIView):
    queryset = RoleModel.objects.all()

    def destroy(self, request, *args, **kwargs):
        try:
            super().destroy(request)
            
            return Response({
                'object': 'destroy_roles',
            }, status=status.HTTP_204_NO_CONTENT)
        
        except Http404:
            return Response({
                'object': 'destroy_roles',
                'data': 'role not found'
            }, status=status.HTTP_400_BAD_REQUEST)
        
class RolesRetrieveView(generics.RetrieveAPIView):
    queryset = RoleModel.objects.all()
    serializer_class = RoleSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            response = super().retrieve(request, *args, **kwargs)
            
            return Response({
                'object': 'retrieve_roles',
                'data': response.data
            }, status=status.HTTP_200_OK)
        
        except Http404:
            return Response({
                'object': 'retrieve_roles',
                'data': 'role not found'
            }, status=status.HTTP_400_BAD_REQUEST)
        
class AuthRegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request):
        response = super().create(request)

        return Response({
            'object': 'create_user',
            'data': response.data
        }, status=status.HTTP_201_CREATED)
    

class AuthLoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request):
        try:
            return super().post(request)
        except ValidationError as e:
            return Response({
                'object': 'login_user',
                'error': 'Invalid credentials'
            }, status=status.HTTP_400_BAD_REQUEST)

