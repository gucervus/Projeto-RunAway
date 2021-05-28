from personagem import Personagem
import sys
import os
from time import sleep
from relogio import Relógio


class Funções(Personagem):
    def __init__(self, nome, altura, genero):
        super().__init__(nome, altura, genero)

    def animation(self, frase):
        for cont in frase:
            print(cont, end='')
            sys.stdout.flush()
            sleep(0.1)

    def generos(self):
        if self.genero == 'masculino':
            return 'o'
        elif self.genero == 'feminino':
            return 'a'
        else:
            return 'e'

    def tempo(self, minuto):
        personagem = Personagem(self.nome, self.altura, self.genero)
        relogio = Relógio(30)
        if personagem.velocidade == True:
            total = minuto // 2
            relogio.corretempo(total)
        else:
            relogio.corretempo(minuto)
