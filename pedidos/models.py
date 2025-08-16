from django.db import models
from django.contrib.auth.models import User

# O modelo Cliente irá complementar o modelo de usuário padrão do Django
class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    endereco = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    cep = models.CharField(max_length=10)

    @property
    def nome_de_exibicao(self):
        return self.user.email.split('@')[0] if self.user.email else self.user.username

    def __str__(self):
        return self.user.username

class Documento(models.Model):
    # Escolhas de layout e páginas por folha
    LAYOUT_CHOICES = [
        ('Retrato', 'Retrato'),
        ('Paisagem', 'Paisagem'),
    ]
    PAGINAS_POR_FOLHA_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('4', '4'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    arquivo = models.FileField(upload_to='documentos_upload/')
    nome_arquivo = models.CharField(max_length=255)
    qtd_paginas = models.IntegerField(default=1)
    eh_colorido = models.BooleanField(default=False)
    tipo_papel = models.CharField(max_length=50)
    data_upload = models.DateTimeField(auto_now_add=True)

    num_copias = models.IntegerField(default=1)
    
    # NOVOS CAMPOS
    layout = models.CharField(max_length=10, choices=LAYOUT_CHOICES, default='Retrato')
    imprimir_dois_lados = models.BooleanField(default=False)
    paginas_por_folha = models.CharField(max_length=2, choices=PAGINAS_POR_FOLHA_CHOICES, default='1')

    def __str__(self):
        return self.nome_arquivo
class Pedido(models.Model):
    STATUS_PEDIDO_CHOICES = (
        ('Pendente', 'Pendente'),
        ('Em Impressao', 'Em Impressão'),
        ('Em Entrega', 'Em Entrega'),
        ('Concluido', 'Concluído'),
    )

    STATUS_PAGAMENTO_CHOICES = (
        ('Pendente', 'Pendente'),
        ('Pago', 'Pago'),
        ('Falhou', 'Falhou'),
    )

    # Escolhas de pagamento com base nas suas especificações
    METODO_PAGAMENTO_CHOICES = (
        ('Pix', 'Pix'),
        ('Cartao de Debito', 'Cartão de Débito'),
        ('Cartao de Credito', 'Cartão de Crédito'),
    )
    
    taxa_entrega_adicionada = models.BooleanField(default=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    documentos = models.ManyToManyField(Documento)
    status_pedido = models.CharField(max_length=20, choices=STATUS_PEDIDO_CHOICES, default='Pendente')
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    data_pedido = models.DateTimeField(auto_now_add=True)
    
    # NOVOS CAMPOS PARA PAGAMENTO
    metodo_pagamento = models.CharField(max_length=50, choices=METODO_PAGAMENTO_CHOICES, blank=True, null=True)
    status_pagamento = models.CharField(max_length=20, choices=STATUS_PAGAMENTO_CHOICES, default='Pendente')

    def __str__(self):
        return f"Pedido #{self.id} de {self.cliente.user.username}"