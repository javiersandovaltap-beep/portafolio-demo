#!/usr/bin/env bash
# build.sh — Script de construcción para Render

set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
#!/usr/bin/env bash
# build.sh — Script de construcción para Render

set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

# Cargar datos iniciales solo si la base está vacía
if [ -z "$(python manage.py shell -c \"from cv.models import Perfil; print(Perfil.objects.count())\" | grep -v 0)" ]; then
    python manage.py loaddata fixtures/data.json
    echo "✅ Datos iniciales cargados"
else
    echo "✅ Base de datos ya tiene datos"
fi
