[Sumário Executivo](README.SE.md) | [Diagrama de Atividades](README.DA.md) | [Levantamento e Análise de Requisitos](README.LAR.md) | [Detalhamento dos Requisitos](README.DR.md) | [Diagramas de sequência](README.DS.md) | [Modelo Conceitual](README.MC.md) | [Diagramas de Classes.](README.DC.md) 

# Mugiwara

Sistema de controle financeiro desenvolvido com Django.

## Executando o Projeto

Versão do Python: 3.12.6

#### Clonando o Projeto
```bash
git clone git@github.com:Gabriela-Amaro/Sistema-Mugiwara.git
```

#### Criando o ambiente virtal
```bash
python3 -m venv .venv
```
#### Ativando o ambiente virtual
```bash
source .venv/bin/activate
```

#### Instalando o pip
```bash
sudo apt install python3-pip
```

#### Entrando na pasta do projeto
```bash
cd setup/
```

#### Instalando as dependências
```bash
pip install -r requirements.txt
```

#### Inserindo os dados de teste no banco
```bash
python3 manage.py dumpdata mugiwara --indent 2 > fixtures/data.json
```

#### Rodando o servidor
```bash
python3 manage.py runserver
```

#### Abrindo o projeto no navegador
```bash
http://localhost:8000/
```
