from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from app.users.models import Usuario
from app.users.serializers import UsuarioSerializer, ContraseñaSerializer


class UsuarioViewSet(viewsets.GenericViewSet):
    model = Usuario
    serializer_class = UsuarioSerializer
    queryset = None

    def get_object(self, pk):
        return get_object_or_404(self.serializer_class.Meta.model, pk=pk)

    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.serializer_class().Meta.model.objects.filter(is_active=True)
        return self.queryset

    @action(detail=True, methods=['post'], url_path='cambiar-contraseña/')
    def set_password(self, request, pk=None):
        usuario = self.get_object(pk)
        contraseña_serializer = ContraseñaSerializer(data=request.data)
        if contraseña_serializer.is_valid():
            usuario.set_password(
                contraseña_serializer.validated_data['password'])
            usuario.save()
            return Response({
                'mensaje': 'Contraseña actualizada correctamente'
            }, status=status.HTTP_202_ACCEPTED)
        return Response(contraseña_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        usuario = self.get_queryset()
        usuario_serializer = self.serializer_class(usuario, many=True)
        return Response(usuario_serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        usuario = self.get_object(pk)
        usuario_serializer = self.serializer_class(usuario)
        return Response(usuario_serializer.data)

    def create(self, request):
        usuario_serializer = self.serializer_class(data=request.data)
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return Response({'mensaje': 'Usuario creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response(usuario_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        usuario = self.get_object(pk)
        usuario_serializer = self.serializer_class(usuario, data=request.data)
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return Response(usuario_serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(usuario_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        usuario = self.model.objects.filter(id=pk).update(is_active=False)
        if usuario == 1:
            return Response({'Mensaje': 'Usuario eliminado correctamente'}, status=status.HTTP_200_OK)
        return Response({'Mensaje': 'No existe usuario con esos parámetros'}, status=status.HTTP_404_NOT_FOUND)
