from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from app.inscripciones.models import InstitutosCarreras, Inscripciones, EstudiantesPrimerCarrera, EstudiantesSegundaCarrera


class InstitutosCarrerasAdmin(admin.ModelAdmin):
    icon_name = 'settings_applications'
    list_display = ('id',)
    ordering = ('id',)


class InscripcionesResources(resources.ModelResource):
    class Meta:
        model = Inscripciones


class InscripcionesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    icon_name = 'how_to_reg'
    search_fields = ['fecha_inscripcion']
    list_display = (
        'id',
        'fecha_inscripcion')
    ordering = ('id',)
    resource_class = InscripcionesResources


class EstudiantesPrimerCarreraResources(resources.ModelResource):
    class Meta:
        model = EstudiantesPrimerCarrera


class EstudiantesSegundaCarreraResources(resources.ModelResource):
    class Meta:
        model = EstudiantesSegundaCarrera


class EstudiantesPrimerCarreraAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    icon_name = 'looks_one'
    search_fields = ['dni_estudiante']
    list_display = (
        'id',
    )
    ordering = ('id',)
    resource_class = EstudiantesPrimerCarreraResources


class EstudiantesSegundaCarreraAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    icon_name = 'looks_two'
    search_fields = ['dni_estudiante']
    list_display = (
        'id',
    )
    ordering = ('id',)
    resource_class = EstudiantesSegundaCarreraResources


'''Registro de los modelos de Carreras'''
admin.site.register(InstitutosCarreras, InstitutosCarrerasAdmin)
admin.site.register(Inscripciones, InscripcionesAdmin)
admin.site.register(EstudiantesPrimerCarrera,
                    EstudiantesPrimerCarreraAdmin)
admin.site.register(EstudiantesSegundaCarrera,
                    EstudiantesSegundaCarreraAdmin)
