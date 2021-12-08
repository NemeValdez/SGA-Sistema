from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from app.inscripciones.filters import InscripcionFilter
from app.inscripciones.models import InstitutosCarreras, EstudiantesPrimerCarrera, EstudiantesSegundaCarrera, EstudiantesInscripcionesCompletas
from app.inscripciones.serializers import InstitutosCarrerasSerializer, EstudiantesPrimerCarreraSerializer, EstudiantesSegundaCarreraSerializer, EstudianteInscripcionesCompletasSerializer


class InstitutosCarrerasViewSet(viewsets.ModelViewSet):
    '''Vista que gestiona el CRUD de la relación entre Institutos y Carreras'''
    serializer_class = InstitutosCarrerasSerializer
    permission_classes = (IsAuthenticated,)
    queryset = InstitutosCarrerasSerializer.Meta.model.objects.all()


class EstudiantesPrimerCarreraViewSet(viewsets.ModelViewSet):
    '''Vista que gestiona el CRUD de la inscripción del estudiante a la primer carrera'''
    serializer_class = EstudiantesPrimerCarreraSerializer
    queryset = EstudiantesPrimerCarreraSerializer.Meta.model.objects.all()


class EstudianteSegundaCarreraViewSet(viewsets.ModelViewSet):
    '''Vista que gestiona el CRUD de la inscripción del estudiante a la segunda carrera'''
    serializer_class = EstudiantesSegundaCarreraSerializer
    queryset = EstudiantesSegundaCarreraSerializer.Meta.model.objects.all()


class BuscarInscripcionView(viewsets.ReadOnlyModelViewSet):
    queryset = EstudianteInscripcionesCompletasSerializer.Meta.model.objects.all()
    serializer_class = EstudianteInscripcionesCompletasSerializer
    filter_class = InscripcionFilter
    search_fields = ('=id',)
