from rest_framework.routers import DefaultRouter
from app.estudiantes.views import EstudiantesViewSet, BuscarDNIView

routers = DefaultRouter()
routers.register(r'estudiante', EstudiantesViewSet,
                 basename='Datos del estudiante')
routers.register(r'buscar-dni', BuscarDNIView, basename='dni')
urlpatterns = routers.urls
