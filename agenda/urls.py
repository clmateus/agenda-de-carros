from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('carros/', views.listar_carros, name='listar_carros'),
    path('agendamentos/', views.listar_agendamentos, name='listar_agendamentos'),
]