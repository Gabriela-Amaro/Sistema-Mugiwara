[Sumário Executivo](README.md) | [Diagrama de Atividades](README.DA.md) | [Levantamento e Análise de Requisitos](README.LAR.md) | [Detalhamento dos Requisitos](README.DR.md) | [Diagramas de sequência]() | [Modelo Conceitual](README.MC.md) | [Diagramas de Classes.](README.DC.md) 

# Modelo Conceitual

```mermaid
erDiagram
    USUARIO {
        int id PK
        string nome
        string senha_hash
        string role
        datetime created_at
        datetime updated_at
    }

    FORNECEDORES {
        int id PK
        string nome
        string cnpj
        string endereco
        string telefone
        string email
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
        datetime updated_at
        int id_fornecedor FK
    }
    
    PAGAMENTOS {
        int id PK
        date data
        decimal valor_pago
        string metodo_pagamento
        datetime created_at
        datetime updated_at
        int id_despesa FK
        int id_conta_bancaria FK
    }
    
    CLIENTES {
        int id PK
        string nome
        string cnpj_cpf
        string endereco
        string telefone
        string email
        datetime created_at
        datetime updated_at
    }
    
    RECEITAS {
        int id PK
        string descricao
        date data
        decimal valor
        string categoria
        datetime created_at
        datetime updated_at
        int id_cliente FK
    }
    
    RECEBIMENTOS {
        int id PK
        date data
        decimal valor_recebido
        string metodo_recebimento
        datetime created_at
        datetime updated_at
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
        datetime created_at
        datetime updated_at
    }
    
    RELATORIOS {
        int id PK
        string tipo
        date periodo_inicio
        date periodo_fim
        blob arquivo_pdf
        blob arquivo_excel
        datetime created_at
        datetime updated_at
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
    
    EXTRATOS_BANCARIOS {
        int id PK
        date data
        blob arquivo_extrato
        datetime created_at
        datetime updated_at
        int id_conta_bancaria FK
    }
    
    FORNECEDORES ||--o{ DESPESAS : fornece
    CLIENTES ||--o{ RECEITAS : possui
    CONTAS_BANCARIAS ||--o{ PAGAMENTOS : realiza
    CONTAS_BANCARIAS ||--o{ RECEBIMENTOS : recebe
    CONTAS_BANCARIAS ||--o{ EXTRATOS_BANCARIOS : gera
    DESPESAS ||--o{ PAGAMENTOS : paga
    RECEITAS ||--o{ RECEBIMENTOS : registra
```
