from rest_framework.routers import DefaultRouter
from app.estudiantes.views import EstudiantesEstablecimientosViewSet, EstudiantesViewSet, BuscarDNIView

routers = DefaultRouter()
routers.register(r'escuela', EstudiantesEstablecimientosViewSet,
                 basename='Secundario de donde proviene el estudiante')
routers.register(r'estudiante', EstudiantesViewSet,
                 basename='Datos del estudiante')
routers.register(r'buscar-dni', BuscarDNIView, basename='dni')
urlpatterns = routers.urls
