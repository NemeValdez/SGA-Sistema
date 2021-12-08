from rest_framework import serializers
from app.estudiantes.models import Estudiantes


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
            'nombre_escuela': instance.nombre_escuela,
            'titulo_escuela': instance.titulo_escuela,
            'estado_secundario': instance.estado_secundario,
        }
