from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import CadastroVeiculo

# Página inicial
def home(request):
    return render(request, 'home/home.html')

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

def cadastro_usuario(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Cria o usuário
        User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )

        # Redireciona para o cadastro de veículo
        return redirect('cadastro_veiculo')  # nome da rota no urls.py

    return render(request, 'cadastro_usuario/cadastro_usuario.html')

