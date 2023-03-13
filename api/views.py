from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def convert_binary(request):
    binary = request.data.get('binary')
    base = request.data.get('base')

    decimal = int(binary, 2)
    if base == 'hex':
        result = hex(decimal).split('x')[-1]
    elif base == 'oct':
        result = oct(decimal).split('o')[-1]
    else:
        result = decimal

    return Response({'result': result}, status=status.HTTP_200_OK)

# def binary_converter(request):
#     return render(request, 'index.html')