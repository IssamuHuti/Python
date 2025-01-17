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

teclas = ['q', 'w', 'e', 'r']
desafiantes = {}

while True:
    limpar()
    if len(desafiantes) > 0:
        print('Ultimas pontuações')
        for nome, acerto in desafiantes.items():
            print(f'{nome} - {acerto}')

    desafiante = permissao_str('Nome do desafiante: ')

    limpar()
    print('Pressione qualquer tecla para iniciar o desafio!')
    inicio = keyboard.read_key()

    sequencia = ''
    while len(sequencia) < 20:
        teclasAleatorias = random.choice(teclas).upper()
        if teclasAleatorias == 'Q':
            print('| Q          |')
        elif teclasAleatorias == 'W':
            print('|    W       |')
        elif teclasAleatorias == 'E':
            print('|       E    |')
        elif teclasAleatorias == 'R':
            print('|          R |')
        
        sequencia += teclasAleatorias

    print('| Q  W  E  R |')

    acertos = 0
    while True:
        acertou = False

        tecla = keyboard.read_key()

        if sequencia[-1] == 'Q':
            if tecla == 'q':
                acertou = True
            else:
                break
        elif sequencia[-1] == 'W':
            if tecla == 'w':
                acertou = True
            else:
                break
        elif sequencia[-1] == 'E':
            if tecla == 'e':
                acertou = True
            else:
                break
        elif sequencia[-1] == 'R':
            if tecla == 'r':
                acertou = True
            else:
                break
        else:
            break
            
        limpar()
        if acertou == True:
            acertos += 1

            teclasAleatorias2 = random.choice(teclas).upper()
            sequencia = teclasAleatorias2 + sequencia[:18]
            for i in sequencia:
                if i == 'Q':
                    print('| Q          |')
                elif i == 'W':
                    print('|    W       |')
                elif i == 'E':
                    print('|       E    |')
                elif i == 'R':
                    print('|          R |')
            
            print('| Q  W  E  R |')
        
        else:
            print('Fim de jogo!')

    print(f'Acertos: {acertos}')

