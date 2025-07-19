from flask import Flask, request, jsonify
app = Flask(__name__)
from scrapper import EDHRECScrapper

'''
Rota pra fazer um scrapping em uma URL e escrever em um arquivo CSV
'''
@app.route("/deck", methods=['POST'])
def get_deck():
    try:
        # O body vai ser um json no formato com uma chave "url"
        data = request.json
        url = data.get('url')
        if not data or 'url' not in data:
            return jsonify({"erro": "JSON inválido ou chave 'url' ausente."}), 400
        # Instancia o scrapper passando a URL
        edhrec_scrapper = EDHRECScrapper(url)
        # Faz o scrapping pra pegar a lista de cartas
        deck_cards = edhrec_scrapper.scrape_hdrec_commander_page()
        # Verificar o resultado do scrapping antes de escrever no arquivo
        if not deck_cards:
            return jsonify({
                "mensagem": "Scrapping concluido, mas nenhuma carta encontrada",
                "comandante": edhrec_scrapper.commander_name
            }), 404
        # Escreve no arquivo CSV
        edhrec_scrapper.write_to_csv(deck_cards)
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