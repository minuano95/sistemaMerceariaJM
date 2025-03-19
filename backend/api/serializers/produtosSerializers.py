from rest_framework import serializers
from django.core.exceptions import ValidationError
from produtos.models import Produto

class ProdutoSerializer(serializers.ModelSerializer):
    codigo = serializers.IntegerField(error_messages={'required': 'O campo código é obrigatório'})
    nome = serializers.CharField(error_messages={'required': 'O campo nome é obrigatório'})
    
    class Meta:
        model = Produto
        fields = ['codigo', 'nome', 'preco_custo', 'preco_venda', 'estoque', 'categoria', 'situacao', 'desconto', 'data_atualizacao']
        read_only_fields = ['data_atualizacao',]
        
        
    