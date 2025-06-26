import os

# junta o caminho da pasta com outra pasta ou arquivo e exibe como um caminho para o acesso da pasta ou arquivo
pasta = "exemplo"
arquivo = "main.py"

caminho = os.path.join(pasta, arquivo)
print("Caminho combinado:", caminho)


# Converte um caminho relativo em caminho absoluto.
relativo = caminho
absoluto = os.path.abspath(relativo) # pega desde a raiz onde está salva o arquivo
print('Caminho absoluto:', absoluto)

# retornar o nome do arquivo e o caminho para chegar nela de forma separada
print('Arquivo:', os.path.basename(caminho)) # retorna só o nome do arquivo
print('Diretório:', os.path.dirname(caminho)) # retorna só o caminho da pasta

# Separa o nome do arquivo da extensão.
nome, extensao = os.path.splitext(arquivo)
print('Nome:', nome)
print('Extensao:', extensao)

# Verifica se um caminho é um arquivo ou uma pasta
caminho1 = 'exemplo.txt'
caminho2 = 'projetos'
if os.path.isfile(caminho2):
    print(f'{caminho2} é um arquivo')
elif os.path.isdir(caminho2):
    print(f'{caminho2} é uma pasta')
else:
    print('Arquivo não identificado')
