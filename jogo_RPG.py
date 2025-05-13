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
            EVA = self.EVA * 1.5 * self.tempo
            return [HP, ATQ, DEF, VEL, EVA]
        
        if self.profissao == 'tanque':
            HP = self.HP * 2 * self.tempo
            ATQ = self.ATQ * 1.2 * self.tempo
            DEF = self.DEF * 2 * self.tempo
            VEL = self.VEL * 1.2 * self.tempo
            EVA = self.EVA * 1.2 * self.tempo
            return [HP, ATQ, DEF, VEL, EVA]
        
        if self.profissao == 'arqueiro':
            HP = self.HP * 1.2 * self.tempo
            ATQ = self.ATQ * 2.5 * self.tempo
            DEF = self.DEF * 1.1 * self.tempo
            VEL = self.VEL * 2 * self.tempo
            EVA = self.EVA * 2 * self.tempo
            return [HP, ATQ, DEF, VEL, EVA]
            
rodada = 1
while True:
    p1 = Atributos('guerreiro', rodada)
    p2 = Atributos('tanque', rodada)
    p3 = Atributos('arqueiro', rodada)

    print(p1.atributoDistribuicao())
    print(p2.atributoDistribuicao())
    print(p3.atributoDistribuicao())

    rodada += 1
    input()
