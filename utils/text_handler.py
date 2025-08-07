'''Classe para lidar com normalizações e correções de texto'''
class TextHandler():
    def __init__(self):
        pass

    @classmethod
    def format_text_to_kebab_case(cls, text):
        '''
        Função que deve receber um texto qualquer e retornar ele com as palavras separadas por - e tudo minusculo
        seguindo a convenção "kebab case"
        Exemplos de entrada e saida:
        NomeComandante => nome-comandante
        Nome Comandante => nome-comandante
        nome-comandante => nome-comandante
        nome_comandante => nome-comandante
        '''