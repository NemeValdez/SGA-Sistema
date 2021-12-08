from rest_framework.routers import DefaultRouter
from app.inscripciones.views import InstitutosCarrerasViewSet, InscripcionesViewSet, EstudiantesPrimerCarreraViewSet, EstudianteSegundaCarreraViewSet, BuscarInscripcionView

routers = DefaultRouter()
routers.register(r'carrera-instituto', InstitutosCarrerasViewSet,
                 basename='Relación entre las carreras de un instituto')
routers.register(r'inscripcion', InscripcionesViewSet,
                 basename='Datos de la preinscripción')
routers.register(r'primera-preinscripcion',
                 EstudiantesPrimerCarreraViewSet, basename='Inscripción a la primer carrera')
routers.register(r'segunda-preinscripcion',
                 EstudianteSegundaCarreraViewSet, basename='Inscripción a la segunda carrera')
routers.register(r'buscar-preinscripcion',
                 BuscarInscripcionView, basename='inscripcion')
urlpatterns = routers.urls
