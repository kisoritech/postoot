from django.contrib import admin

from home.models import CadastroVeiculo

@admin.register(CadastroVeiculo)
class CadastroVeiculoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'modelo', 'placa', 'ano', 'cor', 'renavam', 'data_cadastro')