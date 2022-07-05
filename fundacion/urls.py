from django.urls import path
from .views import *


urlpatterns = [
    path('v1/personas/<id>/', personas, name="persona"),
    path('v1/suscripcion/<id>/', esta_suscrito, name="esta_suscrito"),
    path('v1/insertar-dato/', insertar_dato, name="insertar_dato"),
]