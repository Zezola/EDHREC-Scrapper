# Imagem oficial do python
FROM python:3.10-slim

# Diretorio que vamos usar dentro do container
WORKDIR /app

# Copia o arquivo de dependencias. O primeiro argumento é o arquivo que vamos copiar, o segundo é o diretorio pra onde vamos copiar. No caso esta '.' pq vamos copiar pro diretorio padrao
COPY requirements.txt .

# Roda o pip install dentro do container com o requirements.txt
RUN pip install -r requirements.txt

# Copiar os arquivos do projeto para o WORKDIR
COPY . .

# Expoe a porta que o Flask vai usar (porta 5000)
EXPOSE 5000

# Definir as variaveis de ambiente pra rodar o Flask. Similar a fazer export FLASK_APP=meuapp.py no terminal antes de rodar o flask shell
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]