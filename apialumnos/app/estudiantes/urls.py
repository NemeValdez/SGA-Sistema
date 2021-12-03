from rest_framework.routers import SimpleRouter
from django.urls import path, include

from app.estudiantes.views import EstudiantesEstablecimientosViewSet, EstudiantesViewSet

routers = SimpleRouter()
routers.register(r'escuela', EstudiantesEstablecimientosViewSet,
                 basename='Secundario de donde proviene el estudiante')
router.register(r'estudiante', EstudiantesViewSet,
                basename='Datos del estudiante')
urlpatterns = routers.urls
