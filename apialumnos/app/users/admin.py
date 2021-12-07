from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from app.users.models import Usuario


class UsuariosResources(resources.ModelResource):
    class Meta:
        model = Usuario


class UsuariosAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    icon_name = 'supervisor_account'
    search_fields = ['dni_usuario']
    list_display = (
        'id',
        'dni_usuario'
    )
    ordering = ('id',)
    resource_class = UsuariosResources


admin.site.register(Usuario, UsuariosAdmin)
