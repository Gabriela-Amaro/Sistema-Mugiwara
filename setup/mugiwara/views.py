from django.shortcuts import render, redirect
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.views import View
from .models import conta_bancaria, despesa, receita, fluxo_caixa, pagamento, receita, recebimento
from .forms import UserCreationForm, ContaBancariaForm, DespesaForm, FluxoCaixaForm, PagamentoForm, ReceitaForm, RecebimentoForm
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

# @login_required
def showFluxoCaixaOneView(request, f_id):
    fluxo_caixas = fluxo_caixa.objects.get(id=f_id)
    data_inicio = fluxo_caixas.data_inicial - datetime.timedelta(days=1)
    data_fim = fluxo_caixas.data_final + datetime.timedelta(days=1)
    despesas = despesa.objects.filter(created_at__range=[data_inicio, data_fim])
    receitas = receita.objects.filter(created_at__range=[data_inicio, data_fim])
    total_receitas = receitas.aggregate(total_receitas=Sum('valor'))['total_receitas']
    total_despesas = despesas.aggregate(total_despesas=Sum('valor'))['total_despesas']

    if total_despesas:
        total_despesas = Decimal(total_despesas)
    else:
        total_despesas = 0.00

    if total_receitas:
        total_receitas = Decimal(total_receitas)
    else:
        total_receitas = 0.00

    context = {
        'total_receitas': total_receitas,
        'total_despesas': total_despesas,
        'receitas': receitas,
        'despesas': despesas,
        'fluxo_caixa': fluxo_caixas
    }
    return render(request, 'mugiwara/show_fluxo_caixa_one.html', context)

# @login_required
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
def pagamentoView(request, d_id):
    despesas = despesa.objects.get(id=d_id)
    valor = despesas.valor
    form = PagamentoForm
    if request.method == 'POST':
        form = PagamentoForm(request.POST)
        if form.is_valid():
            if despesas.status == 1:
                pagamento = form.save(commit=False)
                pagamento.valor_pago = despesas.valor
                pagamento.despesa_id = despesas
                if pagamento.metodo_pagamento == 2 and not form.cleaned_data['conta_bancaria_id']:
                    form.add_error('conta_bancaria_id', 'Conta bancária é obrigatória para débito em conta.')
                else:
                    if pagamento.metodo_pagamento == 2:
                        conta = conta_bancaria.objects.get(id=pagamento.conta_bancaria_id.id)
                        if conta.saldo_atual < valor:
                            form.add_error('conta_bancaria_id', 'Saldo Insuficiente')
                            context = {'form': form, 'valor': valor}
                            return render(request, 'mugiwara/pagamento.html', context)
                        else:
                            conta.saldo_atual -= valor
                            conta.save()
                    despesas.status = 2
                    despesas.save()
                    pagamento.save()
                    return redirect('show_pagamentos')
            else:
                return redirect('show_despesa')
    else: 
        form = PagamentoForm()
    
    context = {
        'form': form,
        'valor': valor
    }
    
    return render(request, 'mugiwara/pagamento.html', context)

# @login_required
def showPagamentoView(request):
    pagamentos = pagamento.objects.all()
    context = {
        'pagamentos': pagamentos
    }
    return render(request, 'mugiwara/show_pagamentos.html', context)
    
# @login_required
def createReceitaView(request):
    form = ReceitaForm
    if request.method == 'POST':
        form = ReceitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_receita')
    
    context = {
        'form': form
    }

    return render(request, 'mugiwara/receita.html', context)

# @login_required
def showReceitaView(request):
    receitas = receita.objects.all()
    context = {
        'receitas': receitas
    }
    return render(request, 'mugiwara/show_receita.html', context)

# @login_required
def deleteReceitaView(request, r_id):

    rec = receita.objects.get(id=r_id)
    if request.method == 'POST':
        rec.delete()
        return redirect('show_receita')
    context = {
        'receita': rec
    }
    return render(request, 'mugiwara/delete_receita.html', context)

# @login_required
def recebimentoView(request, r_id):
    receitas = receita.objects.get(id=r_id)
    valor = receitas.valor
    form = RecebimentoForm
    if request.method == 'POST':
        form = RecebimentoForm(request.POST)
        if form.is_valid():
            if receitas.status == 1:
                recebimento = form.save(commit=False)
                recebimento.valor_pago = receitas.valor
                recebimento.receita_id = receitas
                if recebimento.metodo_recebimento == 2 and not form.cleaned_data['conta_bancaria_id']:
                    form.add_error('conta_bancaria_id', 'Selecione qual conta irá receber.')
                else:
                    if recebimento.metodo_recebimento == 2:
                        conta = conta_bancaria.objects.get(id=recebimento.conta_bancaria_id.id)
                        conta.saldo_atual += valor
                        conta.save()
                    receitas.status = 2
                    receitas.save()
                    recebimento.save()
                    return redirect('show_recebimentos')
            else:
                return redirect('show_receita')
    else: 
        form = RecebimentoForm()
    
    context = {
        'form': form,
        'valor': valor
    }
    
    return render(request, 'mugiwara/recebimento.html', context)

# @login_required
def showRecebimentoView(request):
    recebimentos = recebimento.objects.all()
    context = {
        'recebimentos': recebimentos
    }
    return render(request, 'mugiwara/show_recebimentos.html', context)