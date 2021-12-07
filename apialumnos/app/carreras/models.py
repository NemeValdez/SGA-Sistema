from django.db import models


class TurnosCarreras(models.Model):
    '''Turnos en lo que se puede dictar una carrera'''
    turno_carrera = models.CharField(
        max_length=1, null=False,  blank=False, verbose_name='Turno implicíto')
    turno_carrera_completo = models.CharField(
        max_length=6, null=False, blank=False, verbose_name='Turno explicíto')

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
    '''Datos minímos de las carreras posibles para la preinscripción'''
    nombre_carrera = models.CharField(
        max_length=100, null=False, blank=False, verbose_name='Carrera')
    resolucion_carrera = models.CharField(
        max_length=10, null=False, blank=False, verbose_name='Resolución')
    relacion_turno_carrera = models.ForeignKey(
        TurnosCarreras, on_delete=models.CASCADE, related_name='turnosCarreras')

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
    '''Filtros de cantidades aceptadas según instituto y fechas de la preinscripción'''
    cantidad_aceptada = models.PositiveIntegerField(
        default=0, verbose_name='Totales de inscripciones aceptadas')
    cantidad_lista_espera = models.PositiveIntegerField(
        default=0, verbose_name='Totales de inscripciones aceptadas en lista de espera')
    fecha_inicio = models.DateField(
        auto_now=False, auto_now_add=False, null=False, blank=True, verbose_name='Fecha de inicio de preinscripción')
    fecha_fin = models.DateField(
        auto_now=False, auto_now_add=False, null=False, blank=True, verbose_name='Fecha de cierre de preinscripción')
    relacion_carrera = models.ForeignKey(
        Carreras, on_delete=models.CASCADE, related_name='limitesCarreras')

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
