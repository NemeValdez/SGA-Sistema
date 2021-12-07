from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from app.carreras.models import TurnosCarreras, Carreras, LimitacionesCarreras
from app.carreras.serializers import TurnosCarrerasSerializers, CarrerasSerializers, LimitacionesCarrerasSerializers


class TurnosCarrerasViewSet(viewsets.ReadOnlyModelViewSet):
    '''Vista que hace un listado general y filtrado de los turnos de las carreras'''
    serializer_class = TurnosCarrerasSerializers
    permission_classes = (IsAuthenticated,)
    queryset = TurnosCarrerasSerializers.Meta.model.objects.all()


class CarrerasViewSet(viewsets.ModelViewSet):
    '''Vista que gestiona todo un CRUD de Carreras'''
    serializer_class = CarrerasSerializers
    permission_classes = (IsAuthenticated,)
    queryset = CarrerasSerializers.Meta.model.objects.all()


class LimitacionesCarrerasViewSet(viewsets.ModelViewSet):
    '''Vista que gestiona todo un CRUD de los limites de la preinscripción'''
    serializer_class = LimitacionesCarrerasSerializers
    permission_classes = (IsAuthenticated,)
    queryset = LimitacionesCarrerasSerializers.Meta.model.objects.all()
