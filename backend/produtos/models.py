from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome


class Produto(models.Model):
    # def get_produto(self):
        
    
    codigo = models.BigIntegerField(unique=True)
    nome = models.CharField(max_length=100)
    preco_custo = models.DecimalField(max_digits=7, decimal_places=2)
    preco_venda = models.DecimalField(max_digits=7, decimal_places=2)
    estoque = models.IntegerField()
    data_cadastro = models.DateField(auto_now_add=True)
    data_atualizacao = models.DateField(auto_now=True)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    promocao = models.BooleanField(default=False)
    situacao = models.CharField(max_length=20, choices=[('ATIVO', 'Ativo'), ('INATIVO', 'Inativo')])
    desconto = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    
    def __str__(self):
        return f'{self.codigo} {self.nome}'