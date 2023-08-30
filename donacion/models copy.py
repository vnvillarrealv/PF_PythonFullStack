from django.db import models

# Create your models here.
class principal(models.Model):#detalles de la campaña
    categoria = models.CharField(max_length=50)
    campania = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500,null=True)
    beneficiario = models.CharField(max_length=50,null=True)
    monto_a_recaudar= models.DecimalField(max_digits=10,decimal_places=2,null=True)
    # recaudos = models.CharField(max_length=50)
    monto_recaudado = models.DecimalField(max_digits=10, decimal_places=2)
    # total_donativos = models.CharField(max_length=50)
    fecha_inicio = models.DateField(null=True)
    fecha_cierre = models.DateField(null=True)
    total_donativos = models.IntegerField()
    imagen = models.CharField(max_length=500,null=True)

    class Meta:
        db_table = 'categorias_campanias'
    
    def __str__(self) -> str:
        return f"{self.categoria}"
    

#modelos categoria
#modelo detalles campaaña(CAMPAÑA)
#modelos donacion relacionarlo con el usuario
#modelo usuario
#MODELOS PARA COMENTARIOS



    
class animal(models.Model):
    categoria = models.ForeignKey(principal, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50)
    valor_donado =  models.DecimalField(max_digits=10, decimal_places=2)
    fecha_donacion =  models.DateField()

    class Meta:
        db_table= 'mi_pet'
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}\n ${self.valor_donado}"
    
class salud(models.Model):
    categoria = models.ForeignKey(principal, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50)
    valor_donado =  models.DecimalField(max_digits=10, decimal_places=2)
    fecha_donacion =  models.DateField()

    class Meta:
        db_table= 'cruz_roja_en_accion'
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}\n ${self.valor_donado}"
    

class educacion(models.Model):
    categoria = models.ForeignKey(principal, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50)
    valor_donado =  models.DecimalField(max_digits=10, decimal_places=2)
    fecha_donacion =  models.DateField()

    class Meta:
        db_table= 'educando_a_lo_lejos'
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}\n ${self.valor_donado}"
    

class humanitaria(models.Model):
    categoria = models.ForeignKey(principal, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50)
    valor_donado =  models.DecimalField(max_digits=10, decimal_places=2)
    fecha_donacion =  models.DateField()

    class Meta:
        db_table= 'recoleccion_de_alimentos'
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}\n ${self.valor_donado}"
    



