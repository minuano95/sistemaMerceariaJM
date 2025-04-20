from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from clientes.models import Cliente
from django.shortcuts import redirect
from ..serializers import ClienteSerializer

class ListClientes(APIView):
    
    def get(self, reqeuest):
        clientes = Cliente.objects.all()
        serializers = ClienteSerializer(clientes, many=True)
        print(serializers.data)
        return Response(serializers.data)

    
    
class CreateClientes(APIView):
    def post(self, request, format=None):

        serializer = ClienteSerializer(data=request.data)        

        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data)
        
        else:
            return Response(serializer.errors, status=300)
    

    
class ClienteDetailView(APIView):
    def get(self, request, id):
        try:
            cliente = Cliente.objects.get(id=id)
            serializer = ClienteSerializer(cliente)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response(status=404)
        
    def delete(self, request, id):
        try:
            cliente = Cliente.objects.get(id=id)
            cliente.delete()
            return Response(status=204)
        except ObjectDoesNotExist:
            return Response(status=404)
