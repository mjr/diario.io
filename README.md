# diario.io

Sistema de gerenciamento de diários/ponto.

[![Build Status](https://travis-ci.org/mjr/eventex.svg?branch=master)](https://travis-ci.org/mjr/eventex)
[![Code Health](https://landscape.io/github/mjr/eventex/master/landscape.svg?style=flat)](https://landscape.io/github/mjr/eventex/master)

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.6
3. Ative o virtualenv.
4. Instale as dependências.
5. Crie e execute testes.
6. Rode o projeto.

```console
git clone https://github.com/mjr/diario.io.git wdio
cd wdio
python -m venv .wdio
source .wdio/bin/activate
pip install -r requirements.txt
python manage.py test
python manage.py runserver
```
