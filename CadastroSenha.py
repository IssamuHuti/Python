import os
import calendar
from datetime import datetime, date

def limpar():
    os.system('cls')

def preenchimento_data(mensagem):
    while True:
        x = input(mensagem)
        try:
            data_formatada = datetime.strptime(x, "%d/%m/%Y")
            return data_formatada
        except ValueError:
            print('Formato de data invalido, formato correto é "dd/mm/aaaa"')

def permissao_int(mensagem):
    while True:
        x = input(mensagem)
        if x.isdigit(): 
            return int(x)
        else:
            print("Entrada inválida. Informe apenas números.")

vermelho  = '\033[31m'
reset     = '\033[0m'
maiuscula = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
minuscula = 'abcdefghijklmnopqrstuvwxyz'
numerico  = '0123456789'
especiais = '!@#$%^&*()-+'
senhaCadastrada  = ''
codigo           = 0
codigoCadastrado = []
while True:
    limpar()
    print('MENU')
    opcao = permissao_int('Deseja Cadastrar(1) - Consultar(2) - Sair(3) ')
    while opcao not in [1, 2, 3]:
        print('Digite somente 1, 2 ou 3')
        opcao = permissao_int('Deseja Cadastrar(1) - Consultar(2) - Sair(3) ')
    
    if opcao == 1:
        limpar()
        codigo += 1 
        while True:
            validadorMaiusculo = False
            validadorMinusculo = False
            validadorNumericos = False
            validadorEspeciais = False
            print(f'Codigo: {codigo}')
            codigoCadastrado.append(codigo)
            senhaUsuario = input('Digite uma senha: ')
            for i in senhaUsuario:
                if i in maiuscula:
                    validadorMaiusculo = True
                if i in minuscula:
                    validadorMinusculo = True
                if i in numerico:
                    validadorNumericos = True
                if i in especiais:
                    validadorEspeciais = True
            if all([validadorMaiusculo, validadorMinusculo, validadorNumericos, validadorEspeciais]) and len(senhaUsuario) >= 8 and len(senhaUsuario) <= 12:
                dataCadastro = preenchimento_data('Informe a data do cadastro: ')
                print('Senha Cadastrada com sucesso')
                if len(senhaUsuario) < 12:
                    senhaUsuario += (12 - len(senhaUsuario)) * ' '
                senhaCadastrada += senhaUsuario
                senhaCadastrada += str(dataCadastro)[:-9]
                input()
                break
            else:
                if len(senhaUsuario) > 12:
                    print('A senha pode ter no máximo 12 caracteres, digite uma nova senha!')
                elif len(senhaUsuario) < 8:
                    print('A senha tem que ter no mínimo 8 caracteres, digite uma nova senha!')
                else:
                    print('Senha fraca, informe uma senha mais forte!')

    elif opcao == 2:
        if senhaCadastrada == '':
            print('O sistema não possui nenhum cadastro')
            input()
            continue
        
        else:
            selecaoCodigo   = permissao_int('Selecione um codigo: ')
            if selecaoCodigo not in codigoCadastrado:
                print(f'Codigo não cadastrado, informe um código válido de {codigoCadastrado[0]} até {codigoCadastrado[-1]}')
                input()
            else:
                posicaoCadastro = (selecaoCodigo - 1) * 22
                ultimaPosicao   = posicaoCadastro + 22
                cadastro        = senhaCadastrada[posicaoCadastro:ultimaPosicao]
                senha           = cadastro[0:11]
                data            = cadastro[12:22]
                print(senha)
                print(data)

                print()
                ano = int(data[0:4])
                mes = int(data[5:7])
                dia = int(data[8:10])
                calendario  = calendar.TextCalendar()
                diaDestaque = ''
                for linha in calendario.formatmonth(ano, mes).splitlines():
                    if str(dia).rjust(2) in linha:
                        linha = linha.replace(str(dia).rjust(2), f'{vermelho}{dia}{reset}')
                    diaDestaque += linha + '\n'
                
                print(diaDestaque)

                input()
    
    else:
        break

limpar()
print('Você saiu do sistema!')