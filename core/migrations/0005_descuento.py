# Generated by Django 4.0.4 on 2022-06-24 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_boleta_estado'),
    ]

    operations = [
        migrations.CreateModel(
            name='descuento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=40, unique=True)),
                ('porcentaje', models.IntegerField()),
            ],
        ),
    ]
