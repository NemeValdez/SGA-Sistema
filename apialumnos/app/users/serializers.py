from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from app.users.models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

    def create(self, validated_data):
        usuario = Usuario(**validated_data)
        usuario.set_password(validated_data['password'])
        usuario.save()
        return usuario


class ContraseñaSerializer(serializers.Serializer):
    password = serializers.CharField(
        max_length=10, min_length=8, write_only=True)
    confirmacion = serializers.CharField(
        max_length=10, min_length=8, write_only=True)

    def validate(self, data):
        if data['password'] != data['confirmacion']:
            raise serializers.ValidationError(
                'Debe ingresar ambas contraseñas iguales')
        return data


class TokenSerializer(TokenObtainPairSerializer):
    pass
