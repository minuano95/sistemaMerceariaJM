from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from produtos.models import Produto, Categoria
from ..serializers import ProdutoSerializer, CategoriaSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status

# class ListProdutos(APIView):
#     def get(self, request):
#         produtos = Produto.objects.all()
#         print(produtos)
#         serializer = ProdutoSerializer(produtos, many=True)
#         return Response(serializer.data)


@api_view(['get'])
def produtos_api_list(request):
    produtos = Produto.objects.filter(situacao="ATIVO")
    serializer = ProdutoSerializer(produtos, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['get'])
def produto_api_detail(request, id):
    # produto = get_object_or_404(Produto.objects.filter(pk=id, situacao='ATIVO'))
    # # print(produto)
    # serializer = ProdutoSerializer(instance=produto)
    # return Response(serializer.data)
    
    produto = Produto.objects.filter(pk=id, situacao='ATIVO').first()
    
    if produto:
        serializer = ProdutoSerializer(produto)
        return Response(serializer.data)
    else:
        return Response({
            'detail': 'Mensagem de erro personalizada'
        }, status=status.HTTP_404_NOT_FOUND)


@api_view(['get'])
def produto_categoria_api_detail(request, pk):
    categoria = get_object_or_404(
        Categoria,
        pk=pk
    )
    
    serializer = CategoriaSerializer(categoria)
    
    return Response(serializer.data)
