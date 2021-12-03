from rest_framework import serializers
from app.carreras.models import TurnosCarreras, Carreras, LimitacionesCarreras


class TurnosCarrerasSerializers(serializers.ModelSerializer):
    class Meta:
        model = TurnosCarreras
        fields = '__all__'


class CarrerasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Carreras
        fields = '__all__'


class LimitacionesCarrerasSerializers(serializers.ModelSerializer):
    class Meta:
        model = LimitacionesCarreras
        fields = '__all__'
