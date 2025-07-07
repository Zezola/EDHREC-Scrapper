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

**Executar o Script**
Rodar o comando
```bash
python scrapper.py
```

## Resultado

Após a execução você deve ter um arquivo cards.csv na pasta raiz do projeto
