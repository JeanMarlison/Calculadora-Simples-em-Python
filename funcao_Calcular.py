from mensagem import limpar_tela

def somar (a, b):
    return a + b

def sub (a, b):
    return a - b

def mult (a, b):
    return a * b

def div (a, b):
    if b != 0:
        return a / b
    else: 
        limpar_tela()
        return "Erro: Divisão por Zero!"