from django import forms
from .models import conta_bancaria, despesa, fluxo_caixa, pagamento, receita, recebimento
from .models.despesa import status_choices, categoria_choices
from .models.receita import categoria_choices_receita
from .models.pagamento import metodos_pagamento
from .models.recebimento import metodos_recebimento

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class ContaBancariaForm(forms.ModelForm):
    class Meta:
        model = conta_bancaria
        fields = 'nome_banco', 'agencia', 'numero_conta'

        label = {
            'nome_banco': 'Nome do Banco',
            'agencia': 'Agência',
            'numero_conta': 'Número da Conta'
        }

        widgets = {
            'nome_banco': forms.TextInput(attrs={
                'placeholder': 'Insira o nome do banco',
                'required': 'true',
                'maxlenght': '30'
            }),
            'agencia': forms.NumberInput(attrs={
                'placeholder': 'Insira a Agência',
                'required': 'true',
                'maxlenght': '3'

            }),
            'numero_conta': forms.NumberInput(attrs={
                'placeholder': 'Insira o número da conta',
                'required': 'true',
                'maxlenght': '16'
            }),
        }



class DespesaForm(forms.ModelForm):
    class Meta:
        model = despesa
        fields = 'categoria', 'descricao', 'data_vencimento', 'valor', 'status'

        label = {
            'categoria': 'Categoria',
            'descricao': 'Descrição',
            'data_vencimento': 'Vencimento',
            'valor': 'Valor',
            'status': 'Status'
        }

        widgets = {
            'categoria': forms.Select(attrs={
                'class': 'form-select',
                'id': 'categoria_despesa',
                'placeholder': 'Selecione a categoria',
                'required': 'true'
            }),
            'descricao': forms.TextInput(attrs={
                'placeholder': 'Descrição...',
                'required': 'true',
                'maxlenght': '254'
            }),
            'data_vencimento': forms.DateInput(attrs={
                'type': 'date',
                'placeholder': 'dd/mm/YYYY',
                'required': 'true'
            }),
            'valor': forms.NumberInput(attrs={
                'placeholder': '0,00',
                'required': 'true',
                'maxlenght': '12'
            }),
            'status': forms.Select(attrs={
                'class': 'form-select',
                'id': 'status-despesa',
                'required': 'true',
            }) 
        }

class FluxoCaixaForm(forms.ModelForm):
    class Meta:
        model = fluxo_caixa
        fields = 'data_inicial', 'data_final'

        label = {
            'data_inicial': 'De',
            'data_final': 'À'
        }

        widgets = {
            'data_inicial': forms.DateInput(attrs={
                'type': 'date',
                'placeholder': 'dd/mm/YYYY',
                'required': 'true'
            }),
            'data_final': forms.DateInput(attrs={
                'type': 'date',
                'placeholder': 'dd/mm/YYYY',
                'required': 'true'
            })
        }

class PagamentoForm(forms.ModelForm):
    class Meta:
        model = pagamento
        fields = 'metodo_pagamento', 'conta_bancaria_id'

        label = {
            'metodo_pagamento': 'Método de Pagamento',
            'conta_bancaria_id': 'Conta Bancária'
        }
        widgets = {
            'metodo_pagamento': forms.Select(attrs={
                'class': 'form-select',
                'placeholder': 'Selecione o Método de pagamento',
                'required': 'true'
            })
        }

    conta_bancaria_id = forms.ModelChoiceField(
        queryset=conta_bancaria.objects.all(),
        required=False,  # Vai ser obrigatório apenas para débito em conta
        widget=forms.Select(attrs={'class': 'form-control'})  # Estilizado com Bootstrap
    )

class ReceitaForm(forms.ModelForm):

    class Meta:
        model = receita
        fields = 'categoria', 'descricao', 'data_vencimento', 'valor', 'status'

        label = {
            'categoria': 'Categoria',
            'descricao': 'Descrição',
            'data_vencimento': 'Vencimento',
            'valor': 'Valor',
            'status': 'Status'
        }

        widgets = {
            'categoria': forms.Select(attrs={
                'class': 'form-select',
                'id': 'categoria_despesa',
                'placeholder': 'Selecione a categoria',
                'required': 'true'
            }),
            'descricao': forms.TextInput(attrs={
                'placeholder': 'Descrição...',
                'required': 'true',
                'maxlenght': '254'
            }),
            'data_vencimento': forms.DateInput(attrs={
                'type': 'date',
                'placeholder': 'dd/mm/YYYY',
                'required': 'true'
            }),
            'valor': forms.NumberInput(attrs={
                'placeholder': '0,00',
                'required': 'true',
                'maxlenght': '12'
            }),
            'status': forms.Select(attrs={
                'class': 'form-select',
                'id': 'status-despesa',
                'required': 'true',
            }) 
        }

class RecebimentoForm(forms.ModelForm):
    class Meta:
        model = recebimento
        fields = 'metodo_recebimento', 'conta_bancaria_id'

        label = {
            'metodo_recebimento': 'Método de Recebimento',
            'conta_bancaria_id': 'Conta Bancária'
        }
        widgets = {
            'metodo_recebimento': forms.Select(attrs={
                'class': 'form-select',
                'placeholder': 'Selecione o Método de Recebimento',
                'required': 'true'
            })
        }

    conta_bancaria_id = forms.ModelChoiceField(
        queryset=conta_bancaria.objects.all(),
        required=False,  # Vai ser obrigatório apenas para débito em conta
        widget=forms.Select(attrs={'class': 'form-control'})  # Estilizado com Bootstrap
    )

class SearchDespesaForm(forms.ModelForm):
    class Meta:
        model = despesa
        fields = ['categoria', 'preco_min', 'preco_max', 'data_inicio', 'data_fim', 'status']

    query = forms.CharField(
        label='Descrição',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua busca...'})
    )

    categoria_choice = despesa.objects.order_by('categoria').values_list('categoria', flat=True).distinct()
    categoria = forms.ChoiceField(
        label='Categoria', 
        choices=[('', 'Todas')] + [(categoria, categoria_choices(categoria).label) for categoria in categoria_choice], 
        required=False, 
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    preco_min = forms.DecimalField(
        label='Preço Mínimo', 
        required=False, 
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Mínimo'})
    )
    
    preco_max = forms.DecimalField(
        label='Preço Máximo', 
        required=False, 
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Máximo'})
    )
    
    data_inicio = forms.DateField(
        label='Vencimento Mínimo', 
        required=False, 
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    
    data_fim = forms.DateField(
        label='Vencimento Máximo', 
        required=False, 
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )

    status_choice = despesa.objects.order_by('status').values_list('status', flat=True).distinct()
    status = forms.ChoiceField(
        label='Status', 
        choices=[('', 'Todas')] + [(status, status_choices(status).label) for status in status_choice], 
        required=False, 
        widget=forms.Select(attrs={'class': 'form-select'})
    )

class SearchContaBancariaForm(forms.ModelForm):

    class Meta:
        model = conta_bancaria
        fields = ['nome_banco', 'numero_conta']

    nome_banco = forms.CharField(
        label='Banco',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do banco...'})
    )
    
    numero_conta = forms.DecimalField(
        label='Conta', 
        required=False, 
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Número da conta...'})
    )

class SearchReceitasForm(forms.ModelForm):
    class Meta:
        model = receita
        fields = ['categoria', 'preco_min', 'preco_max', 'data_inicio', 'data_fim', 'status']

    query = forms.CharField(
        label='Descrição',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua busca...'})
    )

    categoria_choice = receita.objects.order_by('categoria').values_list('categoria', flat=True).distinct()
    categoria = forms.ChoiceField(
        label='Categoria', 
        choices=[('', 'Todas')] + [(categoria, categoria_choices_receita(categoria).label) for categoria in categoria_choice], 
        required=False, 
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    preco_min = forms.DecimalField(
        label='Preço Mínimo', 
        required=False, 
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Mínimo'})
    )
    
    preco_max = forms.DecimalField(
        label='Preço Máximo', 
        required=False, 
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Máximo'})
    )
    
    data_inicio = forms.DateField(
        label='Vencimento Mínimo', 
        required=False, 
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    
    data_fim = forms.DateField(
        label='Vencimento Máximo', 
        required=False, 
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )

    status_choice = receita.objects.order_by('status').values_list('status', flat=True).distinct()
    status = forms.ChoiceField(
        label='Status', 
        choices=[('', 'Todas')] + [(status, status_choices(status).label) for status in status_choice], 
        required=False, 
        widget=forms.Select(attrs={'class': 'form-select'})
    )

class SearchPagamentosForm(forms.ModelForm):

    class Meta:
        model = pagamento
        fields = ['data_inicio', 'data_fim', 'metodo']

    data_inicio = forms.DateField(
        label='De', 
        required=False, 
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    
    data_fim = forms.DateField(
        label='À', 
        required=False, 
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )

    metodo_pagamento = pagamento.objects.order_by('metodo_pagamento').values_list('metodo_pagamento', flat=True).distinct()
    metodo = forms.ChoiceField(
        label='Método de Pagamento', 
        choices=[('', 'Todos')] + [(metodo, metodos_pagamento(metodo).label) for metodo in metodo_pagamento], 
        required=False, 
        widget=forms.Select(attrs={'class': 'form-select'})
    )

class SearchRecebimentosForm(forms.ModelForm):

    class Meta:
        model = recebimento
        fields = ['data_inicio', 'data_fim', 'metodo']

    data_inicio = forms.DateField(
        label='De', 
        required=False, 
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    
    data_fim = forms.DateField(
        label='À', 
        required=False, 
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )

    metodo_recebimento = recebimento.objects.order_by('metodo_recebimento').values_list('metodo_recebimento', flat=True).distinct()
    metodo = forms.ChoiceField(
        label='Método de recebimento', 
        choices=[('', 'Todos')] + [(metodo, metodos_recebimento(metodo).label) for metodo in metodo_recebimento], 
        required=False, 
        widget=forms.Select(attrs={'class': 'form-select'})
    )