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

    def to_representation(self, instance):
        return{
            'id': instance.id,
            'nombre_carrera': instance.nombre_carrera,
            'resolucion_carrera': instance.resolucion_carrera,
            'id_turno': instance.relacion_turno_carrera.id if instance.relacion_turno_carrera.id is not None else '',
            'turno_carrera': instance.relacion_turno_carrera.turno_carrera if instance.relacion_turno_carrera.turno_carrera is not None else '',
            'turno_carrera_completo': instance.relacion_turno_carrera.turno_carrera_completo if instance.relacion_turno_carrera.turno_carrera_completo is not None else ''
        }


class LimitacionesCarrerasSerializers(serializers.ModelSerializer):
    class Meta:
        model = LimitacionesCarreras
        fields = '__all__'

    def to_representation(self, instance):
        return{
            'id': instance.id,
            'cantidad_aceptada': instance.cantidad_aceptada,
            'cantidad_lista_espera': instance.cantidad_lista_espera,
            'fecha_inicio': instance.fecha_inicio,
            'fecha_fin': instance.fecha_fin,
            'id_carrera': instance.relacion_carrera.id if instance.relacion_carrera.id is not None else '',
            'nombre_carrera': instance.relacion_carrera.nombre_carrera if instance.relacion_carrera.nombre_carrera is not None else '',
            'resolucion_carrera': instance.relacion_carrera.resolucion_carrera if instance.relacion_carrera.resolucion_carrera is not None else '',
            'id_turno': instance.relacion_carrera.relacion_turno_carrera.id if instance.relacion_carrera.relacion_turno_carrera.id is not None else '',
            'turno_carrera': instance.relacion_carrera.relacion_turno_carrera.turno_carrera if instance.relacion_carrera.relacion_turno_carrera.turno_carrera is not None else '',
            'turno_carrera_completo': instance.relacion_carrera.relacion_turno_carrera.turno_carrera_completo if instance.relacion_carrera.relacion_turno_carrera.turno_carrera_completo is not None else ''
        }
