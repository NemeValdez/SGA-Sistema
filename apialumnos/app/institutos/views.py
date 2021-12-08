from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from app.institutos.serializers import InstitutosSerializers, SedesInstitutosSerializers, RolesJerarquicosSerializers, JerarquicosSerializers


class InstitutosViewSet(viewsets.ModelViewSet):
    '''Vista de CRUD de los Institutos'''
    serializer_class = InstitutosSerializers
    queryset = InstitutosSerializers.Meta.model.objects.all()
    permission_classes = (IsAuthenticated,)


class SedesInstitutosViewSet(viewsets.ModelViewSet):
    '''Vista de CRUD de las Sedes o Anexos de los Institutos'''
    serializer_class = SedesInstitutosSerializers
    queryset = SedesInstitutosSerializers.Meta.model.objects.all()
    permission_classes = (IsAuthenticated,)


class RolesJerarquicosViewSet(viewsets.ModelViewSet):
    '''Vista que hace un listado general y filtrado de los cargos que poseen las personas en el Instituto'''
    serializer_class = RolesJerarquicosSerializers
    queryset = RolesJerarquicosSerializers.Meta.model.objects.all()
    permission_classes = (IsAuthenticated,)


class JerarquicosViewSet(viewsets.ModelViewSet):
    '''Vista que hace un listado general y filtrado de los usuarios que poseen acceso como jerárquicos al sistema'''
    serializer_class = JerarquicosSerializers
    queryset = JerarquicosSerializers.Meta.model.objects.all()
    permission_classes = (IsAuthenticated,)
