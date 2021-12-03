from rest_framework import viewsets, status, filters
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from app.estudiantes.serializers import EstudiantesSerializers, EstudiantesEstablecimientosSerializers


class EstudiantesEstablecimientosViewSet(viewsets.ModelViewSet):
    serializer_class = EstudiantesEstablecimientosSerializers

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        return self.get_serializer().Meta.model.objects.filter(id=pk).first()

    def list(self, request):
        establecimiento_serializer = self.get_serializer(
            self.get_queryset(), many=True)
        return Response(establecimiento_serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        buscar_establecimiento = self.get_queryset().filter(id=pk).exists()
        if buscar_establecimiento:
            establecimiento = self.get_queryset().filter(id=pk).first()
            establecimiento_serializer = self.serializer_class(
                establecimiento)
            return Response(establecimiento_serializer.data, status=status.HTTP_200_OK)
        return Response({'mensaje': 'No se han encontrado datos con el parámetro indicado'}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        establecimiento_serializer = self.serializer_class(
            data=request.data)
        if establecimiento_serializer.is_valid():
            establecimiento_serializer.save()
            return Response({'mensaje': 'Datos del secundario guardados correctamente'}, status=status.HTTP_201_CREATED)
        return Response(establecimiento_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        establecimiento = self.get_queryset().filter(id=pk).first()
        if establecimiento:
            establecimiento.delete()
            return Response({'mensaje': 'Datos del secundario del estudiante eliminados correctamente'}, status=status.HTTP_202_ACCEPTED)
        return Response({'mensaje': 'No existe un establecimiento con esos datos'}, status=status.HTTP_400_BAD_REQUEST)


class EstudiantesViewSet(viewsets.ModelViewSet):
    serializer_class = EstudiantesSerializers

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        return self.get_serializer().Meta.model.objects.filter(id=pk).first()

    def list(self, request):
        estudiante_serializer = self.get_serializer(
            self.get_queryset(), many=True)
        return Response(estudiante_serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        buscar_estudiante = self.get_queryset().filter(id=pk).exists()
        if buscar_estudiante:
            estudiante = self.get_queryset().filter(id=pk).first()
            estudiante_serializer = self.serializer_class(
                estudiante)
            return Response(estudiante_serializer.data, status=status.HTTP_200_OK)
        return Response({'mensaje': 'No se han encontrado datos con el parámetro indicado'}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        estudiante_serializer = self.serializer_class(
            data=request.data)
        if estudiante_serializer.is_valid():
            estudiante_serializer.save()
            return Response({'mensaje': 'Datos del estudiante guardados satisfactoriamente'}, status=status.HTTP_201_CREATED)
        return Response(estudiante_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        estudiante_serializer = self.get_queryset().filter(id=pk).first()
        if estudiante_serializer:
            estudiante_serializer.delete()
            return Response({'mensaje': 'Datos del estudiante eliminados correctamente'}, status=status.HTTP_202_ACCEPTED)
        return Response({'mensaje': 'No existe un estudiante con esos datos'}, status=status.HTTP_400_BAD_REQUEST)


class BuscarDNIView(viewsets.ReadOnlyModelViewSet):
    queryset = Estudiantes.objects.all()
    serializer_class = EstudiantesSerializers
    filter_backends = [DjangoFilterBackend]
    search_fields = ['dni_estudiante']
