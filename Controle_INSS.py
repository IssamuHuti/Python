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
            return data_formatada
        except ValueError:
            print('Formato de data invalido, formato correto é "dd/mm/aaaa"')

dataAnalise         = date.today()
qtdAnalise          = permissao_int('Digite a quantidade de empregados que serão analisados: ')
qtdAnalisada        = 0
qtdAposentadosM     = 0
qtdAposentadosF     = 0
valorAposentadoriaM = 0
valorAposentadoriaF = 0
qtdIdadeAcima85M    = 0
qtdIdadeAcima85F    = 0
qtdAdmitidos2006M   = 0
qtdAdmitidos2006F   = 0
qtdAdicionalM       = 0
qtdAdicionalF       = 0
qtdReducaoM         = 0
qtdReducaoF         = 0
qtdContribuinteM    = 0
qtdContribuinteF    = 0
aposentadoriaPagarM = 0
aposentadoriaPagarF = 0

while qtdAnalisada < qtdAnalise:
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

    qtdAnalisada += 1
    idade                = dataAnalise.year - dataNascimento.year
    tempoServico         = dataDemissao.year - dataAdmissao.year
    aposentado           = False
    salarioAposentadoria = salarioBase + (salarioBase * adicionalNoturno / 100) + (salarioBase * adicionalInsalubridade / 100)

    if idade >= 59 and sexoEmpregado == 'M' and tempoServico >= 27:
        qtdAposentadosM += 1
        aposentado = True
    elif idade >= 55 and sexoEmpregado == 'F' and tempoServico >= 22:
        qtdAposentadosF += 1
        aposentado = True
    elif idade < 59 and sexoEmpregado == 'M':
        qtdContribuinteM += 1
    elif idade < 59 and sexoEmpregado == 'F':
        qtdContribuinteF += 1

    acrescimoSalario = 0
    if dataAdmissao.year <= 2010 and dataDemissao.year >= 2015:
        acrescimoSalario += 0.06
        if sexoEmpregado == 'M':
            qtdAdicionalM += 1
        elif sexoEmpregado == 'F':
            qtdAdicionalF += 1
    if dataAdmissao.year <= 2015 and dataDemissao.year >= 2010:
        acrescimoSalario -= 0.02
        if sexoEmpregado == 'M':
            qtdReducaoM += 1
        elif sexoEmpregado == 'F':
            qtdReducaoF += 1

    if aposentado == True:
        salarioAposentadoria = salarioAposentadoria + (salarioAposentadoria * acrescimoSalario)
    
        if sexoEmpregado == 'M':
            aposentadoriaPagarM += salarioAposentadoria
        elif sexoEmpregado == 'F':
            aposentadoriaPagarF += salarioAposentadoria
    
    if dataAnalise.year - dataNascimento.year > 85 and sexoEmpregado == 'M':
        qtdIdadeAcima85M += 1
    elif dataAnalise.year - dataNascimento.year > 85 and sexoEmpregado == 'F':
        qtdIdadeAcima85F += 1
    
    if dataAdmissao.year < 2006 and sexoEmpregado == 'M':
        qtdAdmitidos2006M += 1
    elif dataAdmissao.year < 2006 and sexoEmpregado == 'F':
        qtdAdmitidos2006F += 1

limpar()
print('ANALISE DOS DADOS COLETADOS')
if qtdAposentadosM == 0 and qtdAposentadosF == 0:
    print(f'Quantidade de homens aposentados: 0')
    print(f'Quantidade de mulheres aposentados: 0')
    print(f'Quantidade de homens contribuintes e seu percentual dos contribuintes: {qtdContribuinteM} - {round(qtdContribuinteM / (qtdContribuinteM + qtdContribuinteF), 2)}%')
    print(f'Quantidade de mulheres contribuintes e seu percentual dos contribuintes: {qtdContribuinteF} - {round(qtdContribuinteF / (qtdContribuinteM + qtdContribuinteF), 2)}%')
elif qtdContribuinteM == 0 and qtdContribuinteF == 0:
    print(f'Quantidade de homens aposentados e seu percentual dos aposentados: {qtdAposentadosM} - {round(qtdAposentadosM / (qtdAposentadosM + qtdAposentadosF), 2)}%')
    print(f'Quantidade de mulheres aposentados e seu percentual dos aposentados: {qtdAposentadosF} - {round(qtdAposentadosF / (qtdAposentadosM + qtdAposentadosF), 2)}%')
    print(f'Quantidade de homens contribuintes: 0')
    print(f'Quantidade de mulheres contribuintes: 0')
else:
    print(f'Quantidade de homens aposentados e seu percentual dos aposentados: {qtdAposentadosM} - {round(qtdAposentadosM / (qtdAposentadosM + qtdAposentadosF), 2)}%')
    print(f'Quantidade de mulheres aposentados e seu percentual dos aposentados: {qtdAposentadosF} - {round(qtdAposentadosF / (qtdAposentadosM + qtdAposentadosF), 2)}%')
    print(f'Quantidade de homens contribuintes e seu percentual dos contribuintes: {qtdContribuinteM} - {round(qtdContribuinteM / (qtdContribuinteM + qtdContribuinteF), 2)}%')
    print(f'Quantidade de mulheres contribuintes e seu percentual dos contribuintes: {qtdContribuinteF} - {round(qtdContribuinteF / (qtdContribuinteM + qtdContribuinteF), 2)}%')
print(f'Quantidade de homens com mais de 85 anos: {qtdIdadeAcima85M}')
print(f'Quantidade de mulheres com mais de 85 anos: {qtdIdadeAcima85F}')
print(f'Quantidade de homens que ingressaram no mercado antes de 2006: {qtdAdmitidos2006M}')
print(f'Quantidade de mulheres que ingressaram no mercado antes de 2006: {qtdAdmitidos2006F}')
print(f'Quantidade de homens que receberam algum adicional: {qtdAdicionalM}')
print(f'Quantidade de mulheres que receberam algum adicional: {qtdAdicionalF}')
print(f'Quantidade de homens que tiveram algum redução: {qtdReducaoM}')
print(f'Quantidade de mulheres que tiveram algum redução: {qtdReducaoF}')
