from django.urls import path
from .views import ListClientes, CreateClientes, ClienteDetailView, produtos_api_list, produto_api_detail, produto_categoria_api_detail

app_name = 'api'

urlpatterns = [
    path('clientes/', ListClientes.as_view(), name='clientes-list'),
    path('clientes/add/', CreateClientes.as_view(), name='clientes-list'),
    path('clientes/<int:id>/', ClienteDetailView.as_view(), name='clientes-detail'),
    path('clientes/delete/<int:id>/', ClienteDetailView.as_view(), name='clientes-detail-delete'),

    path('produtos/', produtos_api_list, name='produtos-list'),
    path('produtos/<int:id>/', produto_api_detail, name='produto-detail'),
    path('categoria/<int:pk>/', produto_categoria_api_detail, name='produto-categoria'),
    # path('produtos/', ListProdutos.as_view(), name='produtos-list'),
    
    # path('produtos/', CreateClientes.as_view(), name='clientes-create'),
]
