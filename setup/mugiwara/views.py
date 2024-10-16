from django.shortcuts import render, redirect
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.views import View
from .models import conta_bancaria, despesa, receita, fluxo_caixa
from .forms import UserCreationForm, ContaBancariaForm, DespesaForm, FluxoCaixaForm
from decimal import Decimal

import datetime

# def createTodoView(request):
#     form = TodoForm
#     if request.method == "POST":
#         form = TodoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("show_url")
#     template_name = "todoapp/todo.html"
#     context = {"form": form}
#     return render(request, template_name, context)

# def showTodoView(request):
#     obj = Todo.objects.all()
#     template_name = "todoapp/show.html"
#     context = {"obj": obj}
#     return render(request, template_name, context)

# def updateTodoView(request, f_id):
#     obj = Todo.objects.get(id=f_id)
#     form = TodoForm(instance=obj)
#     if request.method == "POST":
#         form = TodoForm(request.POST, instance=obj)
#         if form.is_valid():
#             form.save()
#             return redirect("show_url")
#     template_name = "todoapp/todo.html"
#     context = {"form": form}
#     return render(request, template_name, context)

# def deleteTodoView(request, f_id):
#     obj = Todo.objects.get(id = f_id)
#     if request.method == "POST":
#         obj.delete()
#         return redirect("show_url")
#     template_name = "todoapp/confirmation.html"
#     context = {"obj": obj}
#     return render(request, template_name, context)

# --------------------------------------------------


@login_required
def index(request):
    saldo_atual = conta_bancaria.objects.aggregate(saldo_atual=Sum('saldo_atual'))['saldo_atual']
    total_receita = receita.objects.aggregate(total_receita=Sum('valor'))['total_receita']
    total_despesa = despesa.objects.aggregate(total_despesa=Sum('valor'))['total_despesa']

    contas = conta_bancaria.objects.all()
    receitas = receita.objects.all()
    despesas = despesa.objects.all()

    context = {
        'saldo_atual': saldo_atual if saldo_atual else '0,00', 
        'total_receita': total_receita if total_receita else '0,00',
        'total_despesa': total_despesa if total_despesa else '0,00',
        'receitas': receitas,
        'despesas': despesas,
        'contas': contas,
    }

    return render(request, "mugiwara/index.html", context)

class login(LoginView):
    template_name = 'mugiwara/login.html'

class signup(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'mugiwara/signup.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request, 'mugiwara/signup.html', {'form': form})

def userLogout(request):
    logout(request)  # Faz o logout do usuário
    return redirect('login')  # Redireciona para a página de login

# @login_required
def createContaBancariaView(request):
    form = ContaBancariaForm
    if request.method == "POST":
        form = ContaBancariaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_conta_bancaria")
    context = {
        "form": form
    }
    return render(request, 'mugiwara/conta_bancaria.html', context)

# @login_required
def showContaBancariaView(request):
    contas = conta_bancaria.objects.all()
    context = {
        'contas': contas
    }
    return render(request, 'mugiwara/show_conta_bancaria.html', context)

# @login_required
def updateContaBancariaView(request, c_id):
    conta = conta_bancaria.objects.get(id=c_id)
    form = ContaBancariaForm(instance=conta)
    if request.method == 'POST':
        form = ContaBancariaForm(request.POST, instance=conta)
        if form.is_valid():
            form.save()
            return redirect('show_conta_bancaria')
    context = {
        'form': form
    }
    return render(request, 'mugiwara/conta_bancaria.html', context) 

# @login_required
def deleteContaBancariaView(request, c_id):
    conta = conta_bancaria.objects.get(id=c_id)
    if request.method == 'POST':
        conta.delete()
        return redirect('show_conta_bancaria')
    context = {
        'conta': conta
    }
    return render(request, 'mugiwara/delete_conta_bancaria.html', context)

# @login_required
def createDespesaView(request):
    form = DespesaForm
    if request.method == 'POST':
        form = DespesaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_despesa')
    
    context = {
        'form': form
    }

    return render(request, 'mugiwara/despesa.html', context)

# @login_required
def showDespesaView(request):
    despesas = despesa.objects.all()
    context = {
        'despesas': despesas
    }
    return render(request, 'mugiwara/show_despesa.html', context)

# @login_required
def updateDespesaView(request, c_id):
    despesas = despesa.objects.get(id=c_id)
    form = DespesaForm(instance=despesas)
    if request.method == 'POST':
        form = DespesaForm(request.POST, instance=despesas)
        if form.is_valid():
            form.save()
            return redirect('show_despesa')
    context = {
        'form': form
    }
    return render(request, 'mugiwara/despesa.html', context) 

# @login_required
def deleteDespesaView(request, c_id):
    desp = despesa.objects.get(id=c_id)
    if request.method == 'POST':
        desp.delete()
        return redirect('show_despesa')
    context = {
        'despesa': desp
    }
    return render(request, 'mugiwara/delete_despesa.html', context)

# @login_required
def createFluxoCaixaView(request):
    form = FluxoCaixaForm
    if request.method == 'POST':
        form = FluxoCaixaForm(request.POST)
        if form.is_valid():
            
            form.save()
            return redirect('show_fluxo_caixa')
    
    context = {
        'form': form
    }

    return render(request, 'mugiwara/fluxo_caixa.html', context)

# @login_required
def showFluxoCaixaView(request):
    fluxo_caixas = fluxo_caixa.objects.all()
    context = {
        'fluxo_caixas': fluxo_caixas
    }
    return render(request, 'mugiwara/show_fluxo_caixa.html', context)

def showFluxoCaixaOneView(request, f_id):
    fluxo_caixas = fluxo_caixa.objects.get(id=f_id)
    data_inicio = fluxo_caixas.data_inicial - datetime.timedelta(days=1)
    data_fim = fluxo_caixas.data_final + datetime.timedelta(days=1)
    despesas = despesa.objects.filter(created_at__range=[data_inicio, data_fim])
    receitas = receita.objects.filter(created_at__range=[data_inicio, data_fim])
    total_receitas = Decimal(receitas.aggregate(total_receitas=Sum('valor'))['total_receitas'])
    total_despesas = Decimal(despesas.aggregate(total_despesas=Sum('valor'))['total_despesas']) 

    context = {
        'total_receitas': total_receitas,
        'total_despesas': total_despesas,
        'receitas': receitas,
        'despesas': despesas,
        'fluxo_caixa': fluxo_caixas
    }
    return render(request, 'mugiwara/show_fluxo_caixa_one.html', context)

def deleteFluxoCaixaView(request, f_id):
    fluxo = fluxo_caixa.objects.get(id=f_id)
    if request.method == 'POST':
        fluxo.delete()
        return redirect('show_fluxo_caixa')
    context = {
        'fluxo': fluxo
    }
    return render(request, 'mugiwara/delete_fluxo_caixa.html', context)


# @login_required
# def contasReceber(request):
#     return render(request, "mugiwara/")

# @login_required
# def fluxo_caixa(request):
#     return render(request, "mugiwara/")

# @login_required
# def relatorios(request):
#     return render(request, "mugiwara/")

# @login_required
# def busca(request):
#     return render(request, "mugiwara/")