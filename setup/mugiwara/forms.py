from django import forms
from .models import conta_bancaria, despesa, fluxo_caixa, pagamento

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

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

class PagamentosForm(forms.ModelForm):
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
                'placeholder': 'Selecione a Método de pagamento',
                'required': 'true'
            })
        }

    conta_bancaria_id = forms.ModelChoiceField(
        queryset=conta_bancaria.objects.all(),
        required=False,  # Vai ser obrigatório apenas para débito em conta
        widget=forms.Select(attrs={'class': 'form-control'})  # Estilizado com Bootstrap
    )