import os

def limpar():
    os.system('cls')

def permissao_str(mensagem):
    while True:
        x = input(mensagem)
        if x.isalpha() and ' ': 
            return x
        else:
            print("Entrada inválida. Informe apenas caracteres.")

participante = permissao_str('Digite o nome do desafiante: ')
