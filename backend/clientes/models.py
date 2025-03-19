from django.db import models
from phonenumber_field.modelfields import PhoneNumberField 


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    telefone = PhoneNumberField(region='BR')
    endereco = models.CharField(max_length=250)
    divida = models.DecimalField(
        null=True,
        max_digits=10,
        decimal_places=2,        
    )
    
    def __str__(self): 
        return f'{self.id} - {self.nome}'