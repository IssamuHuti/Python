SERÁ INFORMADO TUDO SOBRE O QUE FOR APRENDENDO SOBRE PYTHON

1 - if <condição>
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

2 - for i in <tamanho do loop>
    - cria uma repetição de eventos que será finalizado assim que repetir a quantidade de vezes informado
    - é possivel fazer o loop ir de forma decrescente
    - se for utilizar a função em um número, seria bom informar por qual número iria começar, e de quantos em quantos números será feita a repetição

        for i in (1, 10, 2)
        * nesse for informa que o loop começará do número 1 até 10 de 2 em 2
        * para fazer ficar decrescente informar no for (10, 1, -2)
    
    - num for aplicado a uma string, ela percorre letra por letra da string, a menos que forneça o Len(string), o que torna ela uma numeral
    - pode ser aplicado em listas e dicionarios

3 - while <condição para parar>
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

9 - 