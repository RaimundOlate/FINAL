from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Permission

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


@receiver(post_save, sender=User)
def assign_visualizar_catalogo_permission(sender, instance, created, **kwargs):
    if created:
        permission = Permission.objects.get(codename='visualizar_catalogo')
        instance.user_permissions.add(permission)
