SERÁ INFORMADO TUDO SOBRE O QUE FOR APRENDENDO SOBRE PYTHON

1 - if <condição>:
    - Uma função condicional que irá ser executado caso os casos sejam cumpridas 
    - se tiver mais de uma condicional, informar ELIF <condição>
    - Se a condição não for cumprida, a função vai seguir o código sem executar o conteúdo contido na condicional
    - se precisar informar alguma coisa caso não cumpra alguma das condições estabelecidas, usa-se ELSE
    - EXEMPLO:
        n = 2
        if n <= 10:
            print("O 'n' é menor ou igual que 10")
        elif n <= 50:
            print("O 'n' é menor ou igual que 50")
        else:
            print("O 'n' é maior que 50")

2 - for i in <tamanho do loop>, range():
    - cria uma repetição de eventos que será finalizado assim que repetir a quantidade de vezes informado
    - é possivel fazer o loop ir de forma decrescente
    - se for utilizar a função em um número, seria bom informar por qual número iria começar, e de quantos em quantos números será feita a repetição

        for i in range(1, 10, 2)
        * range é uma função utilizada para loopings
        * nesse for informa que o loop começará do número 1 até 10 de 2 em 2
        * para fazer ficar decrescente informar no for (10, 1, -2)
    
    - num for aplicado a uma string, ela percorre letra por letra da string, a menos que forneça o Len(string), o que torna ela uma numeral
    - pode ser aplicado em listas e dicionarios

3 - while <condição para parar>:
    - cria uma repetição que irá parar se cumprir com uma condição
    - quando não se sabe quantas vezes quer que esse loop aconteça, informe 'while True'
    - se precisar interromper o loop, informe break
    - se precisar retorne o loop, informe continue

4 - Len(string)
    - a função Len funciona para informar quantos dígitos uma string possui
    - comumente utilizado no for para percorrer por cada letra da string de forma numérica

5 - print(texto)
    - imprime na tela um texto
    - pode-se digitar dentro do print um texto diretamente ou informar o texto dentro de uma variável e informar a variável
    - é possível informar os números também, porém, se precisa informar um item do tipo int com uma string dentro do print, precisaria converter o item do tipo int em uma valor numeral como int ou float
    - se informar um print() vazio, ela pula uma linha 
    - se informar '\n' dentro da string na hora do texto irá pular de linha a partir da linha que foi informado

6 - input(texto)
    - cria uma abertura para que o usuário possa fornecer uma informação

7 - .upper() e .lower()
    - permite que todas as letras de uma string fiquem em maiúsculas ou minúsculas
    - aplicável no imput

8 - listas, arrays []
    - são variáveis para guardar ou acessar informações
    - para cada itens dentro das listas tem um índice que começa a partir do 0
    - para acessar um item dentro das listas informar o nome da variável representa a variável e dentro de [] informar o indice da informação desejada
    - acrescimo e retirada de itens na lista:
        - se precisar acrescentar mais itens na lista informar:
            variavel_lista.append(valor_a_acrescentar_na_lista) irá acrescentar como ultimo item da lista
        - se precisar acrescentar mais itens na lista no indice que quiser:
            variavel_lista.insert(indice, 'string') - os demais itens que estavam no indice para trás irão sofrer acrescimo no indice de 1
        - se precisar juntas duas listas em uma:
            variavel_lista.extend(outra_lista)
        - se precisar remover o item de um determinado indice:
            variavel_lista.pop(indice)
            variavel_lista.pop() - se não informar nada exclui o ultimo item da lista
        - se precisar apagar um item duplicado:
            variavel_lista.remove(item) - remove o primeiro item duplicado na lista
        - se precisar apagar toda a lista:
            variavel_lista.clear()
    - se precisar inverter a lista informe após a lista informar [::-1]

9 - .isalpha() e .isdigit()
    - são funções que são ligadas a variáveis utilizadas para verificar se dentro da variável possui somente dígitos ou números
    - geralmente utilizados como condicionais de if

10 - def nome_funcao (parametro):
    - cria uma função que vai se tornar repetitivo no programa, otimizando e diminuindo o tamanho do projeto
    - nos parametros informar uma variavel para ser manipulado dentro da função
    - exemplo:
        def soma(x, y):
            return x + y

        def duplicar(x):
            return x * 2

        def permissao_str(mensagem): *validação de input de uma string, na mensagem informa o texto para inserção de um a informação
                                     *a chamada da função acontece dentro de uma variável que chama essa função
        while True:
            x = input(mensagem)
            if x.isalpha(): 
                return x
            else:
                print("Entrada inválida. Informe apenas caracteres.")

11 - .split(parametro)
    - função que pega um texto e separa ela de acordo com o parametro
    - resultado dela entra dentro de uma lista

12 - replace(parametro):
    - substitui uma palavra dentro de um texto por outra
    - texto.replace('substituida', 'subistituiu')

13 - import <nome_do_modulo>
    - executando o import importa dados de um módulo que está salva nas funcionalidades que já veio instalado no python, ou módulos 
    importados como selenium e pandas ou de algum módulo programado 
    - se fizer a importação de todo o módulo, quando for utilizar a informação importada terá de informar o seguinte:
        * nome do módulo + '.' + a informação desejada
    - se importar com "from <modulo> import <informação>, não precisaria informar o nome do módulo na chamada da informação importada
    - fazendo a importação de todo o módulo, se informar "as" depois do módulo e informar uma abreviação, em vez de informar o nome do 
    modulo toda vez que for chamar a função pode chmar pelo apelido estabelecido
        * import pandas as pd
    