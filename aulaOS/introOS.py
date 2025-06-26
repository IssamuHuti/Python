import os

# verificação diretorio
diretorioAtual = os.getcwd() # retorna o diretório atual
print(diretorioAtual)

# explorando arquivos dentro do diretório
conteudo = os.listdir() # Lista os arquivos e pastas no diretório atual
print('Conteudo pasta:')
for i in conteudo:
    print('- ', i)

# criando nova pasta no diretório
nomePasta = 'exemplo'
os.chdir('aulaOS') # altera o diretorio para subpasta aulaOS
if not os.path.exists(nomePasta): # .exists = confirma se a pasta informada existe
    os.mkdir(nomePasta) # cria nova pasta no mesmo diretório com nome informada
    print(f'Pasta {nomePasta} criada com sucesso')
else:
    print(f'Pasta {nomePasta} já existe')
os.chdir('..') # retorna para o diretorio anterior, que no caso seria o diretorio inicial

# altera o diretorio para pasta selecionada que esteja dentro do diretório
# os.chdir('exemplo') # a pasta informada precisa existir
# print('Agora estamos em:', os.getcwd())

try:
    os.remove('teste.txt') # remove o arquivo dentro do diretório # o arquivo precisa existir para remover
    print('Arquivo teste.txt foi removido')
except:
    print('Arquivo teste.txt não existe')

# remover pasta vazia
os.mkdir('pastaVazia')
if os.path.exists('pastaVazia'):
    os.rmdir('pastaVazia') # remoção da pasta vazia # precisa estar com pasta vazia
    print('Pasta removida')

# renomear arquivo ou pasta
# os.rename('exemplo', 'definitivo')
# print('Pasta exemplo -> definitivo')

# Retorna o tamanho do arquivo em bytes
arquivo = "Boletim.py"
if os.path.exists(arquivo):
    tamanho = os.path.getsize(arquivo)
    print(f"Tamanho de {arquivo}: {tamanho} bytes")
