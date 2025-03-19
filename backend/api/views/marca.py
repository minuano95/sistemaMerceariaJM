from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.views import APIView 
from produtos.models import Marca
from ..serializers import MarcaSerializer

class ListMarcas(APIView):
    def get(self, request):
        marcas = Marca.objects.all()
        serializers = MarcaSerializer(marcas, many=True)