from django.urls import path
from . import views

urlpatterns = [
    path('consumo/', views.calcular_consumo, name='calcular_consumo'),
]