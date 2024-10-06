[Sumário Executivo](README.md) | [Diagrama de Atividades](README.DA.md) | [Levantamento e Análise de Requisitos](README.LAR.md) | [Detalhamento dos Requisitos](README.DR.md) | [Diagramas de sequência]() | [Modelo Conceitual](README.MC.md) | [Diagramas de Classes.](README.DC.md) 

# Diagrama de Classes

```mermaid
    classDiagram
    class Usuario {
        -int id
        -string nome
        -string email
        -string senha_hash
        -int role
        -datetime created_at
        -datetime updated_at
        +__str__() string
    }

    class Fornecedor {
        -int id
        -string nome
        -string cnpj
        -string endereco
        -string telefone
        -string email
        -datetime created_at
        -datetime updated_at
        +__str__() string
    }

    class Despesa {
        -int id
        -string descricao
        -date data_vencimento
        -decimal valor
        -string categoria
        -datetime created_at
        -int id_fornecedor
        +__str__() string
    }

    class Pagamento {
        -int id
        -decimal valor_pago
        -int metodo_pagamento
        -datetime created_at
        -int id_despesa
        -int id_conta_bancaria
        +__str__() string
    }

    class Clientes {
        -int id
        -string nome
        -string cnpj_cpf
        -string endereco
        -string telefone
        -string email
        -datetime created_at
        -datetime updated_at
        +__str__() string
    }

    class Receita {
        -int id
        -string descricao
        -date data_vencimento
        -decimal valor
        -string categoria
        -datetime created_at
        -int id_cliente
        +__str__() string
    }

    class Recebimento {
        -int id
        -date data
        -decimal valor_recebido
        -string metodo_recebimento
        -datetime created_at
        -int id_receita
        +__str__() string
    }

    class FluxoCaixa {
        -int id
        -date data
        -decimal saldo_inicial
        -decimal saldo_final
        -decimal projecao_entradas
        -decimal projecao_saidas
        +__str__() string
    }

    class Relatorio {
        -int id
        -int tipo
        -date periodo_inicio
        -date periodo_fim
        -blob arquivo_pdf
        -datetime created_at
        +__str__() string
    }

    class ContaBancaria {
        -int id
        -string nome_banco
        -string agencia
        -string numero_conta
        -decimal saldo_atual
        -datetime created_at
        -datetime updated_at
       +__str__() string
    }

    class ExtratoBancario {
        -int id
        -blob arquivo_extrato
        -datetime created_at
        -int id_conta_bancaria
        +__str__() string
    }

    Fornecedor "1" --> "0..*" Despesa : fornece
    Cliente "1" --> "0..*" Receita : possui
    ContaBancaria "1" --> "0..*" Pagamento : realiza
    ContaBancaria "1" --> "0..*" Recebimento : recebe
    ContaBancaria "1" --> "0..*" ExtratoBancario : gera
    Despesa "1" --> "0..*" Pagamento : paga
    Receita "1" --> "1..*" Recebimento : registra
```
