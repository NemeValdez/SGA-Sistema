from rest_framework.routers import DefaultRouter
from app.users.views import UsuarioViewSet

routers = DefaultRouter()
routers.register(r'usuarios', UsuarioViewSet, basename='usuarios')

urlpatterns = routers.urls
