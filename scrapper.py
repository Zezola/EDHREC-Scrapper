import requests
from bs4 import BeautifulSoup
import csv
import argparse

'''
Escreve no arquivo csv chamado cards.csv a partir de uma lista de nomes
'''
def write_to_csv(card_names):
    with open('cards.csv', 'w', newline='') as csvfile:
        fieldnames = ['Nome']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(card_names)

'''
Faz uma requisição GET no EDHREC e faz um scrapping buscando as cartas por nome. Como é commander por enquanto não precisamos nos preocupar
nos nomes repetirem pq cada carta só pode ter uma no deck.
'''
def scrape_hdrec_commander_page(url):
    card_names = []
    #TODO: Talvez deixar uma base url fixa como commanders/
    base_url = url
    # Fazer uma get pra pagina 
    response = requests.get(base_url)
    # O bs4 vai dar um parse no HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    # Encontrar todos os span que tenham os nomes das cartas
    cards_span_elements = soup.find_all("span", class_="Card_name__Mpa7S")
    for s in cards_span_elements: # Adicionar o text dos spans na lista de card_names
        card_name = s.text
        card_dict = {'Nome': card_name}
        #print(f"card_dict = {card_dict}\n")
        card_names.append(card_dict)
    return card_names



def main():
    # Initialize argpaser
    argparser = argparse.ArgumentParser(description='Um script que faz um scrapping em uma pagina do EDHREC')
    # Adicionando um arg posicional obrigatorio
    argparser.add_argument('url', help='A url do deck que queremos ver.')
    args = argparser.parse_args()
    print(args.url)
    """
    cards = scrape_hdrec_commander_page()
    write_to_csv(cards)
    """
    #TODO Antes de passar a URL, fazer um tratamento para verificar se essa URL existe e é do EDHREC (tambem verificar formato)
    cards = scrape_hdrec_commander_page(args.url)
    write_to_csv(cards)
main()
