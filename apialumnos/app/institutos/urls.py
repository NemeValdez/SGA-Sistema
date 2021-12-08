from rest_framework.routers import DefaultRouter
from app.institutos.views import InstitutosViewSet, SedesInstitutosViewSet, RolesJerarquicosViewSet, JerarquicosViewSet, JerarquicosInstitutosViewSet


routers = DefaultRouter()
routers.register(r'instituto', InstitutosViewSet,
                 basename='institutos')
routers.register(r'sede', SedesInstitutosViewSet,
                 basename='sedesInstitutos')
routers.register(r'cargo', RolesJerarquicosViewSet,
                 basename='cargosInstitutos')
routers.register(r'jerarquico', JerarquicosViewSet,
                 basename='personasAcceso')
routers.register(r'jerarquico-instituto',
                 JerarquicosInstitutosViewSet, basename='jerarquicoInstituto')

urlpatterns = routers.urls
