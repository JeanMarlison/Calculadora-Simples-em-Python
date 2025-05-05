import os
from main import escolha

def limpar_tela():
    # Para Windows
    
    if os.name == 'nt':
        os.system('cls')