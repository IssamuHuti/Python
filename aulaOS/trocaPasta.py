import os

# percorre todos os diretorios e subdiretórios a partir de um caminho inicial
# lista todos os arquivos .py que está dentro da pasta raiz menos os arquivos da pasta venv
pastaIgnorar = ['venv']
for raiz, pastas, arquivos in os.walk("."):
    pastas[:] = [p for p in pastas if 'venv' not in p]

    for arquivo in arquivos:
        if arquivo.endswith(".py"):
            print("Arquivo encontrado:", os.path.join(raiz, arquivo))

# alterando o diretório
print('Diretorio inicial:', os.getcwd())
os.chdir('aulaOS') # altera o diretório para subpasta desejada
print('Diretorio alterado:', os.getcwd())

# como o diretorio foi alterado, se pedir para criar uma pasta dentro do diretorio sera criada dentro do novo diretorio
# novaPasta = 'pastaNova'
# if not os.path.exists(novaPasta):
#     os.mkdir(novaPasta)

os.chdir('..')
print('Diretorio voltou para o inicial:', os.getcwd())

# Cria todas as pastas necessárias no caminho, mesmo que sejam várias subpastas que ainda não existem
os.chdir('aulaOS')
novoCaminho = 'projetos/nivel1/nivel2'
if not os.path.exists(novoCaminho):
    os.makedirs(novoCaminho)
    print(f'Pasta {novoCaminho} criada com sucesso')
else:
    print('Caminho já existe')
