from django.db import models

class Transaction(models.Model):
    """Modelo que representa transação financeira"""
    name = models.CharField(max_length=255, verbose_name="Nome")
    value = models.CharField(max_length=100, verbose_name="Valor")
    transaction_date = models.DateField(verbose_name="Data da transação")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de edição")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Transação'
        verbose_name_plural = 'Transações'