import os
from datetime import datetime, date

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

login = 'ADMIN'
senha = '123mudar'
dataHoje = date.today()

while True:
    limpar()
    digitarLogin = permissao_str('Login: ')
    digitarSenha = input('Senha: ')

    if (digitarLogin.upper() == login) and (digitarSenha == senha):
        break
    else:
        if digitarLogin.upper() != login:
            print('Login inexistente')
        if digitarSenha != senha:
            print('Senha Incorreta')
        input()

while True:
    while True:
        limpar()
        opcao = permissao_int('(1) Efetuar pedidos - (2) Sair ')
        if opcao != 1 and opcao != 2:
            print('Digite somente (1) ou (2)')
            input()
        else:
            break
    
    numeroPedido = 0
    if opcao == 1:
        limpar()
        numeroPedido += 1
        cliente = permissao_str('Cliente: ')
        dataServico = preenchimento_data('Data da ordem: ')
        tecnico = permissao_str('Tecnico: ')
        descricaoEquip = permissao_str('Descrição do equipamento: ')
        dataCompra = preenchimento_data('Data da compra: ')
        diferencaData = abs(datetime.strptime(dataCompra, '%d/%m/%Y') - datetime.strptime(dataHoje, '%d/%m/%Y').days)
        limiteCredito = permissao_float('Limite de crédito: ')
        while True:
            entrega = permissao_str('Entrega? (S/N)')
            if entrega.upper() != 'S' and entrega.upper() != 'N':
                print('Digite somente "S" ou "N"')
                input()
            else:
                break
        
        if entrega == 'S':
            limpar()
            print('Informe os dados para entrega')
            endereco = permissao_str('Endereço: ')
            bairro = permissao_str('Bairro: ')
            referencia = permissao_str('Referencia: ')
            telefone = permissao_int('Telefone para contato: ')
            taxa = 3

        totalGasto = 0
        while totalGasto <= limiteCredito:
            limpar()
            opcaoCliente = permissao_str('Deseja comprar produto (P) ou contratar serviço (S)')
            if opcaoCliente.upper() != 'P' and opcaoCliente != 'S':
                print('Informe somente "P" ou "S"')
                input
            else:
                break

            if opcaoCliente == 'P':
                descicaoP = permissao_str('Produto: ')
                qtdProduto = permissao_int('Quantidade: ')
                precoUnit = permissao_float('Preço por unidade: ')
                descProduto = permissao_float('Desconto(%): ')
                precoProduto = (precoUnit * qtdProduto) - (precoUnit * qtdProduto * descProduto / 100)
                print(f'Preço total = {precoProduto}')
                if diferencaData <= 730:
                    totalGasto += 0
                    print('Coberto pela garantia!')
                else:
                    totalGasto += precoProduto                

            elif opcaoCliente == 'S':
                descricaoS = permissao_str('Serviço: ')
                servicoPreco = permissao_float('Preço do serviço: ')
                descServico = permissao_float('Desconto(%): ')
                comissao = permissao_float('Comissão(%): ')
                precoServico = (servicoPreco * descServico / 100) + (servicoPreco * comissao / 100)
                print(f'Preço total = {precoServico}')
                if diferencaData <= 365:
                    totalGasto += 0
                    print('Coberto pela garantia!')
                else:
                    totalGasto += precoServico
            
            if totalGasto > limiteCredito:
                print('Limite de credito ultrapassado, chame o supervisor para liberar a ultima compra')
                input()
                loginS = 'SUPERVISOR'
                senhaS = '123LIBERA'
                loginSupervisor = permissao_str('Informe o login do supervisor: ')
                senhaSupervisor = input('Senha do supervisor: ')
                if loginSupervisor != loginS and senhaSupervisor != senhaS:
                    print('Login ou Senha incorreta, a ultima operação será excluida')
                    if opcaoCliente == 'P':
                        totalGasto -= precoProduto
                    elif opcaoCliente == 'S':
                        totalGasto -= precoServico
                else:
                    print('Permissão concedida!')
                    input()
                    break

            print(f'Total acumulado: {totalGasto}')
            print(f'Limite de gastos: {limiteCredito}')

        print()
        while True:
            limpar()
            print(f'Total da compra: {totalGasto}')
            print(f'Frete: {totalGasto * entrega / 100}')
            print(f'Valor total: {totalGasto + (totalGasto * entrega / 100)}')
            pagamento = permissao_str('Qual a forma de pagamento? (D) Dinheiro - (C) Cheque - (K) Cartão')
            if pagamento.upper() != 'D' and pagamento.upper() != 'C' and pagamento.upper() != 'K':
                print('Informe somente as opções (D) Dinheiro - (C) Cheque - (K) Cartão')
                pagamento = permissao_str('Qual a forma de pagamento? (D) Dinheiro - (C) Cheque - (K) Cartão')
            else:
                break
        
        limpar()
        if totalGasto == 0:
            print('A garantia está cobrindo toda a operação')
            print()
            print('Informe os dados para emissão de nota')
            while True:
                cnpj = permissao_int('CNPJ: ')
                if len(str(cnpj)) != 14:
                    print('Digite o CNPJ corretamente')
                else:
                    break
            print(f'NFE: {numeroPedido}')
            print(f'Data de emissão: {dataHoje}')
        
        else:
            print('Informe os dados para emissão de nota')
            while True:
                cnpj = permissao_int('CNPJ: ')
                if len(str(cnpj)) != 14:
                    print('Digite o CNPJ corretamente')
                else:
                    break
            print(f'NFE: {numeroPedido}')
            print(f'Data de emissão: {dataHoje}')

        limpar()
        print(f'NFE: {numeroPedido}')
        print(f'Data da emissão: {dataHoje}')
        print(f'Cliente: {cliente}')
        print(f'CNPJ: {cnpj}')
        if totalGasto == 0:
            print('Compra coberta pela garantia')
        else:
            print(f'Valor total: {totalGasto}')
        if opcaoCliente == 'S':
            print(f'Comissão: {comissao}')
        if entrega == 'S':
            print(f'Frete: {totalGasto * entrega / 100}')

    else:
        break
