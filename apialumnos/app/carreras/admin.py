from django.contrib import admin
from app.carreras.models import TurnosCarreras, Carreras, LimitacionesCarreras

admin.site.register(TurnosCarreras)
admin.site.register(Carreras)
admin.site.register(LimitacionesCarreras)
