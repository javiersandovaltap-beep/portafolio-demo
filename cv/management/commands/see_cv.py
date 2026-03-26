from django.core.management.base import BaseCommand
from cv.models import Perfil

class Command(BaseCommand):
    help = 'Puebla el CV con información inicial'

    def handle(self, *args, **kwargs):
        perfil, created = Perfil.objects.get_or_create(
            nombre="Javier Sandoval",
            defaults={'profesion': 'Fullstack Developer', 'bio': 'Estudiante de Python/Django'}
        )
        if created:
            self.stdout.write(self.style.SUCCESS('¡CV poblado con éxito!'))
        else:
            self.stdout.write(self.style.WARNING('El CV ya tiene datos.'))
