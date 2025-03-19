from django.urls import path
from .views import ListClientes, CreateClientes, ClienteDetailView, produtos_api_list

app_name = 'api'

urlpatterns = [
    path('clientes/', ListClientes.as_view(), name='clientes-list'),
    path('clientes/add/', CreateClientes.as_view(), name='clientes-list'),
    path('clientes/<int:id>/', ClienteDetailView.as_view(), name='clientes-detail'),
    path('clientes/delete/<int:id>/', ClienteDetailView.as_view(), name='clientes-detail-delete'),

    path('produtos/', produtos_api_list, name='produtos-list'),
    # path('produtos/', ListProdutos.as_view(), name='produtos-list'),
    
    # path('produtos/', CreateClientes.as_view(), name='clientes-create'),
]
