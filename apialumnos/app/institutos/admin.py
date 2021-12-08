from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from app.institutos.models import Institutos, SedesInstitutos, RolesJerarquicos, Jerarquicos, InstitutosJerarquicos


class RolesJerarquicosAdmin(admin.ModelAdmin):
    icon_name = 'supervisor_account'
    list_display = (
        'id',
        'nombre_rol',
    )
    ordering = ('id',)


class InstitutosResources(resources.ModelResource):
    class Meta:
        model = Institutos


class InstitutosAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    icon_name = 'psychology'
    search_fields = ['numero_instituto']
    list_display = (
        'id',
        'numero_instituto',
        'calle_instituto',
        'altura_instituto',
        'mail_general_instituto',
        'mail_preinscripcion_instituto',
        'sitio_web_instituto',
    )
    resource_class = InstitutosResources
    ordering = ('id',)


class InstitutosJerarquicosResources(resources.ModelResource):
    class Meta:
        model = InstitutosJerarquicos


class InstitutosJerarquicosAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    icon_name = 'psychology'
    list_display = ('id',)
    resource_class = InstitutosJerarquicosResources


'''Registro de los modelos de Estudiantes'''
admin.site.register(RolesJerarquicos, RolesJerarquicosAdmin)
admin.site.register(Institutos, InstitutosAdmin)
admin.site.register(InstitutosJerarquicos, InstitutosJerarquicosAdmin)
