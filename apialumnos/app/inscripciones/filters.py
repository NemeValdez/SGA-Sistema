import django_filters
from app.inscripciones.models import EstudiantesPrimerCarrera, EstudiantesSegundaCarrera


class Inscripcion1Filter(django_filters.FilterSet):
    class Meta():
        model = EstudiantesPrimerCarrera
        fields = ['relacion_estudiante']


class Inscripcion2Filter(django_filters.FilterSet):
    class Meta():
        model = EstudiantesSegundaCarrera
        fields = ['relacion_estudiante']
