from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('carros/', views.listar_carros, name='listar_carros'),
    path('agendamentos/', views.listar_agendamentos, name='listar_agendamentos'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', include('django.contrib.auth.urls')),
]