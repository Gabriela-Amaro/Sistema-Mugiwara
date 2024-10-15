from django import forms
from .models import conta_bancaria, despesa

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
                'placeholder': 'dd/mm/YY',
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

        

# class FluxoDeCaixaForm(forms.ModelForm):
#     class Meta:
#         model = despesa
#         fields = 'categoria', 'descricao', 'data_vencimento', 'valor', 'status'

#         label = {
#             'categoria': 'Categoria',
#             'descricao': 'Descrição',
#             'data_vencimento': 'Vencimento',
#             'valor': 'Valor',
#             'status': 'Status'
#         }

#         widgets = {
#             'categoria': forms.Select(attrs={
#                 'class': 'form-select',
#                 'id': 'categoria_despesa',
#                 'placeholder': 'Selecione a categoria',
#                 'required': 'true'
#             }),
#             'descricao': forms.TextInput(attrs={
#                 'placeholder': 'Descrição...',
#                 'required': 'true',
#                 'maxlenght': '254'
#             }),
#             'data_vencimento': forms.DateInput(attrs={
#                 'placeholder': 'dd/mm/YY',
#                 'required': 'true'
#             }),
#             'valor': forms.NumberInput(attrs={
#                 'placeholder': '0,00',
#                 'required': 'true',
#                 'maxlenght': '12'
#             }),
#             'status': forms.Select(attrs={
#                 'class': 'form-select',
#                 'id': 'status-despesa',
#                 'required': 'true',
#             }) 
#         }


# class FluxoCaixaAtualForm(forms.Form):
#     data_inicial = forms.DateField(initial=datetime.today)
#     data_final = forms.DateField(initial=datetime.today)
