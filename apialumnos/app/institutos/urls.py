from rest_framework.routers import DefaultRouter
from app.institutos.views import InstitutosViewSet, SedesInstitutosViewSet, RolesJerarquicosViewSet, JerarquicosViewSet


routers = DefaultRouter()
routers.register(r'instituto', InstitutosViewSet,
                 basename='Datos del Instituto')
routers.register(r'sede', SedesInstitutosViewSet,
                 basename='Datos de la Sede del Instituto')
routers.register(r'cargo', RolesJerarquicosViewSet,
                 basename='Roles dentro de los Institutos')
routers.register(r'jerarquico', JerarquicosViewSet,
                 basename='Personas con acceso al sistema')

urlpatterns = routers.urls
