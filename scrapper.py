import requests
from bs4 import BeautifulSoup
import csv
import os

class EDHRECScrapper():

    def __init__(self, url: str):
        self.url = url
        # Extrair o nome do comandante direto
        self.commander_name = self.extract_commander_name_from_url()
        # Se não conseguir extrair o nome, paramos a execução, pq provavelmente a URL esta errada
        if not self.commander_name:
            print("ERRO: URL invalida ou não foi possivel extrair o nome do comandante")
            raise ValueError("URL inválida ou não foi possivel extrair o nome do comandante")

    '''
    Receber uma URL do tipo https://edhrec.com/commanders/belakor-the-dark-master
    E extrair só o nome do comandante
    Por enquanto vamos assumir que SEMPRE estamos recebendo um link de uma página de comandante. Adicionei no backlog uma tarefa de verificar se estamos
    na página de um comandante. 
    '''
    def extract_commander_name_from_url(self) -> str | None:
        if not self.url:
            return None
        try:
            # Pega a ultima parte da URL
            name = self.url.split('/')[-1]
            return name
        except Exception as e:
            # Captura qualquer erro inesperado
            print(f"Ocorreu um erro inesperado no processamento da string")
            return None

    '''
    Escreve no arquivo csv chamado cards.csv a partir de uma lista de nomes
    '''
    def write_to_csv(self, card_names: list) -> None:
        # Se nao tiver uma lista de cartas, não salva no arquivo
        if not card_names:
            print("Aviso: Nenhuma carta foi encontrada para salvar")
            return
        # Caminho pra salvar o csv
        directory = "decks_by_commander"
        filepath = os.path.join(directory, f"{self.commander_name}.csv")
        try:
            with open(filepath, 'w', newline='') as csvfile:
                fieldnames = ['Nome']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(card_names)
            print(f"Sucesso! Deck salvo em {filepath}")
        except (IOError, OSError) as e:
            print(f"Erro ao escrever o arquivo '{filepath}:{e}")

    '''
    Faz uma requisição GET no EDHREC e faz um scrapping buscando as cartas por nome. Como é commander por enquanto não precisamos nos preocupar
    nos nomes repetirem pq cada carta só pode ter uma no deck.
    Retorna uma lista vazia caso de errado
    '''
    def scrape_hdrec_commander_page(self)->list:
        try:
            response = requests.get(self.url)
            response.raise_for_status() # Lança um erro pra status 4xx ou 5xx
        
        except requests.exceptions.RequestException as e:
            print(f"Erro ao acessar a URL. Erro: {e}")
            return []
        # Faz o parse pra buscar os elementos
        soup = BeautifulSoup(response.text, 'html.parser')
        cards_span_elements = soup.find_all("span", class_="Card_name__Mpa7S")
        # Verifica se tem algo no scrapping
        if not cards_span_elements:
            print("ERRO: Nao foi possivel encontrar nomes de cards na pagina.")
            return []
        # Processa a lista de cartas
        card_names = []
        for s in cards_span_elements:
            card_dict = {'Nome': s.text}
            card_names.append(card_dict)
        print(f"{len(card_names)} cartas encontradas.")
        return card_names
    



