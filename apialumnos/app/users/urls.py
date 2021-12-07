from rest_framework.routers import DefaultRouter
from app.users.views import UsuarioViewSet

routers = DefaultRouter()
routers.register(r'Usuarios/', UsuarioViewSet, basename='Usuarios')

urlpatterns = routers.urls
