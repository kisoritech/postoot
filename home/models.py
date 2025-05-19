from django.db import models
from django.contrib.auth.models import User

class CadastroVeiculo(models.Model):
    """Realizar o cadastro de um veiculo"""
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='veiculos')  # vínculo com usuário
    modelo = models.CharField(max_length=100)  # Ex: Gol, Onix, Uno
    placa = models.CharField(max_length=10, unique=True)  # Ex: ABC-1234
    ano = models.IntegerField()  # Ex: 2020
    cor = models.CharField(max_length=30, blank=True, null=True)  # Ex: Prata
    renavam = models.CharField(max_length=20, blank=True, null=True)  # código único do veículo
    data_cadastro = models.DateTimeField(auto_now_add=True)  # automático ao salvar

    def __str__(self):
        return f"{self.modelo} - {self.placa}"
    
    class Meta:
        verbose_name = 'Veiculo'
        verbose_name_plural = 'Veiculos'