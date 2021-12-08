from rest_framework.routers import DefaultRouter
from app.estudiantes.views import EstudiantesViewSet, BuscarDNIView

routers = DefaultRouter()
routers.register(r'estudiante', EstudiantesViewSet,
                 basename='estudiante')
routers.register(r'buscar-dni', BuscarDNIView, basename='buscarDNI')
urlpatterns = routers.urls
