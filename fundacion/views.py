from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import PersonaSerializer
from .models import Persona
# Create your views here.

@csrf_exempt
@api_view(['POST'])
def insertar_dato(request):
    if request.method == 'POST':
        serializer = PersonaSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status = status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status = status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
    else:
        return Response(status = status.HTTP_402_PAYMENT_REQUIRED)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def personas(request, id):
    try:
        persona = Persona.objects.get(rut=id)
    except Persona.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = PersonaSerializer(persona)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PersonaSerializer(persona, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        persona.delete()
        return Response(status=status.HTTP_200_OK)

@api_view(['GET', 'PUT'])
def esta_suscrito(request, id):
    try:
        persona = Persona.objects.get(id_producto=id)
    except Persona.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        return JsonResponse({'estado': persona.suscripcion})
    elif request.method == 'PUT':
        persona.suscripcion = not persona.suscripcion
        persona.save()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

