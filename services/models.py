from django.db import models

class ServiciosModel(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripccion = models.TextField()
    precio = models.FloatField()
    duracion = models.IntegerField(null=False, default=0)

    class Meta:
        db_table = 'servicios'

class GradosModel(models.Model):
    id_grado=models.AutoField(primary_key=True)

    TIPO_GRADO=(
        ('PRE_KINDER','PRE_KINDER'),
        ('INICIAL 3','INICIAL 3'),
        ('INICIAL 4','INICIAL 4'),
        ('INICIAL 5','INICIAL 5'),
    )

    grado=models.CharField(max_length=15,choices=TIPO_GRADO)
    
    def __str__(self):
        return self.grade
    
    class Meta:
        db_table='grados'
        verbose_name='Grado'
        verbose_name_plural='Grados'

class AlumnoModel(models.Model):
    id_alumno=models.AutoField(primary_key=True)
    nombres=models.CharField(max_length=50)
    apellidos=models.CharField(max_length=50)
    dni=models.CharField(max_length=8)
    TIPO_ALUMNO=(
        ('REGULAR','REGULAR'),
        ('LIBRE','LIBRE'),
    )
    id_grado=models.ForeignKey('GradosModel',on_delete=models.CASCADE,db_column='id_grado',related_name='alumno')
    tipo_alumno=models.CharField(max_length=15,choices=TIPO_ALUMNO)
    fecha_nac=models.DateField()
    create_en=models.DateTimeField(auto_now_add=True)
    update_en=models.DateTimeField(auto_now=True)
    
    STATUS =(
        ('ACTIVATE','ACTIVATE'),
        ('INACTIVE','INACTIVE'),
        ('DELETED','DELETED'),
        )

    status=models.CharField(max_length=10,choices=STATUS)


    def __str__(self):
        return self.name
    
    class Meta:
        db_table='alumno'
        verbose_name='Alumno'
        verbose_name_plural='Alumnos'

class DocenteModel(models.Model):
    id_docente=models.AutoField(primary_key=True)
    nombres=models.CharField(max_length=50)
    apellidos=models.CharField(max_length=50)
    especialidad=models.CharField(max_length=50)
    dni=models.CharField(max_length=8)
    fecha_nac=models.DateField()
    create_en=models.DateTimeField(auto_now_add=True)
    update_en=models.DateTimeField(auto_now=True)
    
    STATUS =(
            ('ACTIVATE','ACTIVATE'),
            ('INACTIVE','INACTIVE'),
            ('DELETED','DELETED'),
            )
    
    status=models.CharField(max_length=10,choices=STATUS)


    grade=models.ForeignKey('GradosModel',on_delete=models.CASCADE,db_column='id_grado',related_name='docentes')


    def __str__(self):
        return self.name


    class Meta:
        db_table='docente'


class  PadreApoderadoModel(models.Model):
    id_padre=models.AutoField(primary_key=True)
    nombres=models.CharField(max_length=50)
    apellidos=models.CharField(max_length=50)
    dni=models.CharField(max_length=8)
    telefono=models.CharField(max_length=9)
    email=models.EmailField()
    direccion=models.CharField(max_length=100)
    create_en=models.DateTimeField(auto_now_add=True)
    update_en=models.DateTimeField(auto_now=True)
    
    STATUS =(
            ('ACTIVATE','ACTIVATE'),
            ('INACTIVE','INACTIVE'),
            ('DELETED','DELETED'),
            )
    
    status=models.CharField(max_length=10,choices=STATUS)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table='padre_apoderado'
        verbose_name='Padre Apoderado'
        verbose_name_plural='Padres Apoderados'

class AlumnoApoderadoModel(models.Model):
    id_alumno_apoderado=models.AutoField(primary_key=True)
    id_alumno=models.ForeignKey('AlumnoModel',on_delete=models.CASCADE,db_column='id_alumno',related_name='alumno_apoderado')
    id_padre=models.ForeignKey('PadreApoderadoModel',on_delete=models.CASCADE,db_column='id_padre',related_name='alumno_apoderado')
    
    PARENTESCO=(
            ('PADRE','PADRE'),
            ('MADRE','MADRE'),
            ('ABUELO','ABUELO'),
            ('TIO','TIO'),
            ('OTRO','OTRO'),
            )
    
    parentesco = models.CharField(max_length=10,choices=PARENTESCO)

    create_en=models.DateTimeField(auto_now_add=True)
    update_en=models.DateTimeField(auto_now=True)
    
    STATUS =(
            ('ACTIVATE','ACTIVATE'),
            ('INACTIVE','INACTIVE'),
            ('DELETED','DELETED'),
            )
    
    status=models.CharField(max_length=10,choices=STATUS)
    
    class Meta:
        db_table='alumno_apoderado'
        verbose_name='Alumno Apoderado'
        verbose_name_plural='Alumnos Apoderados'

class DocenteServicioModel(models.Model):
    id_docente_servicio = models.AutoField(primary_key=True)
    id_docente=models.ForeignKey('DocenteModel',on_delete=models.CASCADE,db_column='id_docente',related_name='docente_servicio')
    id_servicio=models.ForeignKey('ServiciosModel',on_delete=models.CASCADE,db_column='id_servicio',related_name='docente_servicio')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'docente_servicio'