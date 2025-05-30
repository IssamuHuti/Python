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
import time
import threading
import msvcrt

def limpar():
    os.system('cls')

def interromper():
    global pular
    while True:
        if msvcrt.kbhit():
            botao_interromper = msvcrt.getwch()
            if botao_interromper.lower() == 'x':
                pular = True
                break

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
            VEL = 50
            EVA = 30
            return {'HP' :HP, 'ATQ':ATQ, 'DEF':DEF, 'VEL':VEL, 'EVA':EVA}
        
        if self.profissao == 'tanque':
            HP = self.HP * 2.0 * self.tempo
            ATQ = self.ATQ * 1.2 * self.tempo
            DEF = self.DEF * 2.0 * self.tempo
            VEL = 40
            EVA = 10
            return {'HP' :HP, 'ATQ':ATQ, 'DEF':DEF, 'VEL':VEL, 'EVA':EVA}
        
        if self.profissao == 'arqueiro':
            HP = self.HP * 1.2 * self.tempo
            ATQ = self.ATQ * 2.3 * self.tempo
            DEF = self.DEF * 1.1 * self.tempo
            VEL = 30
            EVA = 50
            return {'HP' :HP, 'ATQ':ATQ, 'DEF':DEF, 'VEL':VEL, 'EVA':EVA}
        
        if self.profissao == 'assassino':
            HP = self.HP * 1.3 * self.tempo
            ATQ = self.ATQ * 2.0 * self.tempo
            DEF = self.DEF * 1.3 * self.tempo
            VEL = 60
            EVA = 40
            return {'HP' :HP, 'ATQ':ATQ, 'DEF':DEF, 'VEL':VEL, 'EVA':EVA}
            

class Combate(Atributos):
    global profissoes, movimentoCampeao, movimentoOponente

    def ataqueCampeao(self):
        if random.random() > (movimentoOponente['EVA'] / 100):
            danoOferecido = movimentoCampeao['ATQ'] - movimentoOponente['DEF']
            movimentoOponente['HP'] -= danoOferecido
        else:
            danoOferecido = 'Miss'
        return danoOferecido

    def ataqueOponente(self):
        if random.random() > (movimentoCampeao['EVA'] / 100):
            danoRecebido = movimentoOponente['ATQ'] - movimentoCampeao['DEF']
            movimentoCampeao['HP'] -= danoRecebido
        else:
            danoRecebido = 'Miss'
        return danoRecebido
    
    def atributoCampeao(self):
        if self == 1:
            personagem = p1.atributoDistribuicao()
            print(profissoes[self-1])
            for atributo, valor in p1.atributoDistribuicao().items():
                print(f'{atributo}: {valor}')
            print()
            return personagem
        
        elif self == 2:
            personagem = p2.atributoDistribuicao()
            print(profissoes[self-1])
            for atributo, valor in p2.atributoDistribuicao().items():
                print(f'{atributo}: {valor}')
            print()
            return personagem
        
        elif self == 3:
            personagem = p3.atributoDistribuicao()
            print(profissoes[self-1])
            for atributo, valor in p3.atributoDistribuicao().items():
                print(f'{atributo}: {valor}')
            print()
            return personagem
        
        elif self == 4:
            personagem = p4.atributoDistribuicao()
            print(profissoes[self-1])
            for atributo, valor in p4.atributoDistribuicao().items():
                print(f'{atributo}: {valor}')
            print()
            return personagem


rodada = 1
profissao = 'Escolha a profissão:\n1 - Guerreiro\n2 - Tanque\n3 - Arqueiro\n4 - Assassino\n=> '
profissoes = ['Guerreiro', 'Tanque', 'Arqueiro', 'Assassino']
vidaPropria = 5
vidaOponente = 5


while True:
    pular = False
    p1 = Atributos('guerreiro', rodada)
    p2 = Atributos('tanque', rodada)
    p3 = Atributos('arqueiro', rodada)
    p4 = Atributos('assassino', rodada)

    while True:
        limpar()

        try:
            atributosRodada = int(input(profissao))
            if atributosRodada in [1, 2, 3, 4]:
                break
            else:
                print('Informe uma opção válida')
                input()
        except ValueError:
            print('Digite somente as opções válidas')
            input()

    limpar()

    oponenteEscolha = random.choice([1, 2, 3, 4])
    movimentoCampeao = Combate.atributoCampeao(atributosRodada)
    movimentoOponente = Combate.atributoCampeao(oponenteEscolha)

    thread_input = threading.Thread(target=interromper)
    thread_input.daemon = True
    thread_input.start()

    limpar()
    print(f'Campeoes com vida: {vidaPropria} - Campeao {profissoes[atributosRodada-1]}')
    print(f'Oponentes com vida: {vidaOponente} - Oponente {profissoes[oponenteEscolha-1]}')
    print()

    velocidadeCampeao = movimentoCampeao['VEL']
    velocidadeOponente = movimentoOponente['VEL']

    cicloCampeao = velocidadeCampeao
    cicloOponente = velocidadeOponente
    while (movimentoCampeao['HP'] > 0) and (movimentoOponente['HP'] > 0):
        cicloCampeao = cicloCampeao + velocidadeCampeao
        if cicloCampeao >= 100:
            cicloCampeao -= 100
        cicloOponente = cicloOponente + velocidadeOponente
        if cicloOponente >= 100:
            cicloOponente -= 100

        if cicloCampeao > cicloOponente:
            vidaTirada = Combate.ataqueCampeao(profissao)
            vidaTomada = 0
        elif cicloCampeao < cicloOponente:
            vidaTirada = 0
            vidaTomada = Combate.ataqueOponente(profissao)
        else:
            vidaTirada = Combate.ataqueCampeao(profissao)
            vidaTomada = Combate.ataqueOponente(profissao)
                
        if pular == False:
            if vidaTomada != 0:
                if movimentoCampeao['HP'] <= 0:
                    print(f'Vida campeao : 0 - Dano sofrido: {vidaTomada}')
                else:
                    print(f'Vida campeao : {movimentoCampeao['HP']} - Dano sofrido: {vidaTomada}')

            if vidaTirada != 0:
                if movimentoOponente['HP'] <= 0:
                    print(f'Vida oponente: 0 - Dano sofrido: {vidaTirada}')
                else:
                    print(f'Vida oponente: {movimentoOponente['HP']} - Dano sofrido: {vidaTirada}')

            if (movimentoCampeao['HP'] <= 0) and (movimentoOponente['HP'] <= 0):
                print()
                print('Empate')
                break
            elif (movimentoOponente['HP'] <= 0) and (movimentoCampeao['HP'] > 0):
                vidaOponente -= 1
                print()
                print('Partida ganha')
                break
            elif (movimentoCampeao['HP'] <= 0) and (movimentoOponente['HP'] > 0):
                vidaPropria -= 1
                print()
                print('Partida perdida')
                break

            time.sleep(1)

        elif pular == True:
            if (movimentoCampeao['HP'] // (movimentoOponente['ATQ'] - movimentoCampeao['DEF'])) > (movimentoOponente['HP'] // (movimentoCampeao['ATQ'] - movimentoOponente['DEF'])):
                vidaOponente -= 1
                print('Partida ganha')
                break
            elif (movimentoCampeao['HP'] // (movimentoOponente['ATQ'] - movimentoCampeao['DEF'])) < (movimentoOponente['HP'] // (movimentoCampeao['ATQ'] - movimentoOponente['DEF'])):
                vidaPropria -= 1
                print('Partida perdida')
                break
            else:
                print('Empate')
                break

    if vidaOponente == 0:
        print('Guerra vencida')
        break
    elif vidaPropria == 0:
        print('Guerra perdida')
        break

    rodada += 1
    input()
