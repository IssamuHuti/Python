'''
criar um jogo estilo rpg(utilizar POO)
- vai ter 2 avatares
- cada um deles vai ter estatisticas proprias de cada atributo de acordo com a profissão
- os atributos são: ataque, vida, defesa, velocidade, evasão (posteriormente magia e defesa magica)
- profissões: guerreiro, tank, arqueiro, (posteriormente mago)
- os atributos de cada profissão será alterada de acordo com os atributos bases
- o atributo de evasão será influencida por probabilidade
- para cada ataque terá um intervalo de tempo, que será determinada pela velocidade de cada avatar escolhido
'''

import os
import random

def limpar():
    os.system('cls')

class Atributos:
    def __init__(self, profissao, tempo):
        self.profissao = profissao
        self.tempo = tempo
        self.HP = 100
        self.ATQ = 10
        self.DEF = 5
        self.VEL = 5
        self.EVA = 10

    def atributoDistribuicao(self):
        if self.profissao == 'guerreiro':
            HP = self.HP * 1.5 * self.tempo
            ATQ = self.ATQ * 1.5 * self.tempo
            DEF = self.DEF * 1.5 * self.tempo
            VEL = self.VEL * 1.5 * self.tempo
            EVA = self.EVA * 1.3 * self.tempo
            return {'HP' :HP, 'ATQ':ATQ, 'DEF':DEF, 'VEL':VEL, 'EVA':EVA}
        
        if self.profissao == 'tanque':
            HP = self.HP * 2 * self.tempo
            ATQ = self.ATQ * 1.2 * self.tempo
            DEF = self.DEF * 2 * self.tempo
            VEL = self.VEL * 1.2 * self.tempo
            EVA = self.EVA * 1.2 * self.tempo
            return {'HP' :HP, 'ATQ':ATQ, 'DEF':DEF, 'VEL':VEL, 'EVA':EVA}
        
        if self.profissao == 'arqueiro':
            HP = self.HP * 1.2 * self.tempo
            ATQ = self.ATQ * 2.5 * self.tempo
            DEF = self.DEF * 1.1 * self.tempo
            VEL = self.VEL * 2 * self.tempo
            EVA = self.EVA * 1.5 * self.tempo
            return {'HP' :HP, 'ATQ':ATQ, 'DEF':DEF, 'VEL':VEL, 'EVA':EVA}
            
rodada = 1
profissao = 'Escolha a profissão:\n1 - Guerreiro\n2 - Tanque\n3 - Arqueiro\n=> '

while True:
    p1 = Atributos('guerreiro', rodada)
    p2 = Atributos('tanque', rodada)
    p3 = Atributos('arqueiro', rodada)

    while True:
        limpar()
        atributosRodada = int(input(profissao))
        if atributosRodada in [1, 2, 3]:
            break
        else:
            print('Informe uma opção válida')
            input()

    limpar()

    if atributosRodada == 1:
        campeao = p1.atributoDistribuicao()
        print('GUERREIRO')
        for atributo, valor in p1.atributoDistribuicao().items():
            print(f'{atributo}: {valor}')
        print()

    elif atributosRodada == 2:
        campeao = p2.atributoDistribuicao()
        print('TANQUE')
        for atributo, valor in p2.atributoDistribuicao().items():
            print(f'{atributo}: {valor}')
        print()

    elif atributosRodada == 3:
        campeao = p3.atributoDistribuicao()
        print('ARQUEIRO')
        for atributo, valor in p3.atributoDistribuicao().items():
            print(f'{atributo}: {valor}')
        print()

    oponenteEscolha = random.choice([1, 2, 3])
    if oponenteEscolha == 1:
        oponente = p1.atributoDistribuicao()
        print('GUERREIRO')
        for atributo, valor in p1.atributoDistribuicao().items():
            print(f'{atributo}: {valor}')
        print()

    elif oponenteEscolha == 2:
        oponente = p2.atributoDistribuicao()
        print('TANQUE')
        for atributo, valor in p2.atributoDistribuicao().items():
            print(f'{atributo}: {valor}')
        print()

    elif oponenteEscolha == 3:
        oponente = p3.atributoDistribuicao()
        print('ARQUEIRO')
        for atributo, valor in p3.atributoDistribuicao().items():
            print(f'{atributo}: {valor}')
        print()

    rodada += 1
    input()
