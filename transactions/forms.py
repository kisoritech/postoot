from django import forms
from .models import Transaction
from datetime import date

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['name', 'value', 'transaction_date']
        widgets = {
            'transaction_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_transaction_date(self):
        data = self.cleaned_data['transaction_date']
        if data > date.today():
            raise forms.ValidationError("A data da transação não pode ser no futuro.")
        return data