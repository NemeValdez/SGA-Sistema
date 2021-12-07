import os
from apialumnos import settings
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'apialumnos.settings.py')

application = get_wsgi_application()
