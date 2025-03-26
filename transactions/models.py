from django.db import models
from services.models import GradosModel,AlumnoModel,DocenteModel,ServiciosModel

class MatriculaModel(models.Model):
    id_matricula = models.AutoField(primary_key=True)
    id_alumno=models.ForeignKey('services.AlumnoModel',on_delete=models.CASCADE,db_column='id_alumno',related_name='matricula')
    id_servicio=models.ForeignKey('services.ServiciosModel',on_delete=models.CASCADE,db_column='id_servicio',related_name='matricula')
    fecha_matricula=models.DateField()
    
    STATUS = (
        ('ACTIVATE','ACTIVATE'),
        ('INACTIVE','INACTIVE'),
        ('FINISHED','FINISHED'),
        ('RETIRED','RETIRED'),
    )

    estado=models.CharField(max_length=10,choices=STATUS)
    observacion=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'matricula'

class PagosModel(models.Model):
    id_pago = models.AutoField(primary_key=True)
    id_matricula=models.ForeignKey('MatriculaModel',on_delete=models.CASCADE,db_column='id_matricula',related_name='pagos')
    monto=models.DecimalField(max_digits=10,decimal_places=2)
    
    METODO = (
        ('EFECTIVO','EFECTIVO'),
        ('YAPE','YAPE'),
        ('PLIN','PLIN'),
        ('TRANSFERENCIA','TRANSFERENCIA'),
    )
    
    metodo_pago=models.CharField(max_length=30,choices=METODO)

    MES = (
    ('ENERO','ENERO'),
    ('FEBRERO','FEBRERO'),
    ('MARZO','MARZO'), 
    ('ABRIL','ABRIL'),
    ('MAYO','MAYO'), 
    ('JUNIO','JUNIO'),
    ('JULIO','JULIO'),
    ('AGOSTO','AGOSTO'),
    ('SETIEMBRE','SETIEMBRE'),
    ('OCTUBRE','OCTUBRE'),
    ('NOVIEMBRE','NOVIEMBRE'),
    ('DICIEMBRE','DICIEMBRE',))

    mes_correspondiente=models.CharField(max_length=10,choices=MES)
    fecha_pago=models.DateField()
    observacion=models.CharField(max_length=100)
    
    ESTADO = (
        ('PENDIENTE','PENDIENTE'),
        ('CANCELADO','CANCELADO'),
        ('PARCIAL','PARCIAL'),
        ('ANULADO','ANULADO'),
    )
    
    estado = models.CharField(max_length=10,choices=ESTADO)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'pagos'



