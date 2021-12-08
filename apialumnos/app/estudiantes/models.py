from django.db import models


class Estudiantes(models.Model):
    '''Datos completos del estudiante'''
    apellido_estudiante = models.CharField(
        max_length=100, null=False, blank=False, verbose_name='Apellido del estudiante')
    nombre_estudiante = models.CharField(
        max_length=100, null=False, blank=False, verbose_name='Nombre del estudiante')
    dni_estudiante = models.CharField(
        max_length=8, null=False, blank=False, verbose_name='DNI del estudiante')
    sexo_estudiante = models.CharField(
        max_length=1, null=False, blank=False, verbose_name='Sexo del estudiante')
    provincia_estudiante = models.CharField(
        max_length=100, null=False, blank=False, verbose_name='Provincia de residencia del estudiante')
    telefono_estudiante = models.CharField(
        max_length=50, null=False, blank=False, verbose_name='Teléfono del estudiante')
    mail_estudiante = models.EmailField(
        null=False, blank=False, verbose_name='Mail del estudiante')
    legajo_estudiante = models.CharField(
        max_length=12, null=False, blank=False, verbose_name='Número de legajo del estudiante')
    nombre_escuela = models.CharField(
        max_length=100, null=False, blank=False, verbose_name='Nombre del secundario del preinscripto')
    titulo_escuela = models.CharField(
        max_length=100, null=False, blank=False, verbose_name='Título que otorga el secundario')
    estado_secundario = models.CharField(
        max_length=1, null=False, blank=False, verbose_name='Estado de la finalización del secundario')
    '''Los campos originales del formulario A1 - preinscripción se van a cargar como nuevos cuando se decida cargar'''

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"

    def __str__(self):
        return '%s %s - DNI: %s' % (self.nombre_estudiante, self.apellido_estudiante, self.dni_estudiante)
