#!/usr/bin/env bash
# build.sh — Script de construcción para Render

set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
