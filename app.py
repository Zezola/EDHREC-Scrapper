from flask import Flask, request, jsonify
from minio import Minio
app = Flask(__name__)
from scrapper import EDHRECScrapper
from utils.csv_handler import CSVHandler

'''Criar o minioclient assim que rodamos o app'''
client = Minio("localhost:9000",
        access_key="minioadmin",
        secret_key="minioadmin",
        secure=False
    )

'''
Rota pra fazer um scrapping em uma URL e escrever em um arquivo CSV
'''
@app.route("/deck", methods=['POST'])
def get_deck_csv():
    try:
        # O body vai ser um json no formato com uma chave "url"
        data = request.json
        url = data.get('url')
        if not data or 'url' not in data:
            return jsonify({"erro": "JSON inválido ou chave 'url' ausente."}), 400
        # Instancia o scrapper passando a URL e instancia o CSVHandler
        edhrec_scrapper = EDHRECScrapper(url=url)
        csv_handler = CSVHandler(base_dir='./decks_by_commander')
    
        # Faz o scrapping pra pegar a lista de cartas e o commander name
        deck_cards = edhrec_scrapper.scrape_hdrec_commander_page()
        commander_name = edhrec_scrapper.commander_name
        # Verificar o resultado do scrapping antes de escrever no arquivo
        if not deck_cards:
            return jsonify({
                "mensagem": "Scrapping concluido, mas nenhuma carta encontrada",
                "comandante": edhrec_scrapper.commander_name
            }), 404
        # Escreve no arquivo CSV
        csv_handler.write_to_csv(deck_cards, commander_name)
        return jsonify({
            "status": "sucesso",
            "comandante": edhrec_scrapper.commander_name,
            "cartas_salvas": len(deck_cards)
        }), 200
        
    except ValueError as e:
        # Pegar os erros de URL invalida que tem no __init__ da classe
        return jsonify({"erro": str(e)}), 400
    except Exception as e:
        print(f"Erro inesperado {e}")
        return jsonify({"erro": "Ocorreu um erro interno no servidor."}), 500

'''
Rota para salvar um arquivo CSV no Minio
'''
@app.route("/deck/csv/save", methods=['POST'])
def save_csv_in_bucket():
    # Receber o nome do comandante e procurar na pasta de decks por comandante
    data = request.json
    commander_name = data.get('commander_name')
    print(f"Data = {data}")
    print(f"Commander = {commander_name}")
    if not commander_name:
        return jsonify({"erro": f"Atributo commander_name não encontrado"}), 400
    csv_handler = CSVHandler(base_dir='./decks_by_commander')
    
    filepath = csv_handler.find_file_by_commander_name(commander_name=commander_name)

    if not filepath:
        return jsonify({"erro": f"Nao foi encontrado nenhum deck para {commander_name}."}), 404
    
    try:    
        client.fput_object(
            bucket_name="jose-ulisses-bucket",
            object_name=f"{commander_name}.csv",
            file_path=filepath,
            content_type="text/csv"
        )
        return jsonify({"sucesso": f"Deck do commander {commander_name} salvo no bucket jose-ulisses-bucket"})
    except Exception as e:
        print(f"Erro ao salvar arquivo no bucket: {e}")
        return jsonify({"erro": f"Nao foi possivel escrever no bucket minio. "}), 500

@app.route("/deck/download_csv/<commander_name>")
def download_csv_by_commander_name(commander_name):
    # Mostra o commander name
    return f"Commander name {commander_name}"