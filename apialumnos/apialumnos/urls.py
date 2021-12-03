from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


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
    path('admin/', admin.site.urls),

    path('usuarios/', include('app.users.urls')),
    path('login/', include('app.login.urls')),
    path('institutos/', include('app.institutos.urls')),
    path('inscripciones/', include('app.inscripciones.urls')),
    path('estudiantes/', include('app.estudiantes.urls')),
    path('carreras/', include('app.carreras.urls')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('ruteos/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
]
