from funcao_Calcular import somar, sub, div, mult
from mensagem import texto, limpar_tela

def main():
    def escolha():
        return
    
    escolha = texto()
    limpar_tela()
    
    if escolha in ('+', '-', '*', '/'):
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Erro: Entrada inválida. Digite números válidos.")
            

        if escolha == '+':
            print("Resultado:", somar(num1, num2))
        elif escolha == '-':
            print("Resultado:", sub(num1, num2))
        elif escolha == '*':
            print("Resultado:", mult(num1, num2))
        elif escolha == '/':
            print("Resultado:", div(num1, num2))
    else:
        print("Opção inválida. Por favor, escolha +, -, * ou /.")
        
while True:
    main()

