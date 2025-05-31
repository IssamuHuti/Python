import os
import keyboard
import time

def limpar():
    os.system('cls')

class AtributosHeroi:
    def __init__(self):
        self.level = 1
        self.hp = 10
        self.mp = 10
        self.ataque = 10
        self.atqMag = 10
        self.defesa = 10
        self.defMagia = 10
        self.vel = 10
        self.sorte = 10
    
    def distribuicaoPontos(self):
        pontosDistribuir = 5

        print('Distribua os pontos (pressione ESC para sair):')
        print('HP (q)\nMP (w)\nATQ.F (e)\nATQ.M (r)\nDEF.F (a)\nDEF.M (s)\nVEL (d)\nSorte (f)')

        while pontosDistribuir > 0:
            if keyboard.is_pressed('q'):
                self.hp += 1
                pontosDistribuir -= 1
            elif keyboard.is_pressed('w'):
                self.mp += 1
                pontosDistribuir -= 1
            elif keyboard.is_pressed('e'):
                self.ataque += 1
                pontosDistribuir -= 1
            elif keyboard.is_pressed('r'):
                self.atqMag += 1
                pontosDistribuir -= 1
            elif keyboard.is_pressed('a'):
                self.defesa += 1
                pontosDistribuir -= 1
            elif keyboard.is_pressed('s'):
                self.defMagia += 1
                pontosDistribuir -= 1
            elif keyboard.is_pressed('d'):
                self.vel += 1
                pontosDistribuir -= 1
            elif keyboard.is_pressed('f'):
                self.sorte += 1
                pontosDistribuir -= 1
            elif keyboard.is_pressed('esc'):
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
    
heroi = AtributosHeroi()
heroi.level += 1
heroi.distribuicaoPontos()
atributoHeroi = heroi.conversaoAtributos()

print('\nAtributos Heroi:')
for atributo, valor in atributoHeroi.items():
    print(f'{atributo}: {valor}')
