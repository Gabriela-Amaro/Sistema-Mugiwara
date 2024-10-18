[Sumário Executivo](README.md) | [Diagrama de Atividades](README.DA.md) | [Levantamento e Análise de Requisitos](README.LAR.md) | [Detalhamento dos Requisitos](README.DR.md) | [Diagramas de sequência]() | [Modelo Conceitual](README.MC.md) | [Diagramas de Classes.](README.DC.md) 

# Modelo Conceitual

```mermaid
erDiagram
    USUARIO {
        int id PK
        string nome
        string senha_hash
        datetime created_at
        datetime updated_at
    }
    
    DESPESAS {
        int id PK
        string descricao
        date data
        decimal valor
        string categoria
        datetime created_at
    }
    
    PAGAMENTOS {
        int id PK
        decimal valor_pago
        int metodo_pagamento
        datetime created_at
        int id_despesa FK
        int id_conta_bancaria FK
    }
    
    RECEITAS {
        int id PK
        string descricao
        date data
        decimal valor
        string categoria
        datetime created_at
    }
    
    RECEBIMENTOS {
        int id PK
        date data
        decimal valor_recebido
        string metodo_recebimento
        datetime created_at
        int id_receita FK
        int id_conta_bancaria FK
    }
    
    FLUXO_CAIXA {
        int id PK
        date data
        decimal saldo_inicial
        decimal saldo_final
        decimal projecao_entradas
        decimal projecao_saidas
    }
    
    CONTAS_BANCARIAS {
        int id PK
        string nome_banco
        string agencia
        string numero_conta
        decimal saldo_atual
        datetime created_at
        datetime updated_at
    }
    
    CONTAS_BANCARIAS ||--o{ PAGAMENTOS : realiza
    CONTAS_BANCARIAS ||--o{ RECEBIMENTOS : recebe
    DESPESAS ||--o{ PAGAMENTOS : paga
    RECEITAS ||--o{ RECEBIMENTOS : registra
```
