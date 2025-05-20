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
        botao_interromper = input()
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
            VEL = self.VEL * 1.5 * self.tempo
            EVA = 30
            return {'HP' :HP, 'ATQ':ATQ, 'DEF':DEF, 'VEL':VEL, 'EVA':EVA}
        
        if self.profissao == 'tanque':
            HP = self.HP * 2.0 * self.tempo
            ATQ = self.ATQ * 1.2 * self.tempo
            DEF = self.DEF * 2.0 * self.tempo
            VEL = self.VEL * 1.2 * self.tempo
            EVA = 10
            return {'HP' :HP, 'ATQ':ATQ, 'DEF':DEF, 'VEL':VEL, 'EVA':EVA}
        
        if self.profissao == 'arqueiro':
            HP = self.HP * 1.2 * self.tempo
            ATQ = self.ATQ * 2.3 * self.tempo
            DEF = self.DEF * 1.1 * self.tempo
            VEL = self.VEL * 2.0 * self.tempo
            EVA = 50
            return {'HP' :HP, 'ATQ':ATQ, 'DEF':DEF, 'VEL':VEL, 'EVA':EVA}
            

class Combate(Atributos):
    def ataqueProprio(self):
        if random.random() > (oponente['EVA'] / 100):
            danoOferecido = campeao['ATQ'] - oponente['DEF']
            oponente['HP'] -= danoOferecido
        else:
            danoOferecido = 0
            print('Miss')
        return danoOferecido

    def ataqueOponente(self):
        if random.random() > (campeao['EVA'] / 100):
            danoRecebido = oponente['ATQ'] - campeao['DEF']
            campeao['HP'] -= danoRecebido
        else:
            danoRecebido = 0
            print('Miss')
        return danoRecebido


rodada = 1
profissao = 'Escolha a profissão:\n1 - Guerreiro\n2 - Tanque\n3 - Arqueiro\n=> '
profissoes = ['Guerreiro', 'Tanque', 'Arqueiro']
vidaPropria = 5
vidaOponente = 5


while True:
    pular = False
    p1 = Atributos('guerreiro', rodada)
    p2 = Atributos('tanque', rodada)
    p3 = Atributos('arqueiro', rodada)

    while True:
        limpar()
        try:
            atributosRodada = int(input(profissao))
            if atributosRodada in [1, 2, 3]:
                break
            else:
                print('Informe uma opção válida')
                input()
        except ValueError:
            print('Digite somente as opções válidas')
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

    while (campeao['HP'] > 0) and (oponente['HP'] > 0):

        thread_input = threading.Thread(target=interromper)
        thread_input.daemon = True
        thread_input.start()

        print(f'Campeoes com vida: {vidaPropria}')
        print(f'Campeao Time: {profissoes[atributosRodada-1]} - HP: {round(campeao['HP'], 0)}')
        print()
        print(f'Oponentes com vida: {vidaOponente}')
        print(f'Campeao inimigo: {profissoes[oponenteEscolha-1]} - HP: {round(oponente['HP'], 0)}')
        print()

        vidaTirada = Combate.ataqueProprio(profissao)
        vidaTomada = Combate.ataqueOponente(profissao)

        if pular == False:
            print(f'Vida campeao: {campeao['HP']} - Dano sofrido: {vidaTomada}')
            print(f'Vida oponente: {oponente['HP']} - Dano sofrido: {vidaTirada}')

            if (campeao['HP'] <= 0) and (oponente['HP'] <= 0):
                print('Empate')
                break
            elif (oponente['HP'] <= 0) and (campeao['HP'] > 0):
                vidaOponente -= 1
                print('Partida ganha')
                break
            elif (campeao['HP'] <= 0) and (oponente['HP'] > 0):
                vidaPropria -= 1
                print('Partida perdida')
                break

            time.sleep(1)
            limpar()

        elif pular == True:
            if (campeao['HP'] // (oponente['ATQ'] - campeao['DEF'])) > (oponente['HP'] // (campeao['ATQ'] - oponente['DEF'])):
                vidaOponente -= 1
                print('Partida ganha')
                break
            elif (campeao['HP'] // (oponente['ATQ'] - campeao['DEF'])) < (oponente['HP'] // (campeao['ATQ'] - oponente['DEF'])):
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
