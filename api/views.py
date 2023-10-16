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

def tratamento(data_x, data_y, point_x, point_y):
    data_x = data_x
    data_y = data_y
    point_x = point_x
    point_y = point_y
    dmax = point_x - point_y
    dist_x = data_x - point_x
    dist_y = data_y - point_y
    sum_dist = dist_x + dist_y
    if sum_dist <= dmax:
        print("passou")
    else:
        print("não passou")

@api_view(['POST'])
def verify(request):
    if request.method == "GET":
        raise APIException('Não tem permissões para GET', 500)
    pass