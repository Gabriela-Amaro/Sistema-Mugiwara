from django.shortcuts import render, redirect
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout
from django.views import View
from .models import conta_bancaria, despesa, receita
from .forms import UserCreationForm


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

@login_required
def contas_pagar(request):
    return render(request, "mugiwara/")

@login_required
def contas_receber(request):
    return render(request, "mugiwara/")

@login_required
def fluxo_caixa(request):
    return render(request, "mugiwara/")

@login_required
def relatorios(request):
    return render(request, "mugiwara/")

@login_required
def busca(request):
    return render(request, "mugiwara/")