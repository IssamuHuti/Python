import os
import stat

# Verifica se você tem permissão para ler, escrever ou executar um arquivo.
os.chdir('aulaOS')
arquivo = 'introOS.py'

if os.access(arquivo, os.R_OK):
    print("Você pode LER este arquivo.")
if os.access(arquivo, os.W_OK):
    print("Você pode ESCREVER neste arquivo.")
if os.access(arquivo, os.X_OK):
    print("Você pode EXECUTAR este arquivo.")

# Permite mudar permissões com base em códigos numéricos (modo octal).
os.chmod(arquivo, stat.S_IREAD)
print("Arquivo definido como somente leitura.")

os.chmod(arquivo, stat.S_IREAD | stat.S_IWRITE)
print("Arquivo agora pode ser lido e escrito.")