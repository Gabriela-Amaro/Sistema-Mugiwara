[Sumário Executivo](README.md) | [Diagrama de Atividades](README.DA.md) | [Levantamento e Análise de Requisitos](README.LAR.md) | [Detalhamento dos Requisitos](README.DR.md) | [Diagramas de sequência]() | [Modelo Conceitual](README.MC.md) | [Diagramas de Classes.](README.DC.md) 

# Diagrama de Classes

```mermaid
    classDiagram
    class Usuario {
        -int id
        -string nome
        -string email
        -string senha_hash
        -string role
        -datetime created_at
        -datetime updated_at
        +getId() int
        +getNome() string
        +setNome(string nome)
        +get_email() string
        +set_email(string email)
        +getSenhaHash() string
        +setSenhaHash(string senha_hash)
        +getRole() string
        +setRole(string role)
        +getCreatedAt() datetime
        +getUpdatedAt() datetime
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
        +getId() int
        +getNome() string
        +setNome(string nome)
        +getCnpj() string
        +setCnpj(string cnpj)
        +getEndereco() string
        +setEndereco(string endereco)
        +getTelefone() string
        +setTelefone(string telefone)
        +getEmail() string
        +setEmail(string email)
        +getCreatedAt() datetime
        +getUpdatedAt() datetime
    }

    class Despesa {
        -int id
        -string descricao
        -date data
        -decimal valor
        -string categoria
        -datetime created_at
        -datetime updated_at
        -int id_fornecedor
        +getId() int
        +getDescricao() string
        +setDescricao(string descricao)
        +getData() date
        +setData(date data)
        +getValor() decimal
        +setValor(decimal valor)
        +getCategoria() string
        +setCategoria(string categoria)
        +getIdFornecedor() int
        +setIdFornecedor(int id_fornecedor)
        +getCreatedAt() datetime
        +getUpdatedAt() datetime
    }

    class Pagamento {
        -int id
        -date data
        -decimal valor_pago
        -string metodo_pagamento
        -datetime created_at
        -datetime updated_at
        -int id_despesa
        -int id_conta_bancaria
        +getId() int
        +getData() date
        +setData(date data)
        +getValorPago() decimal
        +setValorPago(decimal valor_pago)
        +getMetodoPagamento() string
        +setMetodoPagamento(string metodo_pagamento)
        +getIdDespesa() int
        +setIdDespesa(int id_despesa)
        +getIdContaBancaria() int
        +setIdContaBancaria(int id_conta_bancaria)
        +getCreatedAt() datetime
        +getUpdatedAt() datetime
    }

    class Cliente {
        -int id
        -string nome
        -string cnpj_cpf
        -string endereco
        -string telefone
        -string email
        -datetime created_at
        -datetime updated_at
        +getId() int
        +getNome() string
        +setNome(string nome)
        +getCnpjCpf() string
        +setCnpjCpf(string cnpj_cpf)
        +getEndereco() string
        +setEndereco(string endereco)
        +getTelefone() string
        +setTelefone(string telefone)
        +getEmail() string
        +setEmail(string email)
        +getCreatedAt() datetime
        +getUpdatedAt() datetime
    }

    class Receita {
        -int id
        -string descricao
        -date data
        -decimal valor
        -string categoria
        -datetime created_at
        -datetime updated_at
        -int id_cliente
        +getId() int
        +getDescricao() string
        +setDescricao(string descricao)
        +getData() date
        +setData(date data)
        +getValor() decimal
        +setValor(decimal valor)
        +getCategoria() string
        +setCategoria(string categoria)
        +getIdCliente() int
        +setIdCliente(int id_cliente)
        +getCreatedAt() datetime
        +getUpdatedAt() datetime
    }

    class Recebimento {
        -int id
        -date data
        -decimal valor_recebido
        -string metodo_recebimento
        -datetime created_at
        -datetime updated_at
        -int id_receita
        -int id_conta_bancaria
        +getId() int
        +getData() date
        +setData(date data)
        +getValorRecebido() decimal
        +setValorRecebido(decimal valor_recebido)
        +getMetodoRecebimento() string
        +setMetodoRecebimento(string metodo_recebimento)
        +getIdReceita() int
        +setIdReceita(int id_receita)
        +getIdContaBancaria() int
        +setIdContaBancaria(int id_conta_bancaria)
        +getCreatedAt() datetime
        +getUpdatedAt() datetime
    }

    class FluxoCaixa {
        -int id
        -date data
        -decimal saldo_inicial
        -decimal saldo_final
        -decimal projecao_entradas
        -decimal projecao_saidas
        -datetime created_at
        -datetime updated_at
        +getId() int
        +getData() date
        +setData(date data)
        +getSaldoInicial() decimal
        +setSaldoInicial(decimal saldo_inicial)
        +getSaldoFinal() decimal
        +setSaldoFinal(decimal saldo_final)
        +getProjecaoEntradas() decimal
        +setProjecaoEntradas(decimal projecao_entradas)
        +getProjecaoSaidas() decimal
        +setProjecaoSaidas(decimal projecao_saidas)
        +getCreatedAt() datetime
        +getUpdatedAt() datetime
    }

    class Relatorio {
        -int id
        -string tipo
        -date periodo_inicio
        -date periodo_fim
        -blob arquivo_pdf
        -blob arquivo_excel
        -datetime created_at
        -datetime updated_at
        +getId() int
        +getTipo() string
        +setTipo(string tipo)
        +getPeriodoInicio() date
        +setPeriodoInicio(date periodo_inicio)
        +getPeriodoFim() date
        +setPeriodoFim(date periodo_fim)
        +getArquivoPdf() blob
        +setArquivoPdf(blob arquivo_pdf)
        +getArquivoExcel() blob
        +setArquivoExcel(blob arquivo_excel)
        +getCreatedAt() datetime
        +getUpdatedAt() datetime
    }

    class ContaBancaria {
        -int id
        -string nome_banco
        -string agencia
        -string numero_conta
        -decimal saldo_atual
        -datetime created_at
        -datetime updated_at
        +getId() int
        +getNomeBanco() string
        +setNomeBanco(string nome_banco)
        +getAgencia() string
        +setAgencia(string agencia)
        +getNumeroConta() string
        +setNumeroConta(string numero_conta)
        +getSaldoAtual() decimal
        +setSaldoAtual(decimal saldo_atual)
        +getCreatedAt() datetime
        +getUpdatedAt() datetime
    }

    class ExtratoBancario {
        -int id
        -date data
        -blob arquivo_extrato
        -datetime created_at
        -datetime updated_at
        -int id_conta_bancaria
        +getId() int
        +getData() date
        +setData(date data)
        +getArquivoExtrato() blob
        +setArquivoExtrato(blob arquivo_extrato)
        +getIdContaBancaria() int
        +setIdContaBancaria(int id_conta_bancaria)
        +getCreatedAt() datetime
        +getUpdatedAt() datetime
    }

    Fornecedor "1" --> "0..*" Despesa : fornece
    Cliente "1" --> "0..*" Receita : possui
    ContaBancaria "1" --> "0..*" Pagamento : realiza
    ContaBancaria "1" --> "0..*" Recebimento : recebe
    ContaBancaria "1" --> "0..*" ExtratoBancario : gera
    Despesa "1" --> "0..*" Pagamento : paga
    Receita "1" --> "1..*" Recebimento : registra
```
