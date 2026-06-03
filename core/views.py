from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import logout
from .models import Cliente, Pet, Servico, Agendamento
from .forms import ClienteForm, PetForm, ServicoForm, AgendamentoForm

@login_required
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def listar_pets(request):

    pets = Pet.objects.all()

    return render(request, 'pets/listar.html', {
        'pets': pets
    })

@login_required
def listar_clientes(request):

    pesquisa = request.GET.get('q', '')

    clientes = Cliente.objects.all()

    if pesquisa:
        clientes = clientes.filter(
            Q(nome__icontains=pesquisa) |
            Q(email__icontains=pesquisa)
        )

    return render(request, 'clientes/listar.html', {
        'clientes': clientes
    })


@login_required
def criar_cliente(request):

    form = ClienteForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_clientes')

    return render(request, 'clientes/form.html', {
        'form': form
    })


@login_required
def editar_cliente(request, id):

    cliente = get_object_or_404(Cliente, id=id)

    form = ClienteForm(request.POST or None, instance=cliente)

    if form.is_valid():
        form.save()
        return redirect('listar_clientes')

    return render(request, 'clientes/form.html', {
        'form': form
    })


@login_required
def alterar_status_cliente(request, id):

    cliente = get_object_or_404(Cliente, id=id)

    if request.method == 'POST':
        cliente.ativo = not cliente.ativo
        cliente.save()
        return redirect('listar_clientes')

    return render(request, 'clientes/deletar.html', {
        'cliente': cliente
    })

@login_required
def criar_pet(request):

    form = PetForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_pets')

    return render(request, 'pets/form.html', {
        'form': form
    })

@login_required
def editar_pet(request, id):

    pet = get_object_or_404(Pet, id=id)

    form = PetForm(request.POST or None, instance=pet)

    if form.is_valid():
        form.save()
        return redirect('listar_pets')

    return render(request, 'pets/form.html', {
        'form': form
    })

@login_required
def deletar_pet(request, id):

    pet = get_object_or_404(Pet, id=id)

    if request.method == 'POST':
        pet.delete()
        return redirect('listar_pets')

    return render(request, 'pets/deletar.html', {
        'pet': pet
    })


@login_required
def listar_servicos(request):
    
    pesquisa = request.GET.get('q','')

    servicos = Servico.objects.all()
    
    if pesquisa:
        servicos = servicos.filter(
            Q(nome__icontains=pesquisa) |
            Q(preco__icontains=pesquisa)
        )

    return render(request, 'servicos/listar.html', {
        'servicos': servicos,
        'pesquisa': pesquisa
    })


@login_required
def criar_servico(request):

    if request.method == 'POST':

        form = ServicoForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('listar_servicos')

    else:

        form = ServicoForm()

    return render(request, 'servicos/form.html', {
        'form': form
    })


@login_required
def editar_servico(request, id):

    servico = get_object_or_404(Servico, id=id)

    if request.method == 'POST':

        form = ServicoForm(
            request.POST,
            instance=servico
        )

        if form.is_valid():

            form.save()

            return redirect('listar_servicos')

    else:

        form = ServicoForm(instance=servico)

    return render(request, 'servicos/form.html', {
        'form': form
    })


@login_required
def deletar_servico(request, id):

    servico = get_object_or_404(
        Servico,
        id=id
    )

    if request.method == 'POST':

        servico.delete()

        return redirect('listar_servicos')

    return render(request, 'servicos/deletar.html', {
        'servico': servico
    })

@login_required
def listar_agendamentos(request):

    if request.method == 'POST':

        cliente_id = request.POST.get('cliente')
        pet_id = request.POST.get('pet')
        servico_id = request.POST.get('servico')

        data = request.POST.get('data_agendamento')
        horario = request.POST.get('horario_agendamento')

        Agendamento.objects.create(
            cliente_id=cliente_id,
            pet_id=pet_id,
            servico_id=servico_id,
            data=data,
            horario=horario,
            status='PENDENTE'
        )

        return redirect('listar_agendamentos')

    agendamentos = Agendamento.objects.all().order_by('data','horario')

    clientes = Cliente.objects.all()
    pesquisa = request.GET.get('q','')
    pets = Pet.objects.filter(nome__icontains=pesquisa) 
    servicos = Servico.objects.all()

    return render(request, 'agendamentos/listar.html', {
        'agendamentos': agendamentos,
        'clientes': clientes,
        'pets': pets,
        'servicos': servicos,
    })


@login_required
def criar_agendamento(request):

    form = AgendamentoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_agendamentos')

    return render(request, 'agendamentos/form.html', {
        'form': form
    })


@login_required
def editar_agendamento(request, id):

    agendamento = get_object_or_404(Agendamento, id=id)

    clientes = Cliente.objects.all().order_by('nome')
    pets = Pet.objects.all()
    servicos = Servico.objects.all()

    if request.method == 'POST':

        agendamento.cliente_id = request.POST.get('cliente')
        agendamento.pet_id = request.POST.get('pet')
        agendamento.servico_id = request.POST.get('servico')

        agendamento.data = request.POST.get('data_agendamento')
        agendamento.horario = request.POST.get('horario_agendamento')

        agendamento.save()

        return redirect('listar_agendamentos')

    return render(request, 'agendamentos/listar.html', {
        'editar': True,
        'agendamento_editar': agendamento,
        'agendamentos': Agendamento.objects.all(),
        'clientes': clientes,
        'pets': pets,
        'servicos': servicos,
    })


@login_required
def deletar_agendamento(request, id):

    agendamento = get_object_or_404(
        Agendamento,
        id=id
    )

    if request.method == 'POST':
        agendamento.delete()
        return redirect('listar_agendamentos')

    return render(request, 'agendamentos/deletar.html', {
        'agendamento': agendamento
    })