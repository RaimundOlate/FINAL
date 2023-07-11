from django.contrib.auth.management.commands.createsuperuser import Command as BaseCommand
from django.contrib.auth.models import Permission


class Command(BaseCommand):
    help = 'Crea un superusuario con el permiso "visualizar_catalogo"'

    def handle(self, *args, **options):
        super().handle(*args, **options)
        permission = Permission.objects.get(codename='visualizar_catalogo')
        self.user.user_permissions.add(permission)
