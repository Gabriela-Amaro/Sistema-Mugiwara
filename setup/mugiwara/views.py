from django.shortcuts import render
from django.db.models import Sum
from .models import conta_bancaria, despesa, receita

def index(request):
    saldo_atual = conta_bancaria.objects.aggregate(saldo_atual=Sum('saldo_atual'))['saldo_atual']
    total_receita = receita.objects.aggregate(total_receita=Sum('valor'))['total_receita']
    total_despesa = despesa.objects.aggregate(total_despesa=Sum('valor'))['total_despesa']

    receitas = receita.objects.all()
    despesas = despesa.objects.all()

    context = {
        'saldo_atual': saldo_atual, 
        'total_receita': total_receita,
        'total_despesa': total_despesa,
        'receitas': receitas,
        'despesas': despesas
    }

    return render(request, "mugiwara/", context)

def login(request):
    return render(request, "mugiwara/")

def contas_pagar(request):
    return render(request, "mugiwara/")

def contas_receber(request):
    return render(request, "mugiwara/")

def fluxo_caixa(request):
    return render(request, "mugiwara/")

def relatorios(request):
    return render(request, "mugiwara/")

def busca(request):
    return render(request, "mugiwara/")