from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import TransactionForm

# Página inicial que trata login
def home(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        user = authenticate(request, username=email, password=senha)
        if user is not None:
            login(request, user)
            return redirect('consumo')  # Redireciona para o consumo
        else:
            messages.error(request, 'Email ou senha inválidos.')
            return render(request, 'home/home.html')
    return render(request, 'home/home.html')

# Página de cálculo de consumo (após login)
@login_required
def calcular_consumo(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'transactions/sucesso.html', {'form': form})
    else:
        form = TransactionForm()
    return render(request, 'transactions/consumo.html', {'form': form})