from rest_framework.routers import DefaultRouter
from app.inscripciones.views import InstitutosCarrerasViewSet, EstudiantesPrimerCarreraViewSet, EstudianteSegundaCarreraViewSet, BuscarInscripcionView

routers = DefaultRouter()
routers.register(r'carrera-instituto', InstitutosCarrerasViewSet,
                 basename='carrerasInstitutos')
routers.register(r'primera-preinscripcion',
                 EstudiantesPrimerCarreraViewSet, basename='inscripcionCarreraUno')
routers.register(r'segunda-preinscripcion',
                 EstudianteSegundaCarreraViewSet, basename='inscripcionCarreraDos')
routers.register(r'buscar-preinscripcion',
                 BuscarInscripcionView, basename='buscarInscripcion')
urlpatterns = routers.urls
