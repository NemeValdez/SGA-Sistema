from rest_framework import viewsets
from app.estudiantes.filters import DNIFilter
from app.estudiantes.serializers import EstudiantesSerializers


class EstudiantesViewSet(viewsets.ModelViewSet):
    '''Vista de CRUD de los datos del estudiante al inscribirse'''
    serializer_class = EstudiantesSerializers
    queryset = EstudiantesSerializers.Meta.model.objects.all()


class BuscarDNIView(viewsets.ReadOnlyModelViewSet):
    queryset = EstudiantesSerializers.Meta.model.objects.all()
    serializer_class = EstudiantesSerializers
    filter_class = DNIFilter
    search_fields = ('=dni_estudiante',)
