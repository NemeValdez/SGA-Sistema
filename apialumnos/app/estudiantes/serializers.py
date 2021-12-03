from rest_framework import serializers
from app.estudiantes.models import Estudiantes, EstudiantesEstablecimientos


class EstudiantesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Estudiantes
        fields = '__all__'


class EstudiantesEstablecimientosSerializers(serializers.ModelSerializer):
    class Meta:
        model = EstudiantesEstablecimientos
        fields = '__all__'
