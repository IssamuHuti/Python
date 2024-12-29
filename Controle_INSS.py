import os
from datetime import date, datetime

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
            print(data_formatada)
            break
        except ValueError:
            print('Formato de data invalido, formato correto é "dd/mm/aaaa"')

DataAnalise  = date.today()
QtdAnalise   = permissao_int('Digite a quantidade de empregados que serão analisados: ')
QtdAnalisada = 0

while QtdAnalisada < QtdAnalise:
    limpar()
    nomeEmpregado          = permissao_str('Nome do empregado: ')
    sexoEmpregado          = permissao_str('Sexo (M/F): ').upper()
    while sexoEmpregado != 'M' and sexoEmpregado != 'F':
        print('Digite somente M/F')
        sexoEmpregado = permissao_str('Sexo (M/F): ').upper()
    dataNascimento         = preenchimento_data('Informe a data de nascimento (dd/mm/aaaa): ')
    dataAdmissao           = preenchimento_data('Informe a data de admissão (dd/mm/aaaa): ')
    dataDemissao           = preenchimento_data('Informe a data de demissão (dd/mm/aaaa): ')
    salarioBase            = permissao_float('Salario Base: ')
    adicionalNoturno       = permissao_float('Adicional noturno(%): ')
    adicionalInsalubridade = permissao_float('Adicional insalubridade(%): ')

    QtdAnalisada += 1

