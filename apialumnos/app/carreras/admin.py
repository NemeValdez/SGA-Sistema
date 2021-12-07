from django.contrib.admin import ModelAdmin, register
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from app.carreras.models import TurnosCarreras, Carreras, LimitacionesCarreras


@register(TurnosCarreras)
class TurnosCarrerasAdmin(ModelAdmin):
    icon_name = 'query_builder'
    list_display = (
        'id',
        'turno_carrera',
        'turno_carrera_completo'
    )
    ordering = ('id',)


class CarrerasResources(resources.ModelResource):
    class Meta:
        model = Carreras


@register(Carreras)
class CarrerasAdmin(ModelAdmin):
    icon_name = 'leaderboard'
    search_fields = ['resolucion_carrera', 'nombre_carrera']
    list_display = (
        'id',
        'nombre_carrera',
        'resolucion_carrera',
        'relacion_turno_carrera'
    )
    resource_class = CarrerasResources
    ordering = ('id',)


@register(LimitacionesCarreras)
class LimitacionesCarrerasAdmin(ModelAdmin):
    icon_name = 'settings'
    list_display = (
        'id',
        'cantidad_aceptada',
        'cantidad_lista_espera',
        'fecha_inicio',
        'fecha_fin'
    )
    ordering = ('id',)
