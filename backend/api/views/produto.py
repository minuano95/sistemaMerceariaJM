from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from produtos.models import Produto
from ..serializers import ProdutoSerializer

# class ListProdutos(APIView):
#     def get(self, request):
#         produtos = Produto.objects.all()
#         print(produtos)
#         serializer = ProdutoSerializer(produtos, many=True)
#         return Response(serializer.data)


@api_view(['get'])
def produtos_api_list(request):
    produtos = Produto.objects.all()
    serializer = ProdutoSerializer(produtos, many=True)
    return Response(serializer.data)

