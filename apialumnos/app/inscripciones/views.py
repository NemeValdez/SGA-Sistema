from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from app.inscripciones.filters import Inscripcion1Filter, Inscripcion2Filter
from app.inscripciones.models import InstitutosCarreras, Inscripciones, EstudiantesPrimerCarrera, EstudiantesSegundaCarrera
from app.inscripciones.serializers import InstitutosCarrerasSerializer, InscripcionesSerializer, EstudiantesPrimerCarreraSerializer, EstudiantesSegundaCarreraSerializer


class InstitutosCarrerasViewSet(viewsets.ModelViewSet):
    '''Vista que gestiona el CRUD de la relación entre Institutos y Carreras'''
    serializer_class = InstitutosCarrerasSerializer
    permission_classes = (IsAuthenticated,)
    queryset = InstitutosCarrerasSerializer.Meta.model.objects.all()


class InscripcionesViewSet(viewsets.ModelViewSet):
    '''Vista que gestiona el CRUD de los datos de la preinscripción'''
    serializer_class = InscripcionesSerializer
    queryset = InscripcionesSerializer.Meta.model.objects.all()


class EstudiantesPrimerCarreraViewSet(viewsets.ModelViewSet):
    '''Vista que gestiona el CRUD de la inscripción del estudiante a la primer carrera'''
    serializer_class = EstudiantesPrimerCarreraSerializer
    queryset = EstudiantesPrimerCarreraSerializer.Meta.model.objects.all()


class EstudianteSegundaCarreraViewSet(viewsets.ModelViewSet):
    '''Vista que gestiona el CRUD de la inscripción del estudiante a la segunda carrera'''
    serializer_class = EstudiantesSegundaCarreraSerializer
    queryset = EstudiantesSegundaCarreraSerializer.Meta.model.objects.all()


class BuscarInscripcion1View(viewsets.ReadOnlyModelViewSet):
    queryset = EstudiantesPrimerCarreraSerializer.Meta.model.objects.all()
    serializer_class = EstudiantesPrimerCarreraSerializer
    filter_class = Inscripcion1Filter
    search_fields = ('=relacion_estudiante',)


class BuscarInscripcion2View(viewsets.ReadOnlyModelViewSet):
    queryset = EstudiantesPrimerCarreraSerializer.Meta.model.objects.all()
    serializer_class = EstudiantesPrimerCarreraSerializer
    filter_class = Inscripcion2Filter
    search_fields = ('=relacion_estudiante',)
