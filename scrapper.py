import requests
from bs4 import BeautifulSoup
import csv


def write_to_csv(card_names):
    with open('cards.csv', 'w', newline='') as csvfile:
        fieldnames = ['Nome']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(card_names)

def scrape_hdrec_commander_page():
    card_names = []
    base_url = "https://edhrec.com/commanders/teysa-orzhov-scion"
    # Fazer uma get pra pagina 
    response = requests.get(base_url)
    # O bs4 vai dar um parse no HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    # Encontrar todos os span que tenham os nomes das cartas
    cards_span_elements = soup.find_all("span", class_="Card_name__Mpa7S")
    for s in cards_span_elements: # Adicionar o text dos spans na lista de card_names
        card_name = s.text
        card_dict = {'Nome': card_name}
        print(f"card_dict = {card_dict}\n")
        card_names.append(card_dict)
    return card_names



def main():
    cards = scrape_hdrec_commander_page()
    write_to_csv(cards)

main()
