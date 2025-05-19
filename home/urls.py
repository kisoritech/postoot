from django.urls import path
from . import views

urlpatterns = [
    path('consumo/', views.calcular_consumo, name='calcular_consumo'),
    path('cadastro_usuario/', views.cadastro_usuario, name='cadastro_usuario'),
    path('cadastro_veiculo/', views.cadastro_veiculo, name='cadastro_veiculo'),
    path('', views.home , name='home'),  # Exibe home.html
]
