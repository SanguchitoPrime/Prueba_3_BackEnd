from django.contrib import admin
from .models import TipoMaquinaria, Maquinaria


@admin.register(TipoMaquinaria)
class TipoMaquinariaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')
    search_fields = ('nombre',)
    list_filter = ('nombre',)


@admin.register(Maquinaria)
class MaquinariaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'patente_serie', 'tipo', 'anio_fabricacion', 'horas_uso', 'operativa')
    list_filter = ('tipo', 'operativa', 'anio_fabricacion')
    search_fields = ('nombre', 'patente_serie', 'observaciones')