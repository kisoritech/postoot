from time import timezone
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.utils.timezone import now
from django.contrib.auth.models import User
import json

from .forms import TransactionForm
from .models import Transaction

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

# View que registra a transação (via fetch do frontend)
@csrf_exempt
@login_required
def registrar_transacao(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            nome = data.get("name", "Transação")
            valor = float(data.get("value", 0))
            abastecido = float(data.get("abastecido", 0))
            distancia = float(data.get("distancia", 0))
            tempo = float(data.get("tempo", 0))
            consumo_estimado = float(data.get("consumo_estimado", 0))

            transacao = Transaction.objects.create(
                name=nome,
                value=valor,
                abastecido=abastecido,
                distancia=distancia,
                tempo=tempo,
                consumo_estimado=consumo_estimado,
                usuario=request.user,
                transaction_date=now()
            )

            return JsonResponse({"status": "success", "id": transacao.id})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})

    return JsonResponse({"status": "error", "message": "Método não permitido"})

@login_required
def registrar_transacao(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        value = data.get('value')
        if name and value:
            transacao = Transaction.objects.create(
                user=request.user,
                name=name,
                value=value,
                transaction_date=timezone.now()
            )
            return JsonResponse({'status': 'success', 'id': transacao.id})
        return JsonResponse({'status': 'error', 'message': 'Dados incompletos'}, status=400)