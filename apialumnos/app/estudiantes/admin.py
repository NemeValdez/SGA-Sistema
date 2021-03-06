from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from app.estudiantes.models import Estudiantes


class EstudiantesResources(resources.ModelResource):
    class Meta:
        model = Estudiantes


class EstudiantesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    icon_name = 'face'
    search_fields = ['dni_estudiante']
    list_display = (
        'id',
        'nombre_estudiante',
        'apellido_estudiante',
        'dni_estudiante',
    )
    resource_class = EstudiantesResources
    ordering = ('id',)


'''Registro de los modelos de Estudiantes'''
admin.site.register(Estudiantes, EstudiantesAdmin)
