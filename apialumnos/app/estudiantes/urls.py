from rest_framework.routers import DefaultRouter
from app.estudiantes.views import EstudiantesEstablecimientosViewSet, EstudiantesViewSet, DNIViewset

routers = DefaultRouter()
routers.register(r'escuela', EstudiantesEstablecimientosViewSet,
                 basename='Secundario de donde proviene el estudiante')
routers.register(r'estudiante', EstudiantesViewSet,
                 basename='Datos del estudiante')
routers.register(r'buscar-dni', DNIViewset, basename='DNI')
urlpatterns = routers.urls
