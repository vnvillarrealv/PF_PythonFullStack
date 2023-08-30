#pylint: disable=all
from django.contrib import admin
from .models import CATEGORIAS, CAMPANIA, DONACION

# Register your models here.
# admin.site.register(principal)
# admin.site.register(animal)
# admin.site.register(salud)
# admin.site.register(educacion)
# admin.site.register(humanitaria)

@admin.register(CATEGORIAS)
class CATEGORIASAdmin(admin.ModelAdmin):
    list_displya = ('id','categoria')
    list_filter = ('categoria',)

@admin.register(CAMPANIA)
class CAMPANIAAdmin(admin.ModelAdmin):
    list_display = ('id','categoria','nombre_campania','beneficiario','monto_a_recaudar','monto_recaudado','fecha_cierre','status')
    list_filter = ('categoria',)


@admin.register(DONACION)
class DONACIONAdmin(admin.ModelAdmin):
    list_display = ('id','nombre_campania','usuario','valor_donado')


