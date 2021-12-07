from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from app.users.models import Usuario


class Salir(GenericAPIView):
    def post(self, request, *args, **kwargs):
        usuario = Usuario.objects.filter(
            id=request.data.get('usuario', 0))
        if usuario.exists():
            RefreshToken.for_user(usuario.first())
            return Response({
                'mensaje': 'Sesión cerrada correctamente'
            }, status=status.HTTP_200_OK)
        return Response({'error': 'No existe este usuario'}, status=status.HTTP_400_BAD_REQUEST)
