from rest_framework.routers import DefaultRouter
from app.carreras.views import TurnosCarrerasViewSet, CarrerasViewSet, LimitacionesCarrerasViewSet

routers = DefaultRouter()
routers.register(r'turno/', TurnosCarrerasViewSet,
                 basename='Turnos de las Carreras')
routers.register(r'carrera/', CarrerasViewSet,
                 basename='Datos de las Carreras')
routers.register(r'limites/', LimitacionesCarrerasViewSet,
                 basename='Limites que corresponden a determinada Carrera')

urlpatterns = routers.urls
