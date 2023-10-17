from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from django.core.serializers import serialize
from api.models import Address
from api.serializers import AddressSerializer
import json
# Create your views here.

@api_view(['POST'])
def register_address(request):
    if request.method == 'GET':
        raise APIException(403, 'Sem acesso get')
    
    serializer = AddressSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    
    return Response("Invalid")

@api_view(["GET"])
def get_all_address(request):
    address = Address.objects.all()
    serializer = AddressSerializer(address, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def get_location(request):

    data = request.data

    position_x = data['x']
    position_y = data['y']

    d_max = abs(position_x - position_y)

    address = Address.objects.all()
    serializer = AddressSerializer(address, many=True)
    serializer = serializer.data

    lista_resultado = []
    
    for objeto in serializer:
        lista = [objeto['name']]
        x = abs(objeto['x'] - position_x)
        y =abs(objeto['y'] - position_y)
        soma_x_y = x + y
        if soma_x_y <= d_max:
            lista_resultado.append(lista)
   
    return Response(f'{lista_resultado}')