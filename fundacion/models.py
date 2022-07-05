from django.db import models
import requests

# Create your models here.

class Persona(models.Model):
    rut = models.IntegerField(primary_key=True)
    dv = models.CharField(max_length=1)
    suscripcion = models.BooleanField(default=False)