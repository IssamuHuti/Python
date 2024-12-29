import os
from datetime import date

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

limpar()
DataCotacao = date.today()
print(f'Data {DataCotacao}')
Vendedor    = permissao_str('Vendedor: ')

print()
print('Dados do cliente')
Cliente        = permissao_str('Cliente   : ')
Idade          = permissao_int('Idade     : ')
Sexo           = permissao_str('Sexo (M/F): ').upper()
while Sexo != 'M' and Sexo != 'F':
    print('Digite somente M/F')
    Sexo = permissao_str('Sexo (M/F): ').upper()
AnoPrimeiraCNH = permissao_int('Ano da Primeira CNH: ')

print()
print('Dados do veiculo')
Veiculo        = permissao_str('Veiculo desejado : ')
AnoFabricacao  = permissao_int('Ano da fabricacao: ')
TipoVeiculo    = permissao_str('Tipo de veiculo: Passeio(P) - Esportivo(E) - Luxo(L): ').upper()
while TipoVeiculo != 'P' and TipoVeiculo != 'E' and TipoVeiculo != 'L':
    print('Digite somente P/E/L')
    TipoVeiculo = permissao_str('Tipo de veiculo: Passeio(P) - Esportivo(E) - Luxo(L): ').upper()
Motor          = permissao_float('Potencia do motor: ')
ValorFipe      = permissao_float('Valor na Tabela FIPE: ')
UsoVeiculo     = permissao_str('Finalidade de uso: Particular(P) - Profissional(O): ').upper()
while UsoVeiculo != 'P' and UsoVeiculo != 'O':
    print('Digite somente P/O')
    UsoVeiculo = permissao_str('Finalidade de uso: Particular(P) - Profissional(O): ').upper()

DiferencaAnoCNH   = DataCotacao.year - AnoPrimeiraCNH
DiferencaAnoCarro = DataCotacao.year - AnoFabricacao

# Seguradora 1
ValorBase1      = ValorFipe * 0.06
taxaAcumulada1   = 0
if 25 > Idade or Idade > 65:
    taxaAcumulada1 += 10
if Sexo == 'M':
    taxaAcumulada1 += 10
else:
    taxaAcumulada1 -= 5
if DiferencaAnoCNH <= 3:
    taxaAcumulada1 += 15
elif DiferencaAnoCNH > 8:
    taxaAcumulada1 -= 10
if TipoVeiculo == 'E':
    taxaAcumulada1 += 10
elif TipoVeiculo == 'L':
    taxaAcumulada1 += 20
if Motor > 2:
    taxaAcumulada1 += 15
if (DataCotacao.year - AnoFabricacao) < 20:
    taxaAcumulada1 += (DataCotacao.year - AnoFabricacao) * 0.5
else:
    taxaAcumulada1 += 10
if UsoVeiculo == 'O':
    taxaAcumulada1 += 10
if DataCotacao.month == 3:
    taxaAcumulada1 = taxaAcumulada1 * 0.9

# Seguradora 2
ValorBase2      = ValorFipe * 0.07
taxaAcumulada2  = 0
if 23 > Idade or Idade > 60:
    taxaAcumulada2 += 15
elif Idade >= 30 and Idade <= 50:
    taxaAcumulada2 -= 8
if Sexo == 'M':
    taxaAcumulada2 -= 6
else:
    taxaAcumulada2 += 12
if DiferencaAnoCNH <= 2:
    taxaAcumulada2 += 20
elif DiferencaAnoCNH > 5:
    taxaAcumulada2 -= 8
if TipoVeiculo == 'E':
    taxaAcumulada2 += 15
elif TipoVeiculo == 'L':
    taxaAcumulada2 += 18
if Motor > 1.5:
    taxaAcumulada2 += 10
if (DataCotacao.year - AnoFabricacao) < 10:
    taxaAcumulada2 += (DataCotacao.year - AnoFabricacao) * 0.8
else:
    taxaAcumulada2 += 8
if UsoVeiculo == 'O':
    taxaAcumulada2 += 12
if DataCotacao.month == 9:
    taxaAcumulada2 = taxaAcumulada2 * 0.92

print()
cotacaoSeguro1 = ValorBase1 + (ValorBase1 * taxaAcumulada1 / 100)
cotacaoSeguro2 = ValorBase2 + (ValorBase2 * taxaAcumulada2 / 100)

limpar()
print('Cotação dos dois seguros')
vermelho = '\033[31m'
verde = '\033[32m'
reset = '\033[0m'
if cotacaoSeguro1 > cotacaoSeguro2:
    print(f'Cotacao Seguro 1 Anual: {vermelho}{round(cotacaoSeguro1, 2)}{reset}')
    print(f'Cotacao Seguro 2 Anual: {verde}{round(cotacaoSeguro2, 2)}{reset}')
    print()
    print(f'Cotacao Seguro 1 Trimestral: {vermelho}{round(cotacaoSeguro1 / 4, 2)}{reset}')
    print(f'Cotacao Seguro 2 Trimestral: {verde}{round(cotacaoSeguro2 / 4, 2)}{reset}')
    print()
    print(f'Cotacao Seguro 1 Mensal: {vermelho}{round(cotacaoSeguro1 / 12, 2)}{reset}')
    print(f'Cotacao Seguro 2 Mensal: {verde}{round(cotacaoSeguro2 / 12, 2)}{reset}')
elif cotacaoSeguro1 < cotacaoSeguro2:
    print(f'Cotacao Seguro 1 Anual: {verde}{round(cotacaoSeguro1, 2)}{reset}')
    print(f'Cotacao Seguro 2 Anual: {vermelho}{round(cotacaoSeguro2, 2)}{reset}')
    print()
    print(f'Cotacao Seguro 1 Trimestral: {verde}{round(cotacaoSeguro1 / 4, 2)}{reset}')
    print(f'Cotacao Seguro 2 Trimestral: {vermelho}{round(cotacaoSeguro2 / 4, 2)}{reset}')
    print()
    print(f'Cotacao Seguro 1 Mensal: {verde}{round(cotacaoSeguro1 / 12, 2)}{reset}')
    print(f'Cotacao Seguro 2 Mensal: {vermelho}{round(cotacaoSeguro2 / 12, 2)}{reset}')
else:
    print(f'Cotacao Seguro 1 Anual: {round(cotacaoSeguro1, 2)}{reset}')
    print(f'Cotacao Seguro 2 Anual: {round(cotacaoSeguro2, 2)}{reset}')
    print()
    print(f'Cotacao Seguro 1 Trimestral: {round(cotacaoSeguro1 / 4, 2)}{reset}')
    print(f'Cotacao Seguro 2 Trimestral: {round(cotacaoSeguro2 / 4, 2)}{reset}')
    print()
    print(f'Cotacao Seguro 1 Mensal: {round(cotacaoSeguro1 / 12, 2)}{reset}')
    print(f'Cotacao Seguro 2 Mensal: {round(cotacaoSeguro2 / 12, 2)}{reset}')
