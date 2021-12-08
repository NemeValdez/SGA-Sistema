from rest_framework.routers import DefaultRouter
from app.carreras.views import TurnosCarrerasViewSet, CarrerasViewSet, LimitacionesCarrerasViewSet

routers = DefaultRouter()
routers.register(r'turno', TurnosCarrerasViewSet,
                 basename='turnoCarreras')
routers.register(r'carrera', CarrerasViewSet,
                 basename='carreras')
routers.register(r'limites', LimitacionesCarrerasViewSet,
                 basename='limitesCarreras')

urlpatterns = routers.urls
