from rest_framework import generics,status
from rest_framework.response import Response
from .models import MatriculaModel, PagosModel
from .serializers import MatriculaSerializer, PagosSerializer
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from django.db import transaction
import requests
import os
import datetime

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
    
class PagosCreateView(APIView):
    def post(self, request,*args,**kwargs):
        try:
            id_matricula = kwargs.get('id_matricula')

            matricula = MatriculaModel.objects.filter(id_matricula=id_matricula).first()

            if not matricula:
                raise Exception('Matricula no encontrada')
            

            servicios = [
                {
                'price':matricula.id_servicio.precio,
                'quantity':1,
                'total':matricula.id_servicio.precio,
            }
            ]

            items = []
            for servicio in servicios:
                precio_servicio = servicio['price']
                cantidad = servicio['quantity']
                total = precio_servicio* cantidad
                valor_unitario = precio_servicio / 1.18
                subtotal = total / 1.18        
                igv = total - subtotal

                item = {
                    'unidad_de_medida':'ZZ',
                    'codigo':'S-001',
                    'descripcion':'Matricula',
                    'cantidad':1,
                    'valor_unitario':valor_unitario,
                    'precio_unitario': precio_servicio,
                    'descuento':'0',
                    'subtotal':subtotal,
                    'tipo_de_igv':1,
                    'igv':igv,
                    'total':total,
                    'anticipo_regularizacion':False,
                }

                items.append(item)

            total = matricula.id_servicio.precio
            subtotal = total / 1.18
            igv = total - subtotal

            invoice_data = {
                'operacion':'generar_comprobante',
                'tipo_de_comprobante':2,
                'serie':'BBB1',
                'numero':1,
                'sunat_transaction':1,    
                'cliente_tipo_de_documento':1,
                'cliente_numero_de_documento':matricula.id_alumno.dni,
                'cliente_denominacion':matricula.id_alumno.nombres,
                'cliente_direccion':matricula.id_alumno.direccion,
                'cliente_email':matricula.user.email,
                'fecha_de_emision':datetime.datetime.now().strftime('%d-%m-%Y'),
                'moneda':1,
                'porcentaje_de_igv':18.0,
                'total_gravada':subtotal,
                'total_igv':igv,
                'total':total,
                'enviar_automaticamente_a_la_sunat':True,
                'enviar_automaticamente_al_cliente':True,
                'items':items,

            }

            response = requests.post(
                url = 'https://api.nubefact.com/api/v1/bcdd0d49-5f12-42af-ac80-dde40d656993',
                headers={
                    'Content-Type':'application/json',
                    'Authorization': f'Bearer {os.getenv("NF_API_KEY")}'
                }, json=invoice_data                     
                )

            response_json = response.json()
            response_status=response.status_code

            if response_status != 200:
                raise Exception(response_json['errors'])
            
            pagos =  PagosModel.objects.create(
                id_matricula=matricula,
                monto=matricula.id_servicio.precio,
                metodo_pago='EFECTIVO',
                mes_correspondiente='ENERO',
                fecha_pago=matricula.fecha_matricula,
                observacion='Pago de matricula'
            )

            pagos.save()

            return Response({
                'object':'invoice',
                'data':response_json
            },status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                'object':'created_pago',
                'data':str(e)
            },status=status.HTTP_400_BAD_REQUEST)
        
