from rest_framework import serializers
from clientes.models import Cliente
from phonenumber_field.modelfields import PhoneNumberField 
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator, BaseValidator
from phonenumber_field.phonenumber import to_python

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    nome = serializers.CharField(max_length=100, error_messages={'required': 'O campo nome é obrigatório.'})
    cpf = serializers.CharField(max_length=11, error_messages={'required': 'O campo CPF é obrigatório.'})
    telefone = serializers.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'\d{10,11}$',
                message='Formato: 11 99999-9999'
            ),
            MaxLengthValidator(
                limit_value=11,
                message='O campo telefone não pode ter mais que 11 caracteres.'
            )
        ], error_messages={'required': 'O campo telefone é obrigatório.'})
    endereco = serializers.CharField(max_length=150, error_messages={'required': 'O campo endereço é obrigatório.'})
    
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'telefone', 'endereco', 'divida']
        
    def validate(self, attrs):
        if 'divida' not in attrs:
            attrs['divida'] = 0.00
            
        return attrs
    
    def create(self, validate_data):    
        print(self.data)
        print(validate_data)
        print('='*30)
        print(validate_data, type(validate_data), validate_data.keys())
        print('='*30)
        return Cliente.objects.create(**validate_data)
        