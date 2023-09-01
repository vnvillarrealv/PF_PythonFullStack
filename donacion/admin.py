#pylint: disable=all
from django.contrib import admin
from .models import CATEGORIAS, CAMPANIA, DONACION, SOLICITUDES_CAMPANIAS

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


@admin.register(SOLICITUDES_CAMPANIAS)
class SOLICITUDES_CAMPANIASAdmin(admin.ModelAdmin):
    list_display = ('categoria','nombre_campania','nombre','apellido','beneficiario','monto_a_recaudar')


