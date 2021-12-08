import django_filters
from app.estudiantes.models import Estudiantes


class DNIFilter(django_filters.FilterSet):
    class Meta():
        model = Estudiantes
        fields = ['dni_estudiante']
