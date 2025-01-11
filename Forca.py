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

def permissao_int(mensagem):
    while True:
        x = input(mensagem)
        if x.isdigit(): 
            return int(x)
        else:
            print("Entrada inválida. Informe apenas números.")

participante = permissao_str('Digite o nome do desafiante: ')

while True:
    limpar()
    while True:
        usuario = permissao_int('(1)Desafiante - (2)Participante ')
        if usuario != 1 and usuario != 2:
            continue
        else:
            break
        
    if usuario == 2:
        limpar()
        print('Permita o desafiante digitar a palavra chave!')
        input()
    
    limpar()
    palavraChave = permissao_str('Informe a palavra chave: ')
    dica1        = permissao_str('Informe a primeira dica: ')
    dica2        = permissao_str('Informe a segunda dica : ')
    dica3        = permissao_str('Informe a terceira dica: ')
    input()

    limpar()
    print('Vez do participante')
    input()

    while True:
        limpar()
        nivel = permissao_int(f'{participante} escolha um nível: (1)Fácil - (2)Médio - (3)Difícil  ')
        if nivel != 1 and nivel != 2 and nivel != 3:
            print('Informe somente um dos três níveis')
            input()
        else:
            break
    
    vidas = 0
    dicas = False
    palavraSecreta = len(palavraChave) * '*'
    letrasTentadas = ''
    
    if nivel == 1:
        vidas = 6
        dicas = True
    elif nivel == 2:
        vidas = 5
    else:
        vidas = 4
    
    while vidas > 0:
        limpar()
        print(f'Palavra Secreta: {palavraSecreta}')
        print(f'Vidas restantes: {vidas}')
        print(f'Letras utilizadas: {letrasTentadas}')

        print()
        while True:
            letra = permissao_str('Digite uma letra: ')
            if len(letra) > 1:
                print('Digite somente uma letra')
            else:
                break
        
        if letra not in letrasTentadas:
            letrasTentadas += letra
        else:
            print('Letra já utilizada')
            continue
        
        if letra in palavraChave:
            palavraSecreta = ''
            for i in palavraChave:
                if i in letrasTentadas:
                    palavraSecreta += i
                else:
                    palavraSecreta += '*'
        else:
            vidas -= 1
        
        if palavraChave == palavraSecreta:
            break

        print()
        if vidas == 5:
            print(' O ')
            print()
            if dicas == True:
                print(f'1ª Dica: {dica1}')
        elif vidas == 4:
            print(' O ')
            print(' | ')
            print()
            if dicas == True:
                print(f'1ª Dica: {dica1}')
                print(f'2ª Dica: {dica2}')
        elif vidas == 3:
            print(' O ')
            print(' | ')
            print(' | ')
            print()
            if dicas == True:
                print(f'1ª Dica: {dica1}')
                print(f'2ª Dica: {dica2}')
                print(f'3ª Dica: {dica3}')
        elif vidas == 2:
            print(' O ')
            print('\|/')
            print(' | ')
            print()
            if dicas == True:
                print(f'1ª Dica: {dica1}')
                print(f'2ª Dica: {dica2}')
                print(f'3ª Dica: {dica3}')
        elif vidas == 1:
            print(' O ')
            print('\|/')
            print(' | ')
            print('/ \'')
            print()
            if dicas == True:
                print(f'1ª Dica: {dica1}')
                print(f'2ª Dica: {dica2}')
                print(f'3ª Dica: {dica3}')
    
    if vidas == 0:
        print(' O ')
        print('\|/')
        print(' | ')
        print('/ \'')
        print('o o')
        print()
        print('Você perdeu!')
        input()
    else:
        print('Parabens, desafio concluido')
        input()

    limpar()
    opcao = permissao_str('Deseja jogar novamente (S/N)? ').upper()
    if opcao == 'S':
        continue
    else:
        break
