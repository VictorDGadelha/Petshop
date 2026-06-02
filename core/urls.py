from django.urls import path
from . import views

urlpatterns = [

    # DASHBOARD
    path('home/', views.dashboard, name='dashboard'),

    # CLIENTES
    path('clientes/', views.listar_clientes, name='listar_clientes'),

    path('clientes/criar/', views.criar_cliente, name='criar_cliente'),

    path('clientes/editar/<int:id>/', views.editar_cliente, name='editar_cliente'),

    path('clientes/status/<int:id>/',views.alterar_status_cliente,name='alterar_status_cliente'),

    # PETS
    path('pets/', views.listar_pets, name='listar_pets'),

    path('pets/criar/', views.criar_pet, name='criar_pet'),

    path('pets/editar/<int:id>/', views.editar_pet, name='editar_pet'),

    path('pets/deletar/<int:id>/', views.deletar_pet, name='deletar_pet'),

    # SERVIÇOS
    path('servicos/', views.listar_servicos, name='listar_servicos'),

    path('servicos/criar/', views.criar_servico, name='criar_servico'),

    path('servicos/editar/<int:id>/', views.editar_servico, name='editar_servico'),

    path('servicos/deletar/<int:id>/', views.deletar_servico, name='deletar_servico'),

    # AGENDAMENTOS
    path('agendamentos/', views.listar_agendamentos, name='listar_agendamentos'),

    path('agendamentos/editar/<int:id>/', views.editar_agendamento, name='editar_agendamento'),

    path('agendamentos/deletar/<int:id>/', views.deletar_agendamento, name='deletar_agendamento'),
]