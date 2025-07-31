# Web Scrapper de cartas do EDHREC

Este é um script simples em Python que raspa os nomes de cartas de uma URL especifica de uma página de comandante do EDHREC e escreve
em um arquivo .csv

**Pré-requisitos**

- Python3 instalado no computador. Caso não tenha, baixe em: [python.org](https://www.python.org/downloads/)
- Docker instalado no computador. Caso não tenha, baixe em: [docker.com](https://docs.docker.com/get-started/get-docker/)

**Como rodar o projeto**
Clone esse repositório ou baixe o ZIP

**Abra o terminal**
Navegue até a pasta que usou pra baixar o projeto
```bash
cd caminho/para/pasta
```

**Pra rodar localmente e fazer mudanças:**
Se estiver na pasta raiz, so rodar:
```bash
flask run
```

**Montar o container a partir do Dockerfile**
```bash
docker build -t web-scrapper-app .
```

**Rodar o projeto na sua porta 5000 local**
```bash
docker run -i -d -p 5000:5000 --name mtg-scrapper web-scrapper-app
```

## Subindo o MINIO

Subir o docker do Minio. Pra dev podemos usar o comando que eles tem na documentação oficial:
```bash
docker run \
   -p 9000:9000 \
   -p 9001:9001 \
   --name minio \
   -v ~/minio/data:/data \
   -e "MINIO_ROOT_USER=ROOTNAME" \
   -e "MINIO_ROOT_PASSWORD=CHANGEME123" \
   quay.io/minio/minio server /data --console-address ":9001"
```

E pra interagir com o Minio usando a linha de comando temos que instalar o Minio Client [minio.com] https://min.io/docs/minio/linux/reference/minio-mc.html#minio-client
seguindo as instruções pra arquitetura adequada pro seu SO e criar um alias pra podermos rodar os comandos "mirando" na nossa instancia local
```bash
mc alias set local http://127.0.0.1:9000 {MINIO_ROOT_USER} {MINIO_ROOT_PASSWORD} # Trocar o ROOT_USER pelo seu user e PASSWORD pelo seu password
mc admin info local # Um comando pra teste. 
```

## Como usar:
Com o servidor rodando, você pode fazer chamadas POST na porta 5000 do seu ambiente de dev local.
Um exemplo de chamada:
```bash
curl -X POST http://localhost:5000/deck -H "Content-Type: application/json" -d '{"url": "https://edhrec.com/commanders/rowan-scion-of-war"}'
```
**Vendo se o seu arquivo csv foi escrito**
Com o container rodando, rode o comando
```bash
docker exec -it mtg-scrapper bash
```
Dentro do container, rode o comando para ver os conteudos da pasta decks_by_commander
```bash
ls decks_by_commander/
```