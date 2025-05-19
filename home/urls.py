from django.urls import path
from . import views

urlpatterns = [
    path('cadastro_usuario/', views.cadastro_usuario, name='cadastro_usuario'),
    path('cadastro_veiculo/', views.cadastro_veiculo, name='cadastro_veiculo'),
    path('', views.home , name='home'),  # Exibe home.html
]
