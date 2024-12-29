import os

def limpar():
    os.system('cls')

def permissao_int(mensagem):
    while True:
        x = input(mensagem)
        if x.isdigit(): 
            return int(x)
        else:
            print("Entrada inválida. Informe apenas números.")

def permissao_str(mensagem):
    while True:
        x = input(mensagem)
        if x.isalpha(): 
            return x
        else:
            print("Entrada inválida. Informe apenas caracteres.")
    
escola           = input('Colégio  : ')
enderecoEscola   = input('Endereço : ')
numeroEndereco   = permissao_int('Número   : ')
numeroDisciplina = permissao_int('Quantidade de disciplinas: ')

listaAluno      = []
listaAprovados  = []
listaReprovados = []
listaNotas      = []
listaFaltas     = []
listaDiscp      = []

nDisciplina = 1
while nDisciplina <= numeroDisciplina:
    cDisciplina = permissao_str(f'Disciplina {nDisciplina}: ')
    listaDiscp.append(cDisciplina)
    nDisciplina += 1

print()

while True:
    limpar()
    print('Informações do aluno')
    aluno           = permissao_str('Nome       : ')
    idade           = permissao_int('Idade      : ')
    serie           = permissao_int('Serie      : ')
    mensalidade     = permissao_int('Mensalidade: ')
    reprovado       = False
    qtdReprovado    = 0
    novaMensalidade = 0
    reprovadosDisp  = []
    mediaDisplina   = []
    mediaFaltas     = []

    print()
    disciplina = 1
    while disciplina <= len(listaDiscp):
        notas    = []
        faltas   = []

        bimestre = 1
        print(listaDiscp[disciplina - 1])
        while bimestre <= 4:
            nota  = permissao_int(f'Nota  {bimestre}: ')
            falta = permissao_int(f'Falta {bimestre}: ')
            notas.append(nota)
            faltas.append(falta)

            bimestre += 1
        
        print()
        
        mediaNota  = sum(notas) / 4
        mediaFalta = sum(faltas) / 4

        mediaDisplina.append(mediaNota)
        mediaFaltas.append(mediaFalta)
    
        if serie == 3:
            if mediaFalta > 6 or mediaNota < 60:
                reprovado = True
        elif serie == 4:
            if mediaFalta > 8 or mediaNota < 60:
                reprovado = True
        else:
            if mediaFalta > 8 or mediaNota < 70:
                reprovado = True

        if reprovado == True:
            qtdReprovado += 1
            reprovadosDisp.append(listaDiscp[disciplina - 1])

        disciplina += 1

    listaAluno.append(aluno)
    listaNotas.append(mediaDisplina)
    listaFaltas.append(mediaFaltas)

    novaMensalidade = mensalidade + (mensalidade * (qtdReprovado * 20 / 100))

    limpar()
    if reprovado == False:
        listaAprovados.append(aluno)
        print(f'Parabens {aluno}, você foi aprovado!')
    else:
        listaReprovados.append(aluno)
        print(f'Reprovado, a sua mensalidade para ano que vem subirá para {round(novaMensalidade, 2)} reais')
        print('Disciplinas reprovadas:')
        for d in reprovadosDisp:
            print(d)
    
    print()
    outroAluno = permissao_str('Deseja cadastrar outro aluno (S/N): ').upper()
    while outroAluno != 'S' and outroAluno != 'N':
        print('Informe somente "S" ou "N"')
        outroAluno = permissao_str('Deseja cadastrar outro aluno (S/N): ').upper()
    if outroAluno == 'N':
        limpar()
        break

print('Lista dos alunos aprovados!')
for aluno in listaAprovados:
    print(aluno)

print()
print('Alunos Reprovados...')
for aluno in listaReprovados:
    print(aluno)

