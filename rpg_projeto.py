import os
import keyboard
import time

def limpar():
    os.system('cls')

class AtributosHeroi:
    def __init__(self):
        self.level = 1
        self.xp = 0
        self.hp = 10
        self.mp = 10
        self.ataque = 10
        self.atqMag = 10
        self.defesa = 10
        self.defMagia = 10
        self.vel = 10
        self.sorte = 10
    
    # problemas para informar os pontos de atributos para distribuição
    def aumentoNivel(self):
        self.level += 1

        pontosDistribuir = 5

        print('Distribua os pontos (pressione ESC para sair):')

        # não está diminuindo o valor dos pontosDistribuir, não está informando a quantidade de pontos a distribuir restante
        while pontosDistribuir > 0:
            print(f'Pontos a distribuir: {pontosDistribuir}')
            print('HP    (q)\nMP    (w)\nATQ.F (e)\nATQ.M (r)\nDEF.F (a)\nDEF.M (s)\nVEL   (d)\nSorte (f)')

            evento = keyboard.read_event() # cria uma variavel que recebe a informação de que anteriormente já foi feita o recebimento da insersão da tecla
            if evento.event_type == keyboard.KEY_DOWN: # cria um evento para que não permita acontecer erro de reler a tecla do loop anterior
                teclaAtribuicao = keyboard.read_key()

                if teclaAtribuicao == 'q':
                    self.hp += 1
                    pontosDistribuir -= 1
                elif teclaAtribuicao == 'w':
                    self.mp += 1
                    pontosDistribuir -= 1
                elif teclaAtribuicao == 'e':
                    self.ataque += 1
                    pontosDistribuir -= 1
                elif teclaAtribuicao == 'r':
                    self.atqMag += 1
                    pontosDistribuir -= 1
                elif teclaAtribuicao == 'a':
                    self.defesa += 1
                    pontosDistribuir -= 1
                elif teclaAtribuicao == 's':
                    self.defMagia += 1
                    pontosDistribuir -= 1
                elif teclaAtribuicao == 'd':
                    self.vel += 1
                    pontosDistribuir -= 1
                elif teclaAtribuicao == 'f':
                    self.sorte += 1
                    pontosDistribuir -= 1
                elif teclaAtribuicao == 'esc':
                    print(f'Pontos a distribuir restantes: {pontosDistribuir}')
                    break

    def conversaoAtributos(self):
        hp = self.hp * 10
        mp = self.mp * 5
        atqF = self.ataque * 3
        atqM = self.atqMag * 3
        defF = self.defesa * 2
        defM = self.defMagia * 2
        vel = self.vel * 2
        sorte = self.sorte * 1
        return {'Level': self.level,
            'HP': hp, 
            'MP': mp, 
            'Atq.F': atqF, 
            'Atq.M': atqM, 
            'Def.F': defF, 
            'Def.M': defM, 
            'VEL': vel, 
            'Sorte': sorte
        }
    
    def xpUp(self):
        xp = self.xp
        xp += 50

        if xp >= 100:
            xp -= 100
            self.level += 1
        
        return {'Level': self.level, 'XP': self.xp}

    
while True:
    heroi = AtributosHeroi()
    heroi.aumentoNivel()
    experienciaHeroi = heroi.xpUp()
    atributoHeroi = heroi.conversaoAtributos()

    print(f'LEVEL: {experienciaHeroi['Level']}')
    print(f'XP: {experienciaHeroi['XP']}')
    print('\nAtributos Heroi:')
    for atributo, valor in atributoHeroi.items():
        print(f'{atributo}: {valor}')

    input()
