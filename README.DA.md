[Sumário Executivo](README.md) | [Diagrama de Atividades](README.DA.md) | [Levantamento e Análise de Requisitos](README.LAR.md) | [Detalhamento dos Requisitos](README.DR.md) | [Diagramas de sequência]() | [Modelo Conceitual](README.MC.md) | [Diagramas de Classes.](README.DC.md) 

# Diagrama de Atividades

```mermaid
graph TD
    Start([Início]) --> Login[Login no Sistema]
    Login --> |Sucesso| ModuleSelection{Selecionar Módulo?}
    ModuleSelection --> |Contas a Pagar| AccountsPayable[Visualizar Contas a Pagar]
    ModuleSelection --> |Contas a Receber| AccountsReceivable[Visualizar Contas a Receber]
    ModuleSelection --> |Fluxo de Caixa| CashFlow[Visualizar Fluxo de Caixa]
    ModuleSelection --> |Relatórios Financeiros| FinancialReports[Visualizar Relatórios]

    AccountsPayable --> ApprovalNeeded{Aprovação Necessária?}
    ApprovalNeeded --> |Sim| ManagerApproval[Solicitar Aprovação]
    ApprovalNeeded --> |Não| ProceedToPayment[Realizar Pagamento]
    ManagerApproval --> ProceedToPayment
    ProceedToPayment --> UpdateStatus[Atualizar Status da Conta]

    AccountsReceivable --> PaymentReceived{Pagamento Recebido?}
    PaymentReceived --> |Sim| RegisterPayment[Registrar Pagamento]
    PaymentReceived --> |Não| KeepPending[Manter Pendência]
    RegisterPayment --> UpdateStatusReceivable[Atualizar Status de Recebível]

    FinancialReports --> ReportType{Selecionar Tipo de Relatório?}
    ReportType --> BalanceSheet[Balanço Patrimonial]
    ReportType --> IncomeStatement[Demonstração de Resultados]
    ReportType --> CashFlowReport[Relatório de Fluxo de Caixa]
    BalanceSheet --> GenerateReport[Gerar Relatório]
    IncomeStatement --> GenerateReport
    CashFlowReport --> GenerateReport
    GenerateReport --> Export[Exportar como PDF/Excel]

    UpdateStatus --> End[Logout ou Sair]
    UpdateStatusReceivable --> End
    CashFlow --> End
    Export --> End
```
