[Sumário Executivo](README.SE.md) | [Diagrama de Atividades](README.DA.md) | [Levantamento e Análise de Requisitos](README.LAR.md) | [Detalhamento dos Requisitos](README.DR.md) | [Diagramas de sequência](README.DS.md) | [Modelo Conceitual](README.MC.md) | [Diagramas de Classes.](README.DC.md) 

# Mugiwara

Sistema de controle financeiro desenvolvido com Django.

## Executando o Projeto

Versão do Python: 3.12.6

#### Ativar o ambiente virtual
```bash
  source .venv/bin/activate
```

#### Entrar na pasta do projeto
```bash
  cd setup/
```

#### Inserir os dados de teste no banco
```bash
  python manage.py dumpdata mugiwara --indent 2 > fixtures/data.json
```

#### Rodar o servidor
```bash
  python manage.py runserver
```

#### Abrir o projeto no navegador
```bash
  http://localhost:8000/
```
