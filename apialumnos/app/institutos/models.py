from django.db import models
from app.users.models import Usuario


class Institutos(models.Model):
    '''Datos completos del Instituto'''
    numero_instituto = models.CharField(
        max_length=4, null=False, blank=False, verbose_name='Número del Instituto')
    calle_instituto = models.CharField(
        max_length=50, null=False, blank=False, verbose_name='Dirección completa del Instituto')
    altura_instituto = models.CharField(
        max_length=5, null=False, blank=False, verbose_name='Altura de la dirección del Instituto')
    mail_general_instituto = models.EmailField(
        null=False, blank=False, verbose_name='Mail oficial del Instituto')
    mail_preinscripcion_instituto = models.EmailField(
        null=False, blank=False, verbose_name='Mail destinado a la preinscripción')
    telefono_instituto = models.CharField(
        max_length=20, null=False, blank=False, verbose_name='Teléfono del Instituto')
    sitio_web_instituto = models.URLField(
        null=True, blank=True, verbose_name='Sitio web del Instituto')

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = "Instituto"
        verbose_name_plural = "Institutos"

    def __str__(self):
        return 'Instituto N°: %s' % (self.numero)


class SedesInstitutos(models.Model):
    '''Datos de la Sede o Anexo del Instituto en caso de poseer'''
    nombre_sede_instituto = models.CharField(
        max_length=100, null=False, blank=False, verbose_name='Nombre de la Sede o Anexo del Instituto')
    calle_sede_instituto = models.CharField(
        max_length=50, null=False, blank=False, verbose_name='Dirección completa del Instituto')
    altura_sede_instituto = models.CharField(
        max_length=5, null=False, blank=False, verbose_name='Altura de la dirección del Instituto')
    relacion_instituto_sede = models.ForeignKey(
        Institutos, on_delete=models.CASCADE, related_name='sedesInstitutos')

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = "Sede del Instituto"
        verbose_name_plural = "Sedes del Instituto"

    def __str__(self):
        return 'Instituto N°: %s - Sede: %s' % (self.numero_instituto, self.nombre_sede_instituto)


class RolesJerarquicos(models.Model):
    '''Tipos de cargos o roles dentro de un Instituto'''
    nombre_rol = models.CharField(
        max_length=100, null=False, blank=False, verbose_name='Rol que desempeña en el Instituto')

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos en Sistema"

    def __str__(self):
        return 'Cargo: %s' % (self.nombre_rol)


class Jerarquicos(models.Model):
    '''Datos de los responsables de la gestión de la preinscripción'''
    nombre_jerarquico = models.CharField(
        max_length=255, blank=False, null=False, verbose_name='Nombre de la persona responsable')
    apellido_jerarquico = models.CharField(
        max_length=255, blank=False, null=False, verbose_name='Apellido de la persona responsable')
    sexo_jerarquico = models.CharField(
        max_length=1, null=True, blank=True, verbose_name='Sexo de la persona responsable')
    fecha_nacimiento_jerarquico = models.DateField(
        null=True, blank=True, verbose_name='Fecha de nacimiento del responsable')
    relacion_rol_jerarquico = models.ForeignKey(
        RolesJerarquicos, on_delete=models.CASCADE, related_name='cargosJerarquicos')
    relacion_jerarquico_usuario = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, related_name='jerarquicoUsuario')

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = "Responsable"
        verbose_name_plural = "Responsables"

    def __str__(self):
        return '%s %s - DNI: %s' % (self.nombre_jerarquico, apellido_jerarquico, self.dni_usuario)


class InstitutosJerarquicos(models.Model):
    '''Datos de los responsables y de los institutos que representan'''
    relacion_jerarquico = models.ForeignKey(
        Jerarquicos, on_delete=models.CASCADE, related_name='responsableInstituto')
    relacion_instituto = models.ForeignKey(
        Institutos, on_delete=models.CASCADE, related_name='institutoResponsable')

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = "Responsable e Instituto"
        verbose_name_plural = "Responsables y sus Institutos"

    def __str__(self):
        return '%s %s - DNI: %s' % (self.nombre_jerarquico, apellido_jerarquico, self.dni_usuario)
