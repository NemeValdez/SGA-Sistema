from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from app.users.login.ingresar import Ingresar
from app.users.login.salir import Salir


schema_view = get_schema_view(
    openapi.Info(
        title="Gestión de Alumnos API",
        default_version='v1',
        description="API de Sistema para la PreInscripción de Estudiantes para el nivel terciario de la Provincia de Buenos Aires, Argentina",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="carnevali.damian@gmail.com"),
        license=openapi.License(name="ALUF License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', include('admin_honeypot.urls')),
    path('sga-panel/', admin.site.urls),

    path('usuarios/', include('app.users.urls')),
    path('institutos/', include('app.institutos.urls')),
    path('inscripciones/', include('app.inscripciones.urls')),
    path('estudiantes/', include('app.estudiantes.urls')),
    path('carreras/', include('app.carreras.urls')),

    path('obtener-token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refrescar-token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('ingresar/', Ingresar.as_view(), name='Ingresar'),
    path('salir/', Salir.as_view(), name='Salir'),
    path('ruteos/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
]
