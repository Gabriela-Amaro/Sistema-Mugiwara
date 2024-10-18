[Sumário Executivo](README.SE.md) | [Diagrama de Atividades](README.DA.md) | [Levantamento e Análise de Requisitos](README.LAR.md) | [Detalhamento dos Requisitos](README.DR.md) | [Diagramas de sequência](README.DS.md) | [Modelo Conceitual](README.MC.md) | [Diagramas de Classes.](README.DC.md) 

# Diagrama de Classes

```mermaid
    classDiagram
    class Usuario {
        -int id
        -string nome
        -string senha_hash
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

    class Receita {
        -int id
        -string descricao
        -date data_vencimento
        -decimal valor
        -string categoria
        -datetime created_at
        +__str__() string
    }

    class Recebimento {
        -int id
        -date data
        -decimal valor_recebido
        -string metodo_recebimento
        -datetime created_at
        -int id_receita
        -int id_conta_bancaria
        +__str__() string
    }

    class FluxoCaixa {
        -int id
        -date data_inicial
        -date data_final
        -date created_at
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

    ContaBancaria "1" --> "0..*" Pagamento : realiza
    ContaBancaria "1" --> "0..*" Recebimento : recebe
    Despesa "1" --> "0..*" Pagamento : paga
    Receita "1" --> "1..*" Recebimento : registra
```
