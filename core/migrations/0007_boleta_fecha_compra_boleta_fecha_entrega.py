# Generated by Django 4.0.4 on 2022-06-30 08:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_usuario_suscripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='boleta',
            name='fecha_compra',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='boleta',
            name='fecha_entrega',
            field=models.DateField(blank=True, null=True),
        ),
    ]
