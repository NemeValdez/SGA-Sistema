from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from app.carreras.serializers import TurnosCarrerasSerializers, CarrerasSerializers, LimitacionesCarrerasSerializers


class TurnosCarrerasViewSet(viewsets.ModelViewSet):
    serializer_class = TurnosCarrerasSerializers
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        return self.get_serializer().Meta.model.objects.filter(id=pk).first()

    def list(self, request):
        turno_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(turno_serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        buscar_turno = self.get_queryset().filter(id=pk).exists()
        if buscar_turno:
            turno = self.get_queryset().filter(id=pk).first()
            turno_serializer = self.serializer_class(turno)
            return Response(turno_serializer.data, status=status.HTTP_200_OK)
        return Response({'mensaje': 'No se han encontrado datos con el parámetro indicado'}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        turno_serializer = self.serializer_class(data=request.data)
        if turno_serializer.is_valid():
            turno_serializer.save()
            return Response({'mensaje': 'Turno creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response(turno_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request):
        if self.get_queryset(pk):
            turno_serializer = self.serializer_class(
                self.get_queryset(pk), data=request.data)
            if turno_serializer.is_valid():
                turno_serializer.save()
                return Response(turno_serializer.data, status=status.HTTP_200_OK)
            return Response(turno_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'mensaje': 'No se encontraron datos con ese parámetro'}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        turno_serializer = self.get_queryset().filter(id=pk).first()
        if turno_serializer:
            turno_serializer.delete()
            return Response({'mensaje': 'Turno eliminado correctamente'}, status=status.HTTP_202_ACCEPTED)
        return Response({'mensaje': 'No existe un turno con esos datos'}, status=status.HTTP_400_BAD_REQUEST)


class TurnosCarrerasViewSet(viewsets.ModelViewSet):
    serializer_class = CarrerasSerializers
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        return self.get_serializer().Meta.model.objects.filter(id=pk).first()

    def list(self, request):
        carrera_serializer = self.get_serializer(
            self.get_queryset(), many=True)
        return Response(carrera_serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        buscar_turno = self.get_queryset().filter(id=pk).exists()
        if buscar_turno:
            turno = self.get_queryset().filter(id=pk).first()
            carrera_serializer = self.serializer_class(turno)
            return Response(carrera_serializer.data, status=status.HTTP_200_OK)
        return Response({'mensaje': 'No se han encontrado datos con el parámetro indicado'}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        carrera_serializer = self.serializer_class(data=request.data)
        if carrera_serializer.is_valid():
            carrera_serializer.save()
            return Response({'mensaje': 'Turno creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response(carrera_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request):
        if self.get_queryset(pk):
            carrera_serializer = self.serializer_class(
                self.get_queryset(pk), data=request.data)
            if carrera_serializer.is_valid():
                carrera_serializer.save()
                return Response(carrera_serializer.data, status=status.HTTP_200_OK)
            return Response(carrera_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'mensaje': 'No se encontraron datos con ese parámetro'}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        carrera_serializer = self.get_queryset().filter(id=pk).first()
        if carrera_serializer:
            carrera_serializer.delete()
            return Response({'mensaje': 'Turno eliminado correctamente'}, status=status.HTTP_202_ACCEPTED)
        return Response({'mensaje': 'No existe un turno con esos datos'}, status=status.HTTP_400_BAD_REQUEST)
