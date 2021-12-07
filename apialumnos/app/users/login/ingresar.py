from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from app.users.serializers import TokenSerializer, UsuarioSerializer


class Ingresar(TokenObtainPairView):
    serializer_class = TokenSerializer

    def post(self, request, *args, **kwargs):
        dni_usuario = request.data.get('dni_usuario', '')
        password = request.data.get('password', '')
        usuario = authenticate(
            dni_usuario=dni_usuario,
            password=password
        )
        if usuario:
            login_serializer = self.serializer_class(data=request.data)
            if login_serializer.is_valid():
                usuario_serializer = UsuarioSerializer(usuario)
                return Response({
                    'token_acceder': login_serializer.validated_data.get('access'),
                    'token_refrescar': login_serializer.validated_data.get('refresh'),
                    'usuario': usuario_serializer.data,
                    'message': 'Inicio de Sesión exitoso'
                }, status=status.HTTP_200_OK)
            return Response({'error': 'Datos ingresados incorrectos'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Datos ingresados incorrectos'}, status=status.HTTP_400_BAD_REQUEST)
