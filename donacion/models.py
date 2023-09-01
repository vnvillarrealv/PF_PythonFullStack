#pylint: disable=all
from django.db import models
from django.contrib.admin.widgets import AdminDateWidget
from django import forms
from datetime import datetime
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Create your models here.   
class CATEGORIAS(models.Model):
    categoria = models.CharField(max_length=50)
    class Meta:
        db_table = 'categoria_campaña'
        verbose_name_plural = 'categorias_campañas'
    def __str__(self) -> str:
        # print(f"categoria: {self.categoria}")
        return f"{self.categoria}"
    
class CAMPANIA(models.Model):
    categoria = models.ForeignKey(CATEGORIAS, on_delete=models.CASCADE)
    nombre_campania = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=5000)
    beneficiario = models.CharField(max_length=200)
    monto_a_recaudar= models.DecimalField(max_digits=10,decimal_places=2)
    monto_recaudado = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_inicio = models.DateField()
    fecha_cierre = models.DateField()
    status = models.BooleanField()
    imagen = models.CharField(max_length=5000)

    class Meta:
        db_table = 'campaña'
        verbose_name_plural = 'campañas'
    
    def __str__(self) -> str:
        # print(f"nombre_campaña: {self.nombre_campania}")
        return self.nombre_campania

class DONACION(models.Model):
    nombre_campania = models.ForeignKey(CAMPANIA, on_delete=models.CASCADE,related_name='donaciones')#related_name te ayuda a hacer un "llamadoa al revez" de la tabla campania hacia donacion. YA QUE CAMPANIA NO DEPENDE DE DONACION, y asi es ocmo podiamos llamar a donacion a atraves de campania
    usuario = models.CharField(max_length=200)#luego en el template se colcoa el bloque de codigo correspondiente
    valor_donado= models.DecimalField(max_digits=10,decimal_places=2)
    fecha_donativo = models.DateField(null=True)
    comentario = models.CharField(max_length=5000, null=True)

    class Meta:
        db_table = 'donacion'
        verbose_name_plural = 'donaciones'
    
    def __str__(self) -> str:
        return f"valor donado: ${self.valor_donado}"
    
@receiver([post_save, post_delete], sender=DONACION)
def actualizar_monto_recaudado(sender, instance, **kwargs):
    campania = instance.nombre_campania
    nuevo_monto_recaudado = campania.donaciones.aggregate(models.Sum('valor_donado'))['valor_donado__sum']
    campania.monto_recaudado = nuevo_monto_recaudado or 0
    campania.save()

def categoria_alterna():
    categoria_alterna = models.ForeignKey(CATEGORIAS, on_delete=models.CASCADE)
    return categoria_alterna

class SOLICITUDES_CAMPANIAS(models.Model):
    
    categoria = models.ForeignKey(CATEGORIAS, on_delete=models.SET_DEFAULT, default=categoria_alterna)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    nombre_campania = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=5000)
    beneficiario = models.CharField(max_length=200)
    monto_a_recaudar= models.DecimalField(max_digits=10,decimal_places=2)
    direccion = models.CharField(max_length=500)
    telefono = models.CharField(max_length=500)

    class Meta:
        db_table = 'nueva_solicitud'
        verbose_name_plural = 'nuevas_solicitudes'
    
    def __str__(self) -> str:
        return f"campaña nueva: ${self.nombre_campania}"


