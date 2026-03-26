#!/usr/bin/env bash
# build.sh — Script de construcción para Render

set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

# Cargar fixtures solo si no hay datos
python manage.py shell <<EOF
from cv.models import Perfil
if Perfil.objects.count() == 0:
    print("Cargando fixtures...")
    from django.core import management
    management.call_command('loaddata', 'fixtures/data.json')
    print("Fixtures cargados!")
else:
    print("Datos ya existen")
EOF
