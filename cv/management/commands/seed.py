from django.core.management.base import BaseCommand
from cv.models import Experiencia, Formacion, Proyecto


class Command(BaseCommand):
    help = 'Rellena la base de datos con datos de demostración'

    def handle(self, *args, **kwargs):
        self.stdout.write('Limpiando datos anteriores...')
        Experiencia.objects.all().delete()
        Formacion.objects.all().delete()
        Proyecto.objects.all().delete()

        self.stdout.write('Creando experiencias...')
        Experiencia.objects.create(
            periodo='2023 — Presente',
            puesto='Desarrollador Backend',
            empresa='Soluciones Tech SpA',
            descripcion='Desarrollo y mantenimiento de APIs REST con Django. Integración con bases de datos PostgreSQL y gestión de autenticación de usuarios.',
            tecnologias='Django, Python, PostgreSQL, REST API',
            orden=1,
        )
        Experiencia.objects.create(
            periodo='2022 — 2023',
            puesto='Desarrollador Frontend Junior',
            empresa='Agencia Digital Nexo',
            descripcion='Maquetación de interfaces web con HTML, CSS y Bootstrap. Colaboración en proyectos de e-commerce y sitios corporativos.',
            tecnologias='HTML, CSS, Bootstrap, JavaScript',
            orden=2,
        )

        self.stdout.write('Creando formaciones...')
        Formacion.objects.create(
            periodo='2022',
            titulo='Bootcamp Desarrollo Web Full Stack',
            institucion='SENCE / Academia de Programación',
            descripcion='Programa intensivo de 800 horas. Desarrollo con Python, Django, bases de datos relacionales y despliegue en la nube.',
            orden=1,
        )
        Formacion.objects.create(
            periodo='2020 — 2021',
            titulo='Técnico en Programación',
            institucion='Instituto Profesional',
            descripcion='Fundamentos de programación, lógica computacional, bases de datos y desarrollo de software.',
            orden=2,
        )

        self.stdout.write('Creando proyectos...')
        Proyecto.objects.create(
            titulo='CV Portafolio Web',
            descripcion='Aplicación web desarrollada con Django para gestionar y mostrar un currículum vitae en línea. Incluye panel de administración con control de permisos.',
            tecnologias='Django, Python, Bootstrap, PostgreSQL',
            enlace_github='https://github.com/tuusuario/portafolio',
            enlace_sitio=None,
            orden=1,
        )
        Proyecto.objects.create(
            titulo='Sistema de Contacto',
            descripcion='Módulo de formulario de contacto con validación de datos, protección CSRF y confirmación visual al usuario.',
            tecnologias='Django Forms, HTML, CSS',
            enlace_github=None,
            enlace_sitio=None,
            orden=2,
        )

        self.stdout.write(self.style.SUCCESS('✅ Seed completado exitosamente.'))
