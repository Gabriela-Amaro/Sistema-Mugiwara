[Sumário Executivo](README.md) | [Diagrama de Atividades](README.DA.md) | [Levantamento e Análise de Requisitos](README.LAR.md) | [Detalhamento dos Requisitos](README.DR.md) | [Diagramas de sequência]() | [Modelo Conceitual](README.MC.md) | [Diagramas de Classes.](README.DC.md) 

# Diagrama de Classes

```mermaid
    classDiagram
    class usuario {
        -int id
        -string nome
        -string email
        -string senha_hash
        -string role
        -datetime created_at
        -datetime updated_at
        +get_nome()
        +set_nome(string nome)
        +get_role()
        +set_role(string role)
        +get_email()
        +set_email(string email)
        +get_created_at()
        +get_updated_at()
    }

    class fornecedores {
        -int id
        -string nome
        -string cnpj
        -string endereco
        -string telefone
        -string email
        -datetime created_at
        -datetime updated_at
        +get_nome()
        +set_nome(string nome)
        +get_cnpj()
        +set_cnpj(string cnpj)
        +get_endereco()
        +set_endereco(string endereco)
        +get_telefone()
        +set_telefone(string telefone)
        +get_email()
        +set_email(string email)
        +get_created_at()
        +get_updated_at()
    }
```
