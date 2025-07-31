import os
import csv

class CSVHandler():
    '''
    Classe responsável por lidar com o arquivo CSV. 
    Aqui vão ser feitas as operações de 
    - Escrita
    - Localizar arquivo por commander name
    - Deletar CSV
    - Alterar CSV
    '''
    def __init__(self, base_dir:str = './../decks_by_commander/'):
        '''
        base_dir: O caminho raiz de onde vamos achar e escrever os arquivos
        '''
        self.base_dir = base_dir
    '''
    Encontra um file-path de acordo com um commander name. Commander names devem estar sempre no formato nome-do-comandante
    Esse método retorna uma string com o caminho pro arquivo em caso de sucesso ou None
    '''
    def find_file_by_commander_name(self, commander_name:str):
        filename = f'{commander_name}.csv'
        full_path = os.path.join(self.base_dir, filename)
        print(f"Fullpath = {full_path}")
        if os.path.isfile(full_path):
            return full_path
        return None

    '''
    Escreve em um arquivo CSV
    '''
    def write_to_csv(self, card_names: list, commander_name:str) -> None:
        # Se nao tiver uma lista de cartas, não salva no arquivo
        if not card_names:
            print("Aviso: Nenhuma carta foi encontrada para salvar")
            return
        # Caminho pra salvar o csv
        filepath = os.path.join(self.base_dir, f"{commander_name}.csv")
        try:
            with open(filepath, 'w', newline='') as csvfile:
                fieldnames = ['Nome']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(card_names)
            print(f"Sucesso! Deck salvo em {filepath}")
        except (IOError, OSError) as e:
            print(f"Erro ao escrever o arquivo '{filepath}:{e}")

