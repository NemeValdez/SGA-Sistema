import django_filters
from app.inscripciones.models import EstudiantesInscripcionesCompletas


class InscripcionFilter(django_filters.FilterSet):
    class Meta():
        model = EstudiantesInscripcionesCompletas
        fields = ['id']
