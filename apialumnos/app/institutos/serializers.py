from rest_framework import serializers
from app.institutos.models import Institutos, SedesInstitutos, RolesJerarquicos, Jerarquicos, InstitutosJerarquicos


class InstitutosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Institutos
        fields = '__all__'


class SedesInstitutosSerializers(serializers.ModelSerializer):
    class Meta:
        model = SedesInstitutos
        fields = '__all__'

    def to_representation(self, instance):
        return{
            'id': instance.id,
            'nombre_sede_instituto': instance.nombre_sede_instituto,
            'calle_sede_instituto': instance.calle_sede_instituto,
            'altura_sede_instituto': instance.altura_sede_instituto,
            'id_instituto': instance.relacion_instituto_sede.id,
            'numero_instituto': instance.relacion_instituto_sede.numero_instituto,
            'calle_instituto': instance.relacion_instituto_sede.calle_instituto,
            'altura_instituto': instance.relacion_instituto_sede.altura_instituto,
            'mail_general_instituto': instance.relacion_instituto_sede.mail_general_instituto,
            'mail_preinscripcion_instituto': instance.relacion_instituto_sede.mail_preinscripcion_instituto,
            'telefono_instituto': instance.relacion_instituto_sede.telefono_instituto,
            'sitio_web_instituto': instance.relacion_instituto_sede.sitio_web_instituto,
        }


class RolesJerarquicosSerializers(serializers.ModelSerializer):
    class Meta:
        model = RolesJerarquicos
        fields = '__all__'


class JerarquicosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Jerarquicos
        fields = '__all__'

    def to_representation(self, instance):
        return{
            'id': instance.id,
            'nombre_jerarquico': instance.nombre_jerarquico,
            'apellido_jerarquico': instance.apellido_jerarquico,
            'sexo_jerarquico': instance.sexo_jerarquico,
            'fecha_nacimiento_jerarquico': instance.fecha_nacimiento_jerarquico,
            'id_cargo': instance.relacion_rol_jerarquico.id if instance.relacion_rol_jerarquico.id is not None else '',
            'cargo': instance.relacion_rol_jerarquico.nombre_rol if instance.relacion_rol_jerarquico.nombre_rol is not None else '',
            'id_instituto': instance.relacion_instituto.id if instance.relacion_instituto.id is not None else '',
            'instituto': instance.relacion_instituto.numero_instituto if instance.relacion_instituto.numero_instituto is not None else'',
        }
