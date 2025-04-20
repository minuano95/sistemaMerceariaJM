from rest_framework import serializers
from produtos.models import Categoria

class categoriaSerializer(serializers.Serializer):
    nome = serializers.CharField(max_length=100)
    