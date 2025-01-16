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

limpar()
teclas           = ['Q', 'W', 'E', 'R']

sequencia = ''
while len(sequencia) < 20:
    teclasAleatorias = random.choice(teclas)
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
    for letra in teclas:
        while True:
            for key in teclas:
                if keyboard.is_pressed(key) and key == sequencia[-1]:
                    if key == letra:
                        acertou == True
                else:
                    break
            # if sequencia[-1] == 'Q':
            #     if keyboard.is_pressed('Q'):
            #         acertou = True
            #     else:
            #         break
            # elif sequencia[-1] == 'W':
            #     if keyboard.is_pressed('W'):
            #         acertou = True
            #     else:
            #         break
            # elif sequencia[-1] == 'E':
            #     if keyboard.is_pressed('E'):
            #         acertou = True
            #     else:
            #         break
            # elif sequencia[-1] == 'R':
            #     if keyboard.is_pressed('R'):
            #         acertou = True
            #     else:
            #         break
        
    limpar()
    if acertou == True:
        acertos += 1

        teclasAleatorias2 = random.choice(teclas)
        sequencia == teclasAleatorias2 + sequencia[:18]
        for i in sequencia:
            if teclasAleatorias == 'Q':
                print('| Q          |')
            elif teclasAleatorias == 'W':
                print('|    W       |')
            elif teclasAleatorias == 'E':
                print('|       E    |')
            elif teclasAleatorias == 'R':
                print('|          R |')
        
        print('| Q  W  E  R |')
    
    else:
        print('Fim de jogo!')

print(f'Acertos: {acertos}')
