from django.contrib import admin
from .models import Cliente, Documento, Pedido

admin.site.register(Cliente)
admin.site.register(Documento)
admin.site.register(Pedido)