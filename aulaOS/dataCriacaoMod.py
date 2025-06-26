import os
import datetime

# confere a data de modificação do arquivo
os.chdir('aulaOS')
arquivo = 'introOS.py'
if os.path.exists(arquivo):
    horaModificao = os.path.getmtime(arquivo) # obtem a informação do horario da modificação
    dataModificacao = datetime.datetime.fromtimestamp(horaModificao) # transforma a variável numa linguagem intendível
    print('Últimas modificações', dataModificacao)

    horaCriacao = os.path.getctime(arquivo) # obtem a informação do horario da criação
    dataCriacao = datetime.datetime.fromtimestamp(horaCriacao)
    print('Data criação:', horaCriacao)
    
