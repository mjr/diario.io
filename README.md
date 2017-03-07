# diario.io

Sistema de gerenciamento de diários/ponto.

[![Build Status](https://travis-ci.org/mjr/diario.io.svg?branch=master)](https://travis-ci.org/mjr/diario.io)
[![Code Health](https://landscape.io/github/mjr/diario.io/master/landscape.svg?style=flat)](https://landscape.io/github/mjr/diario.io/master)

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.6
3. Ative o virtualenv.
4. Instale as dependências.
5. Crie e execute testes.
6. Rode as migrações para criar as tabelas no banco de dados
7. Rode o projeto.

```console
git clone https://github.com/mjr/diario.io.git wdio
cd wdio
python -m venv .wdio
source .wdio/bin/activate
pip install -r requirements.txt
python manage.py test
python manage.py migrate
python manage.py runserver
```
