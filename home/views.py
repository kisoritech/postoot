from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Página inicial
def home(request):
    return render(request, 'home/home.html')


