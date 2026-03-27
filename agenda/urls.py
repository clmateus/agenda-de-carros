from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.agendamento, name='agendamento'),
    path('admin/', admin.site.urls),
    path('agendamento/', views.agendamento, name='agendamento'),
    path('agendamentos/', views.listar_agendamentos, name='listar_agendamentos'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', include('django.contrib.auth.urls')),
    path('solicitacoes/', views.solicitacoes, name='solicitacoes'),
    path('responder_solicitacao/<int:id>/<str:acao>', views.responder_solicitacao, name='responder_solicitacao'),
    path('veiculos/', views.veiculos, name='veiculos'),
    path('veiculos/editar/<int:pk>/', views.editar_veiculo, name='editar_veiculo'),
    path('veiculos/remover/<int:pk>/', views.remover_veiculo, name='remover_veiculo'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)