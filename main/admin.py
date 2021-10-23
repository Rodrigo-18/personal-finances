from django.contrib import admin
from django.contrib import admin
from .models import *

@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ['descricao', 'valor', 'date']
@admin.register(Despesa)
class DespesaAdmin(admin.ModelAdmin):
    list_display = ['descricao', 'valor', 'date']
@admin.register(Balanco)
class BalancoAdmin(admin.ModelAdmin):
    pass
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    pass
# Register your models here.
