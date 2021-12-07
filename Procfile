release: python apialumnos/manage.py makemigrations --no-input
release: python apialumnos/manage.py migrate --no-input
web: gunicorn apialumnos:apialumnos.wsgi --log-file - --log-level debug
python apialumnos/manage.py collectstatic --noinput
apialumnos/manage.py migrate