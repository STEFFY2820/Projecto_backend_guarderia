from rest_framework import generics,status
from rest_framework.response import Response
from .models import MatriculaModel, PagosModel
from .serializers import MatriculaSerializer, PagosSerializer
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView

class MatriculaListView(generics.ListCreateAPIView):
    queryset = MatriculaModel.objects.all()
    serializer_class = MatriculaSerializer

    def list(self,request,*args,**kwargs):
        response =super().list(request,*args,**kwargs)
        return Response({
            'object':'list_matricula',
            'data':response.data},
            status=status.HTTP_200_OK
        )

class MatriculaCreate(APIView):
    def post(self, request):
        data=request.data
        print(data)

        validate_data = MatriculaSerializer(data=request.data).is_valid(raise_exception=True)

        if validate_data:
            pass
        return Response({'ok': True}, status=status.HTTP_200_OK)
