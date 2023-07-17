from django.db import models
from django.contrib.auth.models import User, Permission
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType


AUTO_MARCA = [
    ('TOYOTA', 'Toyota'),
    ('CHEVROLET', 'Chevrolet'),
    ('FIAT', 'Fiat'),
    ('FORD', 'Ford'),
]

AUTO_CATEGORIA = [
    ('PARTICULAR', 'Particular'),
    ('TRANSPORTE', 'Transporte'),
    ('CARGA', 'Carga'),
]


class Auto(models.Model):
    marca = models.CharField(max_length=20, choices=AUTO_MARCA, default='FORD')
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    categoria = models.CharField(
        max_length=20, choices=AUTO_CATEGORIA, default='PARTICULAR')
    precio = models.IntegerField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.marca} - {self.modelo}'

    def get_condicion_precio(self):
        if self.precio <= 10000:
            return "Bajo"
        elif 10000 < self.precio <= 30000:
            return "Medio"
        else:
            return "Alto"


@receiver(post_save, sender=User)
def assign_visualizar_catalogo_permission(sender, instance, created, **kwargs):
    if created:
        permission = Permission.objects.get(codename='visualizar_catalogo')
        instance.user_permissions.add(permission)


@receiver(post_save, sender=User)
def assign_add_perm(sender, instance, created, **kwargs):
    if created:
        content_type = ContentType.objects.get_for_model(Auto)
        permission = Permission.objects.get(
            content_type=content_type, codename='add_auto')
        instance.user_permissions.add(permission)
