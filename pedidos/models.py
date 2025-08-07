from django.db import models
from django.contrib.auth.models import User

# O modelo Cliente irá complementar o modelo de usuário padrão do Django
class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    endereco = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    cep = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username

class Documento(models.Model):
    # Um documento pertence a um cliente
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    arquivo = models.FileField(upload_to='documentos_upload/')
    nome_arquivo = models.CharField(max_length=255)
    qtd_paginas = models.IntegerField(default=1)
    eh_colorido = models.BooleanField(default=False)
    tipo_papel = models.CharField(max_length=50, default='A4 Sulfite')
    data_upload = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome_arquivo

class Pedido(models.Model):
    # Um pedido tem um status para controle
    STATUS_CHOICES = (
        ('Pendente', 'Pendente'),
        ('Em Impressao', 'Em Impressão'),
        ('Em Entrega', 'Em Entrega'),
        ('Concluido', 'Concluído'),
    )

    # Um pedido pertence a um cliente
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    # Um pedido pode ter vários documentos
    documentos = models.ManyToManyField(Documento)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pendente')
    data_pedido = models.DateTimeField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Pedido #{self.id} de {self.cliente.user.username}"