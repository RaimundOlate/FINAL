# Generated by Django 4.0.5 on 2023-07-10 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(choices=[('TOYOTA', 'Toyota'), ('CHEVROLET', 'Chevrolet'), ('FIAT', 'Fiat'), ('FORD', 'Ford')], default='FORD', max_length=20)),
                ('modelo', models.CharField(max_length=100)),
                ('serial_carroceria', models.CharField(max_length=50)),
                ('serial_motor', models.CharField(max_length=50)),
                ('categoria', models.CharField(choices=[('PARTICULAR', 'Particular'), ('TRANSPORTE', 'Transporte'), ('CARGA', 'Carga')], default='PARTICULAR', max_length=20)),
                ('precio', models.IntegerField(blank=True, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]