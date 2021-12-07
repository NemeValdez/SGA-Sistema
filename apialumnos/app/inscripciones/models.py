from django.db import models
from app.carreras.models import Carreras
from app.estudiantes.models import Estudiantes
from app.institutos.models import Institutos


class InstitutosCarreras(models.Model):
    '''Modelo que relaciona un Instituto con sus carreras y los contadores de inscripciones en esta'''
    relacion_instituto = models.ForeignKey(
        Institutos, on_delete=models.CASCADE, related_name='institutosInscripcion')
    relacion_carrera = models.ForeignKey(
        Carreras, on_delete=models.CASCADE, related_name='carrerasInscripcion')
    contador_aceptados = models.PositiveIntegerField(
        null=False, blank=False, default=0)
    contador_lista_espera = models.PositiveIntegerField(
        null=False, blank=False, default=0)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = "Relación entre Instituto y Carrera"
        verbose_name_plural = "Relaciones entre Institutos y Carreras"

    def __str__(self):
        return '%s dictada en el Instituto N° %s' % (self.nombre_carrera, self.numero_instituto)


class Inscripciones(models.Model):
    '''Modelo que otorga detalle del momento de la inscripción'''
    fecha_inscripcion = models.DateTimeField(
        null=False, blank=False, verbose_name='Fecha y hora de la preinscripción')

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = "Dato de Inscripción"
        verbose_name_plural = "Datos de Inscripciones"

    def __str__(self):
        return 'Inscripción N° %s realizada el %s' % (str(self.id), str(self.fecha_inscripcion))


class EstudiantesPrimerCarrera(models.Model):
    '''Inscripción del estudiante a su primer carrera'''
    relacion_estudiante = models.ForeignKey(
        Estudiantes, on_delete=models.CASCADE, related_name='estudiantesPreinscripcionUno')
    primer_carrera = models.OneToOneField(
        Carreras, on_delete=models.CASCADE, related_name='carrerasPreinscripcionUno')
    relacion_inscripcion = models.ForeignKey(
        Inscripciones, on_delete=models.CASCADE, related_name='inscripcionPreinscripcionUno')

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = "Inscripción formalizada"
        verbose_name_plural = "Inscripciones formalizadas"

    def __str__(self):
        return 'Inscripción N° %s del Estudiante %s' % (str(self.relacion_inscripcion.id), str(self.relacion_estudiante.dni_estudiante))


class EstudiantesSegundaCarrera(models.Model):
    '''Inscripción del estudiante a su primer carrera'''
    relacion_estudiante = models.ForeignKey(
        Estudiantes, on_delete=models.CASCADE, related_name='estudiantesPreinscripcionDos')
    segunda_carrera = models.OneToOneField(
        Carreras, on_delete=models.CASCADE, related_name='carrerasPreinscripcionDos')
    relacion_inscripcion = models.ForeignKey(
        Inscripciones, on_delete=models.CASCADE, related_name='inscripcionPreinscripcionDos')

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = "Inscripción formalizada"
        verbose_name_plural = "Inscripciones formalizadas"

    def __str__(self):
        return 'Inscripción N° %s del Estudiante %s' % (str(self.relacion_inscripcion.id), str(self.relacion_estudiante.dni_estudiante))
