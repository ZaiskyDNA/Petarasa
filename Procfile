release: python3 manage.py collectstatic --noinput && python3 manage.py migrate
web: gunicorn petarasa_project.wsgi --log-file -
