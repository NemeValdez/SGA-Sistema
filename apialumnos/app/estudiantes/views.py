from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from app.estudiantes.models import Estudiantes
from app.estudiantes.serializers import EstudiantesSerializers, EstudiantesEstablecimientosSerializers


class EstudiantesEstablecimientosViewSet(viewsets.ModelViewSet):
    '''Vista de CRUD de secundario del Estudiante al pre inscribirse'''
    serializer_class = EstudiantesEstablecimientosSerializers
    queryset = EstudiantesEstablecimientosSerializers.Meta.model.objects.all()


class EstudiantesViewSet(viewsets.ModelViewSet):
    '''Vista de CRUD de los datos del estudiante al inscribirse'''
    serializer_class = EstudiantesSerializers
    queryset = EstudiantesSerializers.Meta.model.objects.all()


class DNIViewset(viewsets.ModelViewSet):
    serializer_class = EstudiantesSerializers
    queryset = Estudiantes.model.object.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('dni_estudiante')
