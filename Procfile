release: python apialumnos/manage.py makemigrations --no-input
release: python apialumnos/manage.py migrate --no-input
web: gunicorn apialumnos.wsgi:apialumnos --log-file - --log-level debug