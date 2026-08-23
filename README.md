SQLAlchemy CRUD

Projeto desenvolvido em Python para praticar SQLAlchemy, CRUD, organização em camadas e migrações com Alembic.

A aplicação simula um sistema bancário simples, com cadastro de clientes, bancos, contas corrente e poupança e movimentações financeiras.

Tecnologias
Python 3.12
SQLAlchemy
Alembic
SQLite
validate-docbr
Estrutura
backend/
├── base/
├── database/
├── models/
├── repositories/
└── service/

alembic/
main.py
requirements.txt

O projeto separa as responsabilidades entre models, repositories e services, deixando o acesso ao banco e as regras de negócio organizados em camadas.

Instalação

Clone o projeto:

git clone https://github.com/brunopereirasys/sqlalchemy_crud.git
cd sqlalchemy_crud

Crie um ambiente virtual:

python -m venv .venv

Ative o ambiente e instale as dependências:

pip install -r requirements.txt
Executando
python main.py

O banco utilizado é SQLite e fica em:

backend/data/sistema_bancario.db




Alembic

Para aplicar as migrações:

alembic upgrade head

Para criar uma nova migração:

alembic revision --autogenerate -m "descrição da alteração"
Objetivo

Esse projeto faz parte dos meus estudos de Python e banco de dados, com foco em entender na prática como trabalhar com ORM, arquitetura em camadas, persistência de dados e migrações.
