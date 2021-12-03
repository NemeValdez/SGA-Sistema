from django.db import models


class TurnosCarreras(models.Model):
    turno_carrera = models.CharField(max_length=1, null=False,  blank=False)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = "Turno de Carrera"
        verbose_name_plural = "Turnos de Carrera"

    def __str__(self):
        return 'Turno: %s' % (self.turno_carrera)


class Carreras(models.Model):
    nombre_carrera = models.CharField(max_length=100, null=False, blank=False)
    resolucion_carrera = models.CharField(
        max_length=10, null=False, blank=False)
    relacion_turno_carrera = models.ForeignKey(
        TurnosCarreras, on_delete=models.CASCADE)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = "Carrera"
        verbose_name_plural = "Carreras"

    def __str__(self):
        return 'Carrera N°: %s - Nombre: %s' % (self.resolucion_carrera, self.nombre_carrera)


class LimitacionesCarreras(models.Model):
    cantidad_actual = models.PositiveIntegerField(
        default=0)
    cantidad_aceptada = models.PositiveIntegerField(
        default=0)
    cantidad_lista_espera = models.PositiveIntegerField(
        default=0)
    fecha_inicio = models.DateField(
        auto_now=False, auto_now_add=False, null=False, blank=True)
    fecha_fin = models.DateField(
        auto_now=False, auto_now_add=False, null=False, blank=True)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = "Limitación"
        verbose_name_plural = "Limitaciones"

    def __str__(self):
        return 'Existen %s preinscriptos de %s disponibles' % (self.cantidad_actual, self.cantidad_aceptada)
