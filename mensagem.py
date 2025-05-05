import os

def limpar_tela():
    # Para Windows
    if os.name == 'nt':
        os.system('cls')
        
def texto():
    
    
    print("Selecione a Operação")
    print(" +  -  *  / : ")

    escolha = input()
    return escolha

    
