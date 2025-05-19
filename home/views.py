from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import CadastroVeiculo
from .forms import TransactionForm, LoginForm
from django.contrib.auth.decorators import login_required

# Página de login (home)
def home(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email_or_username = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # 1º: Tenta autenticar diretamente com o que o usuário digitou
            user = authenticate(request, username=email_or_username, password=password)

            if user is None:
                # 2º: Se falhar, tenta autenticar via email (buscar o username associado)
                try:
                    user_obj = User.objects.get(email=email_or_username)
                    user = authenticate(request, username=user_obj.username, password=password)
                except User.DoesNotExist:
                    user = None

            if user is not None:
                login(request, user)
                return redirect('calcular_consumo')
            else:
                messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'home/home.html', {'form': form})

# Página protegida de cálculo de consumo
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

# Cadastro de veículo (ligado ao usuário já registrado)
def cadastro_veiculo(request):
    if request.method == "POST":
        usuario_id = request.POST.get('usuario')
        modelo = request.POST.get('modelo')
        placa = request.POST.get('placa')
        ano = request.POST.get('ano')
        cor = request.POST.get('cor')
        renavam = request.POST.get('renavam')

        usuario = User.objects.get(id=usuario_id)
        CadastroVeiculo.objects.create(
            usuario=usuario,
            modelo=modelo,
            placa=placa,
            ano=ano,
            cor=cor,
            renavam=renavam
        )

        return redirect('home')

    usuarios = User.objects.all()
    return render(request, 'cadastro_usuario/cadastro_veiculo.html', {'usuarios': usuarios})

# Cadastro de usuário
def cadastro_usuario(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Cria usuário com senha criptografada
        User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )

        return redirect('cadastro_veiculo')

    return render(request, 'cadastro_usuario/cadastro_usuario.html')

