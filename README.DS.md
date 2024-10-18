[Sumário Executivo](README.SE.md) | [Diagrama de Atividades](README.DA.md) | [Levantamento e Análise de Requisitos](README.LAR.md) | [Detalhamento dos Requisitos](README.DR.md) | [Diagramas de sequência](README.DS.md) | [Modelo Conceitual](README.MC.md) | [Diagramas de Classes.](README.DC.md) 

# Diagramas de Sequência


## Cadastro de Despesas (RF1)

```mermaid
sequenceDiagram
    actor Funcionario as Funcionário Financeiro
    participant Sistema
    participant BD as Banco de Dados

    Funcionario ->> Sistema: Solicita "Criar Despesa" (data, valor, categoria)
    Sistema ->> BD: Valida e salva dados da despesa
    BD -->> Sistema: Confirmação de salvamento
    Sistema -->> Funcionario: Confirmação de despesa cadastrada

    alt Visualizar Despesa
        Funcionario ->> Sistema: Solicita visualização de despesa
        Sistema ->> BD: Recupera dados da despesa
        BD -->> Sistema: Envia dados da despesa
        Sistema -->> Funcionario: Exibe dados da despesa
    end

    alt Editar Despesa
        Funcionario ->> Sistema: Solicita edição de despesa
        Sistema ->> BD: Atualiza dados da despesa
        BD -->> Sistema: Confirmação de atualização
        Sistema -->> Funcionario: Confirmação de edição bem-sucedida
    end

    alt Excluir Despesa
        Funcionario ->> Sistema: Solicita exclusão de despesa
        Sistema ->> BD: Exclui despesa
        BD -->> Sistema: Confirmação de exclusão
        Sistema -->> Funcionario: Confirmação de exclusão bem-sucedida
    end
```

## Pagamento de Contas (RF2)

```mermaid
sequenceDiagram
    actor Funcionario as Funcionário Financeiro
    participant Sistema
    participant BD as Banco de Dados
    participant Banco as Sistema Bancário

    Funcionario ->> Sistema: Solicita "Pagamento de Conta" (valor, data)
    Sistema ->> Banco: Envia dados de pagamento para conciliação
    Banco -->> Sistema: Confirmação de pagamento realizado
    Sistema ->> BD: Registra pagamento
    BD -->> Sistema: Confirmação de registro
    Sistema -->> Funcionario: Confirmação de pagamento realizado
```

## Cadastro de Receitas (RF3)

```mermaid
sequenceDiagram
    actor Funcionario as Funcionário Financeiro
    participant Sistema
    participant BD as Banco de Dados

    Funcionario ->> Sistema: Solicita "Criar Receita" (data, valor, categoria, cliente)
    Sistema ->> BD: Valida e salva dados da receita
    BD -->> Sistema: Confirmação de salvamento
    Sistema -->> Funcionario: Confirmação de receita cadastrada

    alt Visualizar Receita
        Funcionario ->> Sistema: Solicita visualização de receita
        Sistema ->> BD: Recupera dados da receita
        BD -->> Sistema: Envia dados da receita
        Sistema -->> Funcionario: Exibe dados da receita
    end

    alt Editar Receita
        Funcionario ->> Sistema: Solicita edição de receita
        Sistema ->> BD: Atualiza dados da receita
        BD -->> Sistema: Confirmação de atualização
        Sistema -->> Funcionario: Confirmação de edição bem-sucedida
    end

    alt Excluir Receita
        Funcionario ->> Sistema: Solicita exclusão de receita
        Sistema ->> BD: Exclui receita
        BD -->> Sistema: Confirmação de exclusão
        Sistema -->> Funcionario: Confirmação de exclusão bem-sucedida
    end
```

## Registro de Recebimentos e Pagamentos (RF4)

```mermaid
sequenceDiagram
    actor Funcionario as Funcionário Financeiro
    participant Sistema
    participant BD as Banco de Dados
    participant Banco as Sistema Bancário

    Funcionario ->> Sistema: Solicita "Registrar Transação Bancária"
    Sistema ->> Banco: Concilia transação bancária
    Banco -->> Sistema: Dados da transação conciliada
    Sistema ->> BD: Registra transação
    BD -->> Sistema: Confirmação de registro
    Sistema -->> Funcionario: Confirmação de transação registrada e conciliada
```

## Fluxo de Caixa (RF5)

```mermaid
sequenceDiagram
    actor Funcionario as Funcionário Financeiro
    participant Sistema
    participant BD as Banco de Dados

    Funcionario ->> Sistema: Solicita "Análise de Fluxo de Caixa" (período)
    Sistema ->> BD: Recupera dados de fluxo de caixa do período
    BD -->> Sistema: Analisa e calcula fluxo de caixa
    Sistema -->> Funcionario: Exibe análise de fluxo de caixa detalhada
```

## Pagamentos Eletronicos (RF6)

```mermaid
sequenceDiagram
    actor Funcionario as Funcionário Financeiro
    participant Sistema
    participant BD as Banco de Dados
    participant Banco as Sistema Bancário

    Funcionario ->> Sistema: Solicita "Pagamento Eletrônico" (valor, conta bancária)
    Sistema ->> BD: Verifica saldo disponível
    BD -->> Sistema: Confirmação de saldo
    Sistema ->> Banco: Realiza pagamento eletrônico
    Banco -->> Sistema: Confirmação de pagamento
    Sistema -->> Funcionario: Pagamento eletrônico confirmado
```
