from django.shortcuts import render, redirect
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.views import View
from .models import conta_bancaria, despesa, receita, fluxo_caixa, pagamento, receita, recebimento
from .forms import UserCreationForm, ContaBancariaForm, DespesaForm, FluxoCaixaForm, PagamentoForm, ReceitaForm, RecebimentoForm, SearchDespesaForm, SearchContaBancariaForm, SearchReceitasForm, SearchPagamentosForm, SearchRecebimentosForm
from decimal import Decimal

import datetime

@login_required
def index(request):
    saldo_contas = conta_bancaria.objects.aggregate(saldo_atual=Sum('saldo_atual'))['saldo_atual']

    entradas_confirmadas = receita.objects.filter(status=2).aggregate(total_receita=Sum('valor'))['total_receita'] 
    entradas_futuras = receita.objects.filter(status=1).aggregate(total_receita=Sum('valor'))['total_receita']

    saidas_confirmadas = despesa.objects.filter(status=2).aggregate(total_despesa=Sum('valor'))['total_despesa']
    saidas_futuras = despesa.objects.filter(status=1).aggregate(total_despesa=Sum('valor'))['total_despesa']

    contas = conta_bancaria.objects.all()
    receitas = receita.objects.all()
    despesas = despesa.objects.all()

    context = {
        'saldo_atual': saldo_contas if saldo_contas else '0,00', 
        'entradas_confirmadas': entradas_confirmadas if entradas_confirmadas else '0,00',
        'entradas_futuras': entradas_futuras if entradas_futuras else '0,00',
        'saidas_confirmadas': saidas_confirmadas if saidas_confirmadas else '0,00',
        'saidas_futuras': saidas_futuras if saidas_futuras else '0,00',
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

@login_required
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

@login_required
def showContaBancariaView(request):
    form = SearchContaBancariaForm(request.GET or None)    
    contas = conta_bancaria.objects.all()

    if form.is_valid():
        nome_banco = form.cleaned_data.get('nome_banco')
        numero_conta = form.cleaned_data.get('numero_conta')

        if nome_banco:
            contas = contas.filter(nome_banco__icontains=nome_banco)        
        
        if numero_conta:
            contas = contas.filter(numero_conta__icontains=numero_conta)

    context = {
        'contas': contas,
        'form': form
    }
    return render(request, 'mugiwara/show_conta_bancaria.html', context)

@login_required
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

@login_required
def deleteContaBancariaView(request, c_id):
    conta = conta_bancaria.objects.get(id=c_id)
    if request.method == 'POST':
        conta.delete()
        return redirect('show_conta_bancaria')
    context = {
        'conta': conta
    }
    return render(request, 'mugiwara/delete_conta_bancaria.html', context)

@login_required
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

@login_required
def showDespesaView(request):
    form = SearchDespesaForm(request.GET or None)
    despesas = despesa.objects.all()

    if form.is_valid():
        query = form.cleaned_data.get('query')
        categoria = form.cleaned_data.get('categoria')
        preco_min = form.cleaned_data.get('preco_min')
        preco_max = form.cleaned_data.get('preco_max')
        data_inicio = form.cleaned_data.get('data_inicio')
        data_fim = form.cleaned_data.get('data_fim')
        status = form.cleaned_data.get('status')

        if query:
            despesas = despesas.filter(descricao__icontains=query)        
        
        if categoria:
            despesas = despesas.filter(categoria=categoria)
        
        if preco_min:
            despesas = despesas.filter(valor__gte=preco_min)
        
        if preco_max:
            despesas = despesas.filter(valor__lte=preco_max)
        
        if data_inicio:
            despesas = despesas.filter(data_vencimento__gte=data_inicio)
        
        if data_fim:
            despesas = despesas.filter(data_vencimento__lte=data_fim)

        if status:
            despesas = despesas.filter(status=status)

    context = {
        'despesas': despesas,
        'form': form
    }
    return render(request, 'mugiwara/show_despesa.html', context)

@login_required
def deleteDespesaView(request, c_id):
    desp = despesa.objects.get(id=c_id)
    if request.method == 'POST':
        desp.delete()
        return redirect('show_despesa')
    context = {
        'despesa': desp
    }
    return render(request, 'mugiwara/delete_despesa.html', context)

@login_required
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

@login_required
def showFluxoCaixaView(request):
    fluxo_caixas = fluxo_caixa.objects.all()
    context = {
        'fluxo_caixas': fluxo_caixas
    }
    return render(request, 'mugiwara/show_fluxo_caixa.html', context)

@login_required
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

@login_required
def deleteFluxoCaixaView(request, f_id):
    fluxo = fluxo_caixa.objects.get(id=f_id)
    if request.method == 'POST':
        fluxo.delete()
        return redirect('show_fluxo_caixa')
    context = {
        'fluxo': fluxo
    }
    return render(request, 'mugiwara/delete_fluxo_caixa.html', context)

@login_required
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

@login_required
def showPagamentoView(request):
    form = SearchPagamentosForm(request.GET or None)
    pagamentos = pagamento.objects.all()

    if form.is_valid():
        data_inicio = form.cleaned_data.get('data_inicio')
        data_fim = form.cleaned_data.get('data_fim')
        metodo = form.cleaned_data.get('metodo')
        
        if data_inicio:
            pagamentos = pagamentos.filter(created_at__gte=data_inicio)
        
        if data_fim:
            pagamentos = pagamentos.filter(created_at__lte=data_fim)

        if metodo:
            pagamentos = pagamentos.filter(metodo_pagamento=metodo)

    context = {
        'form': form,
        'pagamentos': pagamentos
    }
    return render(request, 'mugiwara/show_pagamentos.html', context)
    
@login_required
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

@login_required
def showReceitaView(request):
    form = SearchReceitasForm(request.GET or None)
    receitas = receita.objects.all()
    if form.is_valid():
        query = form.cleaned_data.get('query')
        categoria = form.cleaned_data.get('categoria')
        preco_min = form.cleaned_data.get('preco_min')
        preco_max = form.cleaned_data.get('preco_max')
        data_inicio = form.cleaned_data.get('data_inicio')
        data_fim = form.cleaned_data.get('data_fim')
        status = form.cleaned_data.get('status')

        if query:
            receitas = receitas.filter(descricao__icontains=query)        
        
        if categoria:
            receitas = receitas.filter(categoria=categoria)
        
        if preco_min:
            receitas = receitas.filter(valor__gte=preco_min)
        
        if preco_max:
            receitas = receitas.filter(valor__lte=preco_max)
        
        if data_inicio:
            receitas = receitas.filter(data_vencimento__gte=data_inicio)
        
        if data_fim:
            receitas = receitas.filter(data_vencimento__lte=data_fim)

        if status:
            receitas = receitas.filter(status=status)

    context = {
        'form': form,
        'receitas': receitas
    }
    return render(request, 'mugiwara/show_receita.html', context)

@login_required
def deleteReceitaView(request, r_id):

    rec = receita.objects.get(id=r_id)
    if request.method == 'POST':
        rec.delete()
        return redirect('show_receita')
    context = {
        'receita': rec
    }
    return render(request, 'mugiwara/delete_receita.html', context)

@login_required
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

@login_required
def showRecebimentoView(request):
    form = SearchRecebimentosForm(request.GET or None)
    recebimentos = recebimento.objects.all()

    if form.is_valid():
        data_inicio = form.cleaned_data.get('data_inicio')
        data_fim = form.cleaned_data.get('data_fim')
        metodo = form.cleaned_data.get('metodo')
        
        if data_inicio:
            recebimentos = recebimentos.filter(created_at__gte=data_inicio)
        
        if data_fim:
            recebimentos = recebimentos.filter(created_at__lte=data_fim)

        if metodo:
            recebimentos = recebimentos.filter(metodo_recebimento=metodo)

    context = {
        'form': form,
        'recebimentos': recebimentos
    }
    return render(request, 'mugiwara/show_recebimentos.html', context)

