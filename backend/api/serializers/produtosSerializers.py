from rest_framework import serializers
# from django.core.exceptions import ValidationError
from produtos.models import Produto
from produtos.models import Categoria


#-------------------------------------------------
# Aula 284
# Craindo um serializer específico para a categoria
class CategoriaSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nome = serializers.CharField(max_length=165)
#-------------------------------------------------


# class ProdutoSerializer(serializers.Serializer):
#     codigo = serializers.IntegerField()
#     nome = serializers.CharField(max_length=65)
#     preco_custo = serializers.FloatField()
    
    # #-------------------------------------------------
    # # Aula 283 - Renomeando e Juntando campos
    
    # ainda_ativo = serializers.BooleanField(source='ativo')
    
    # nome_codigo = serializers.SerializerMethodField()
    # def get_nome_codigo(self, produto):
    #     return f'{produto.nome} | {produto.codigo}'
    
    # novo_campo_nome_e_codigo = serializers.SerializerMethodField(method_name='nome_codigo')
    # def nome_codigo(self, produto):
    #     return f'{produto.nome} | {produto.codigo}'
    # #-------------------------------------------------
    
    #-------------------------------------------------
    # Aula 284 - Campos Relacionados
    # from produtos.models import Categoria
    
    # Vai mostrar o ID
    # categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all())
    # status = serializers.FieldDoesNotExist()
    
    # # Juntando a alteração de nome com o campo relacional
    # marca = serializers.PrimaryKeyRelatedField(source='categoria', queryset=Categoria)

    # Mostando a string (__str__) do model ao invés do id
    # categoria_nome = serializers.StringRelatedField(source='categoria')
    
    # Mostrando o objeto inteiro como um campo da api
    # categoria_objeto = CategoriaSerializer(source='categoria')
    #-------------------------------------------------
    
    
    #-------------------------------------------------
    # Aula 285 - HyperlinkedRelatedField
    # ForeignKey como link
    # Transforma uma chave estrangeira em um link para ser acessado diretamente. 
    # categoria_links = serializers.HyperlinkedRelatedField(
    #     source='categoria', # Model
    #     queryset=Categoria.objects.all(), # Pesquisa
    #     view_name='api:produto-categoria', # ViewName
    # )
    #-------------------------------------------------
    
    # estoque = serializers.IntegerField()
    # situacao = serializers.BooleanField()
    # desconto = serializers.FloatField()



#-------------------------------------------------
# Aula 286 - Migrando para o ModelSerializer
class ProdutoSerializer(serializers.ModelSerializer):
    categoria_link = serializers.HyperlinkedRelatedField(
        source='categoria',
        # queryset=Categoria.objects.all(),
        # many=True,
        read_only=True,
        view_name='api:produto-categoria',
    )
        
    class Meta: # Onde é definido o model que ele usa e os campos que vai trazer
        model = Produto
        fields = ['codigo', 'nome', 'estoque', 'categoria', 'categoria_link']
    
    
    
#     codigo = serializers.IntegerField(error_messages={'required': 'O campo código é obrigatório'})
#     nome = serializers.CharField(error_messages={'required': 'O campo nome é obrigatório'})
    
#     class Meta:
#         model = Produto
#         fields = ['codigo', 'nome', 'preco_custo', 'estoque', 'categoria', 'situacao', 'desconto', 'data_atualizacao']
#         read_only_fields = ['data_atualizacao',]
        
        
    