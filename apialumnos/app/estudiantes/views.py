from rest_framework import viewsets, generics
from django_filters import rest_framework as filters
from app.estudiantes.serializers import EstudiantesSerializers, EstudiantesEstablecimientosSerializers


class EstudiantesEstablecimientosViewSet(viewsets.ModelViewSet):
    '''Vista de CRUD de secundario del Estudiante al pre inscribirse'''
    serializer_class = EstudiantesEstablecimientosSerializers
    queryset = EstudiantesEstablecimientosSerializers.Meta.model.objects.all()


class EstudiantesViewSet(viewsets.ModelViewSet):
    '''Vista de CRUD de los datos del estudiante al inscribirse'''
    serializer_class = EstudiantesSerializers
    queryset = EstudiantesSerializers.Meta.model.objects.all()


class BuscarDNIView(generics.ListAPIView):
    '''Vista que permite buscar por DNI a los registrados como estudiantes'''
    queryset = EstudiantesSerializers.Meta.model.objects.all()
    serializer_class = EstudiantesSerializers
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('dni_estudiante',)
