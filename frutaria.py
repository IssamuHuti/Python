import os
from datetime import datetime
import keyboard

def limpar():
    os.system('cls')

def permissao_int(mensagem):
    while True:
        x = input(mensagem)
        if x.isdigit(): 
            return int(x)
        else:
            print("Entrada inválida. Informe apenas números.")

def permissao_float(mensagem):
    while True:
        x = input(mensagem)
        if x.isdigit() or '.': 
            return float(x)
        else:
            print("Entrada inválida. Informe apenas números.")

def permissao_str(mensagem):
    while True:
        x = input(mensagem)
        if x.isalpha() and ' ': 
            return x
        else:
            print("Entrada inválida. Informe apenas caracteres.")

def preenchimento_data(mensagem):
    while True:
        x = input(mensagem)
        try:
            data_formatada = datetime.strptime(x, "%d/%m/%Y")
            return data_formatada
        except ValueError:
            print('Formato de data invalido, formato correto é "dd/mm/aaaa"')

codigos     = [5500, 7744, 4445, 6565]
produtos    = ['Amora preta', 'Uva Rubi', 'Pepino', 'Morango']
precoUnit   = [1.5, 8, 3.99, 15.49]
descontos   = [12, 11, 2, 6]
estoques    = [110, 198.5, 445, 200]
logins      = ['admin', 'user1', 'user2']
senhas      = ['1234', '2345', '3456']

limpar()
while True:
    tentativa = 0
    numeroPedido = 0
    while tentativa < 3:
        login     = permissao_str('Login: ')
        senha     = permissao_int('Senha: ')
        tentativa += 1
        if login not in logins:
            print('Usuario não cadastrado!')
            continue
        if senha == senhas[logins.index(login)]:
            print('Bem vindo!')
            break
        else:
            print('Senha incorreta...')
    
    if tentativa == 3:
        break

    limpar()
    while True:
        opcao = permissao_int('(1) Efetuar pedidos - (2) Sair ')
        if opcao != 1 and opcao != 2:
            print('Digite somente 1 ou 2')
            opcao = permissao_int('(1) Efetuar pedidos - (2) Sair ')
            continue
        else:
            break
    
    if opcao == 1:
        while keyboard.is_pressed('esc') == False:
            numeroPedido += 1
            cliente = permissao_str('Digite o nome do cliente: ')
            credito = permissao_int('Limite de crédito: ')
            dataPedido = preenchimento_data('Data do pedido: ')
            
            print()
            print('CODIGOS |   PRODUTOS   | PREÇO UNIT | DESCONTO MAX % | ESTOQUE')
            print(f'{codigos[0]}   | {produtos[0]} | {precoUnit[0]}       | {descontos[0]}%            | {estoques[0]} ')
            print(f'{codigos[1]}   | {produtos[1]}    | {precoUnit[1]}       | {descontos[1]}%            | {estoques[1]} ')
            print(f'{codigos[2]}   | {produtos[2]}      | {precoUnit[2]}       | {descontos[2]}%             | {estoques[2]} ')
            print(f'{codigos[3]}   | {produtos[3]}     | {precoUnit[3]}      | {descontos[3]}%             | {estoques[3]} ')
            
            print()
            while True:
                cod = permissao_int('Digite o código do produto: ')
                if cod in codigos:
                    break
                else:
                    print('Digite somente os códigos dos produtos em estoque')
                    continue
            if estoques[codigos.index(cod)] <= 0:
                print('O produto está sem estoque')
                continue

            qtd = permissao_float('Digite a quantidade do produto: ')
            if qtd > estoques[codigos.index(cod)]:
                qtd == estoques[codigos.index(cod)]

            while True:
                desc = permissao_int('Digite o percentual de desconto: ')
                if desc > descontos[codigos.index(cod)]:
                    print(f'O limite de desconto nesse produto é de {descontos[codigos.index(cod)]}')
                    continue
                else:
                    break

        else:
            print('Pedidos realizados:')

    else:
        break
    
