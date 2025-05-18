from django.contrib import admin

from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'value', 'transaction_date')