# Generated by Django 4.0.4 on 2022-07-01 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('rut', models.IntegerField(primary_key=True, serialize=False)),
                ('dv', models.CharField(max_length=1)),
                ('suscripcion', models.BooleanField(default=False)),
            ],
        ),
    ]