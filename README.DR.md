[Sumário Executivo](README.md) | [Diagrama de Atividades](README.DA.md) | [Levantamento e Análise de Requisitos](README.LAR.md) | [Detalhamento dos Requisitos](README.DR.md) | [Diagramas de sequência]() | [Modelo Conceitual](README.MC.md) | [Diagramas de Classes.](README.DC.md) 

# Detalhamento dos Requisitos

|RF1. CRUD de Fornecedores|
|-----------------------|
|Descrição: Permitir a criação, edição, visualização e exclusão de fornecedores, com informações, como nome, CNPJ, e contato.|
|Fontes: Departamento financeiro.|
|Usuários: Funcionários do setor financeiro, administradores.|
|Informações de entrada: Nome do fornecedor, CNPJ, telefone, e-mail.|
|Informações de saída: Lista de fornecedores, dados atualizados do fornecedor.|
|Requisitos não funcionais: Tempo de resposta rápido para CRUD, segurança dos dados (criptografia).|

|RF2. CRUD de Despesas|
|-----------------------|
|Descrição: Criar, editar, visualizar e excluir despesas detalhadas, como data, valor, categoria e fornecedor vinculado.|
|Fontes: Documentos fiscais, fornecedores.|
|Usuários: Funcionários do setor financeiro, administradores.|
|Informações de entrada: Data, valor, categoria, fornecedor.|
|Informações de saída: Relatórios de despesas, histórico de despesas por fornecedor.|
|Requisitos não funcionais: Interface intuitiva, tempo de resposta rápido.|

|RF3. Pagamento de Contas|
|-----------------------|
|Descrição: Facilitar a execução de pagamentos de contas, com integração a sistemas bancários para conciliação automática.|
|Fontes: Contas a pagar, fornecedores.|
|Usuários: Funcionários do setor financeiro, administradores.|
|Informações de entrada: Conta a pagar, dados de pagamento (valor, data).|
|Informações de saída: Confirmação de pagamento, extrato bancário conciliado|
|Requisitos não funcionais: Alta disponibilidade, segurança (integração bancária segura).|

|RF4. CRUD de Clientes|
|-----------------------|
|Descrição: criar, editar, visualizar e excluir informações de clientes.|
|Fontes: Clientes.|
|Usuários: Funcionários do setor de vendas, financeiro, administradores.|
|Informações de entrada: Nome, CNPJ/CPF, endereço, telefone, e-mail.|
|Informações de saída: Lista de clientes, dados atualizados do cliente.|
|Requisitos não funcionais: Segurança dos dados, conformidade com LGPD.|

|RF5. CRUD de Receitas|
|-----------------------|
|Descrição: Criar, editar, visualizar e excluir receitas com detalhes como data, valor, categoria e cliente.|
|Fontes: Contratos, vendas realizadas.|
|Usuários: Funcionários do setor financeiro, administradores.|
|Informações de entrada: Data, valor, categoria, cliente.|
|Informações de saída: Relatórios de receitas.|
|Requisitos não funcionais: Interface de fácil navegação, confiabilidade dos dados.|

|RF6. Registro de Pagamentos|
|-----------------------|
|Descrição: Permitir o registro e conciliação de pagamentos recebidos, com integração bancária.|
|Fontes:  Bancos, clientes.|
|Usuários: Funcionários do setor financeiro, administradores.|
|Informações de entrada: Informações de recebimentos (valor, data).|
|Informações de saída: Pagamentos registrados, conciliação bancária.|
|Requisitos não funcionais: Segurança na integração bancária, velocidade na conciliação.|

|RF8. Projeção de Fluxo de Caixa|
|-----------------------|
|Descrição: Permitir a criação de previsões de fluxo de caixa baseadas em lançamentos futuros.|
|Fontes: receitas e despesas futuras|
|Usuários: funcionarios, administradores.|
|Informações de entrada: Lançamentos futuros de receitas e despesas, e data futura.|
|Informações de saída: Projeção detalhada de entradas e saídas futuras.|
|Requisitos não funcionais: Precisão nos cálculos, interface amigável.|

|RF13. Pagamentos Eletrônicos|
|-----------------------|
|Descrição: Facilitar a realização de pagamentos eletrônicos diretamente pelo sistema.|
|Fontes: Contas a pagar.|
|Usuários: Funcionários, administradores.|
|Informações de entrada: Dados de pagamento (valor, conta bancária(drop down das contas bancarias existentes typedchoice).|
|Informações de saída: Confirmação de pagamento eletrônico, se o valor for menor ou igual ao saldo.|
|Requisitos não funcionais: |

|RF15. Registro de Recebimentos e Pagamentos|
|-----------------------|
|Descrição:  Facilitar o registro e a conciliação de transações bancárias no sistema.|
|Fontes: Bancos, clientes, fornecedores.|
|Usuários: Funcionários do setor financeiro, administradores.|
|Informações de entrada:  Informações das transações bancárias.|
|Informações de saída: Transações registradas e conciliadas.|
|Requisitos não funcionais: Baixo tempo de resposta, segurança dos dados.|
