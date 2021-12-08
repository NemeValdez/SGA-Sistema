from rest_framework import serializers
from app.inscripciones.models import InstitutosCarreras, Inscripciones, EstudiantesPrimerCarrera, EstudiantesSegundaCarrera, EstudiantesInscripcionesCompletas


class InstitutosCarrerasSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstitutosCarreras
        fields = '__all__'

    def to_representation(self, instance):
        return{
            'id': instance.id,
            'id_instituto': instance.relacion_instituto.id if instance.relacion_instituto.id is not None else '',
            'instituto': instance.relacion_instituto.numero_instituto if instance.relacion_instituto.numero_instituto is not None else '',
            'id_carrera': instance.relacion_carrera.id if instance.relacion_carrera.id is not None else '',
            'carrera': instance.relacion_carrera.nombre_carrera if instance.relacion_carrera.nombre_carrera is not None else '',
            'contador_aceptados': instance.contador_aceptados,
            'contador_lista_espera': instance.contador_lista_espera
        }


class InscripcionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscripciones
        fields = '__all__'


class EstudiantesPrimerCarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstudiantesPrimerCarrera
        fields = '__all__'

    def to_representation(self, instance):
        return{
            'id': instance.id,
            'id_estudiante': instance.relacion_estudiante.id if instance.relacion_estudiante.id is not None else '',
            'dni_estudiante': instance.relacion_estudiante.dni_estudiante if instance.relacion_estudiante.dni_estudiante is not None else '',
            'id_carrera': instance.relacion_carrera.id if instance.relacion_carrera.id is not None else '',
            'carrera': instance.relacion_carrera.nombre_carrera if instance.relacion_carrera.nombre_carrera is not None else '',
            'id_inscripcion': instance.relacion_inscripcion.id if instance.relacion_inscripcion.id is not None else '',
            'fecha_inscripcion': instance.relacion_inscripcion.fecha_inscripcion if instance.relacion_inscripcion.fecha_inscripcion is not None else ''
        }


class EstudiantesSegundaCarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstudiantesSegundaCarrera
        fields = '__all__'

    def to_representation(self, instance):
        return{
            'id': instance.id,
            'id_estudiante': instance.relacion_estudiante.id if instance.relacion_estudiante.id is not None else '',
            'dni_estudiante': instance.relacion_estudiante.dni_estudiante if instance.relacion_estudiante.dni_estudiante is not None else '',
            'id_carrera': instance.relacion_carrera.id if instance.relacion_carrera.id is not None else '',
            'carrera': instance.relacion_carrera.nombre_carrera if instance.relacion_carrera.nombre_carrera is not None else '',
            'id_inscripcion': instance.relacion_inscripcion.id if instance.relacion_inscripcion.id is not None else '',
            'fecha_inscripcion': instance.relacion_inscripcion.fecha_inscripcion if instance.relacion_inscripcion.fecha_inscripcion is not None else ''
        }


class EstudianteInscripcionesCompletasSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstudiantesInscripcionesCompletas
        fields = '__all__'

    def to_representation(self, instance):
        return{
            'id': instance.id,
            'id_relacion_primer_carrera': instance.relacion_primer_carrera.id if instance.relacion_primer_carrera.id is not None else '',
            'id_relacion_segunda_carrera': instance.relacion_segunda_carrera.id if instance.relacion_segunda_carrera.id is not None else '',
        }
