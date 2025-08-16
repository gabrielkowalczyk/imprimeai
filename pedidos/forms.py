from django import forms
from django.contrib.auth.models import User
from .models import Documento, Cliente, Pedido

class RegistroForm(forms.ModelForm):
    # Campo para o nome de usuário (que será o telefone)
    username = forms.CharField(max_length=150, required=True, label='Telefone')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
    email = forms.EmailField(label='Email', required=True) # Adicione esta linha

    class Meta:
        model = User
        fields = ['username', 'email'] # Atualize esta linha com o novo campo

class DocumentoForm(forms.ModelForm):
    # Definindo as opções para o tipo de papel
    TIPO_PAPEL_CHOICES = [
        ('A4 Padrão (75g)', 'A4 Padrão (75g)'),
        ('A4 Robusto (120g)', 'A4 Robusto (120g)'),
        ('A4 Cartolina (180g)', 'A4 Cartolina (180g)'),
    ]

    # Definindo as opções para páginas por folha
    PAGINAS_POR_FOLHA_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('4', '4'),
    ]

    class Meta:
        model = Documento
        fields = ['arquivo', 'num_copias', 'eh_colorido', 'imprimir_dois_lados', 'paginas_por_folha', 'tipo_papel', 'layout']

    # Customizando os campos para melhor usabilidade
    arquivo = forms.FileField(label='Selecione o arquivo para impressão', widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    num_copias = forms.IntegerField(label='Número de Cópias', widget=forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}))
    eh_colorido = forms.BooleanField(label='Impressão Colorida?', required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    imprimir_dois_lados = forms.BooleanField(label='Imprimir frente e verso?', required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    paginas_por_folha = forms.ChoiceField(label='Páginas por folha', choices=PAGINAS_POR_FOLHA_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    tipo_papel = forms.ChoiceField(label='Tipo de Papel', choices=TIPO_PAPEL_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    layout = forms.ChoiceField(label='Layout', choices=[('Retrato', 'Retrato'), ('Paisagem', 'Paisagem')], widget=forms.RadioSelect())

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['endereco', 'cidade', 'cep']
        widgets = {
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'cep': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PagamentoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['metodo_pagamento']
        widgets = {
            'metodo_pagamento': forms.RadioSelect(attrs={'class': 'form-check'}),
        }