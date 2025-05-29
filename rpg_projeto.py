import os
import keyboard
import time

def limpar():
    os.system('cls')

class AtributosHeroi:
    def __init__(self):
        self.nivel = 1
        self.hp = 10
        self.mp = 10
        self.ataque = 10
        self.atqMag = 10
        self.defesa = 10
        self.defMagia = 10
        self.vel = 10
        self.sorte = 10
    
    def distribuicaoPontos(self, tecla):
        pontosDistribuir = 5

        while pontosDistribuir > 0:
            if tecla.name == 'q':
                self.hp += 1
                pontosDistribuir -= 1
            elif tecla.name =='w':
                self.mp += 1
                pontosDistribuir -= 1
            elif tecla.name =='e':
                self.ataque += 1
                pontosDistribuir -= 1
            elif tecla.name =='r':
                self.ataque += 1
                pontosDistribuir -= 1
            elif tecla.name =='a':
                self.defesa += 1
                pontosDistribuir -= 1
            elif tecla.name =='s':
                self.defMagia += 1
                pontosDistribuir -= 1
            elif tecla.name =='d':
                self.vel += 1
                pontosDistribuir -= 1
            elif tecla.name =='f':
                self.sorte += 1
                pontosDistribuir -= 1
            elif tecla.name == 'esc':
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
        return {'HP': hp, 'MP': mp, 'Atq.F': atqF, 'Atq.M': atqM, 'Def.F': defF, 'Def.M': defM, 'VEL': vel, 'Sorte': sorte}
    