#pylint: disable=all
from django.db import models
from django.contrib.admin.widgets import AdminDateWidget
from django import forms

# Create your models here.   
class categorias(models.Model):
    categoria = models.CharField(max_length=50)
    class Meta:
        db_table = 'categorias_campañas'
    def __str__(self) -> str:
        # print(f"categoria: {self.categoria}")
        return f"{self.categoria}"
    
class campania(models.Model):
    categoria = models.ForeignKey(categorias, on_delete=models.CASCADE)
    nombre_campania = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=5000)
    beneficiario = models.CharField(max_length=200)
    monto_a_recaudar= models.DecimalField(max_digits=10,decimal_places=2)
    monto_recaudado = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_inicio = models.DateField()
    # fecha_inicio = forms.DateField(widget=AdminDateWidget(format='%d/%m/%Y'))
    fecha_cierre = models.DateField()
    # fecha_cierre = forms.DateField(widget=AdminDateWidget(format='%d/%m/%Y'))
    status = models.BooleanField()
    imagen = models.CharField(max_length=500)

    class Meta:
        db_table = 'campañas'
    
    def __str__(self) -> str:
        # print(f"nombre_campaña: {self.nombre_campania}")
        return self.nombre_campania
    

class donacion(models.Model):

    nombre_campania = models.ForeignKey(campania, on_delete=models.CASCADE, related_name="donaciones") #arojaba eero de esperar numeor pero recibia string, se agrego una colmna mas de id
    usuario = models.CharField(max_length=200)
    valor_donado= models.DecimalField(max_digits=10,decimal_places=2)
    fecha_donativo = models.DateField(null=True)
    comentario = models.CharField(max_length=5000)

    class Meta:
        db_table = 'donacion'
    
    def __str__(self) -> str:
        return f"valor donado: ${self.valor_donado}"
    
    
class Comentarios(models.Model):
    nombre_campania = models.ForeignKey(campania, on_delete=models.CASCADE, related_name="comentarios")
    name = models.CharField(max_length=255)
    body = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True) #anade la fecha actual

    def __str__(self):
        return '%s - %s' % (self.nombre_campania, self.name)
    

# class Comentarios(models.Model):
#     nombre_campania = models.ForeignKey(campania, related_name='comentarios', on_delete=models.CASCADE)
#     autor = models.CharField(max_length=255)
#     contenido = models.TextField()
#     fecha = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return str(self.autor) + ', ' + self.nombre_campania[:40]


