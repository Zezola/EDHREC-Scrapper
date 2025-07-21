# Web Scrapper de cartas do EDHREC

Este é um script simples em Python que raspa os nomes de cartas de uma URL especifica de uma página de comandante do EDHREC e escreve
em um arquivo .csv

**Pré-requisitos**

- Python3 instalado no computador. Caso não tenha, baixe em: [python.org](https://www.python.org/downloads/)

**Como rodar o projeto**
Clone esse repositório ou baixe o ZIP

**Abra o terminal**
Navegue até a pasta que usou pra baixar o projeto
```bash
cd caminho/para/pasta
```

**(Opcional, mas recomendado) Criar um ambiente virtual**
Isso isola as dependencias do seu projeto e evita conflitos com outras bibliotecas
```bash
python -m venv venv
```

**Instalar Dependencias**
Esse comando vai insalar as dependencias que estão no requirements.txt
```bash
pip install -r requirements.txt
```

**Subir o servidor local**
Rodar o comando
```bash
flask run
```
## Como usar:
Com o servidor rodando, você pode fazer chamadas POST na porta 5000 do seu ambiente de dev local.
Um exemplo de chamada:
```bash
curl -X POST http://localhost:5000/deck -H "Content-Type: application/json" -d '{"url": "https://edhrec.com/commanders/nahiri-forged-in-fury"}'
```
