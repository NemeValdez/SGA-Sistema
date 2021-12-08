from rest_framework import viewsets, status
from rest_framework.response import Response
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


class BuscarDNIView(viewsets.ModelViewSet):
    '''Vista que permite buscar por DNI a los registrados como estudiantes'''
    serializer_class = EstudiantesSerializers()

    def get_queryset(self, pk=None):
        if pk is None:
            return Response({
                'mensaje': 'Error en los parámetros de la búsqueda'
            }, status=status.HTTP_404_NOT_FOUND)
        return self.get_serializer().Meta.model.objects.filter(dni_estudiante=pk).first()

    def retrieve(self, request, pk=None):
        buscar_dni = self.get_queryset().filter(dni_estudiante=pk).exists()
        if buscar_dni:
            dni = self.get_queryset().filter(dni_estudiante=pk).first()
            dni_serializer = self.serializer_class(dni)
            return Response(dni_serializer.data, status=status.HTTP_200_OK)
        return Response({'mensaje': 'No se han encontrado datos con el parámetro indicado'}, status=status.HTTP_404_NOT_FOUND)
