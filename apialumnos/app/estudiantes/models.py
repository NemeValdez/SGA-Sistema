from django.db import models


class EstudiantesEstablecimientos(models.Model):
    '''Modelo de relación con la escuela de procedencia del estudiante'''
    nombre_escuela = models.CharField(
        max_length=100, null=False, blank=False)
    titulo = models.CharField(
        max_length=100, null=False, blank=False)
    estado_secundario = models.CharField(
        max_length=1, null=False, blank=False)
    '''Los campos originales del formulario A1 - preinscripción se van a cargar como nuevos cuando se decida cargar'''

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = "Secundario del Estudiante"
        verbose_name_plural = "Secundario del Estudiante"

    def __str__(self):
        return self.nombre_escuela


class Estudiantes(models.Model):
    apellido_estudiante = models.CharField(
        max_length=100, null=False, blank=False)
    nombre_estudiante = models.CharField(
        max_length=100, null=False, blank=False)
    dni_estudiante = models.CharField(
        max_length=8, null=False, blank=False)
    sexo_estudiante = models.CharField(
        max_length=1, null=False, blank=False)
    provincia_estudiante = models.CharField(
        max_length=100, null=False, blank=False)
    telefono_estudiante = models.CharField(
        max_length=50, null=False, blank=False)
    mail_estudiante = models.EmailField(
        null=False, blank=False)
    legajo_estudiante = models.CharField(
        max_length=12, null=False, blank=False)
    secundario_estudiante = models.ForeignKey(
        EstudiantesEstablecimientosPreinscripciones, on_delete=models.CASCADE, related_name="escuela")
    estado_estudiante = models.CharField(
        max_length=20, null=False, blank=False)

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
