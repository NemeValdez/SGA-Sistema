from rest_framework import serializers
from app.estudiantes.models import Estudiantes, EstudiantesEstablecimientos


class EstudiantesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Estudiantes
        fields = '__all__'

    def to_representation(self, instance):
        return{
            'id': instance.id,
            'apellido_estudiante': instance.apellido_estudiante,
            'nombre_estudiante': instance.nombre_estudiante,
            'dni_estudiante': instance.dni_estudiante,
            'sexo_estudiante': instance.sexo_estudiante,
            'provincia_estudiante': instance.provincia_estudiante,
            'telefono_estudiante': instance.telefono_estudiante,
            'mail_estudiante': instance.mail_estudiante,
            'legajo_estudiante': instance.legajo_estudiante,
            'estado_estudiante': instance.estado_estudiante,
            'id_escuela': instance.secundario_estudiante.id if instance.secundario_estudiante.id is not None else '',
            'nombre_escuela': instance.secundario_estudiante.nombre_escuela if instance.secundario_estudiante.nombre_escuela is not None else '',
            'titulo': instance.secundario_estudiante.titulo if instance.secundario_estudiante.titulo is not None else '',
            'estado_secundario': instance.secundario_estudiante.estado_secundario if instance.secundario_estudiante.estado_secundario is not None else '',
        }


class EstudiantesEstablecimientosSerializers(serializers.ModelSerializer):
    class Meta:
        model = EstudiantesEstablecimientos
        fields = '__all__'
