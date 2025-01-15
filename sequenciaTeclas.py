import os
import keyboard
import random

def limpar():
    os.system('cls')

def permissao_str(mensagem):
    while True:
        x = input(mensagem)
        if x.isalpha() and ' ': 
            return x
        else:
            print("Entrada inválida. Informe apenas caracteres.")

teclas           = ['Q', 'W', 'E', 'R']
teclasAleatorias = random.choice(teclas)
