from funcoes import Funções
import os


class Personagem:
    def __init__(self, nome, altura, atributo):
        self.nome = nome
        self.altura = altura
        self.atributo = atributo

    def escolhaAtributo(self):
        func = Funções(genero='')
        if self.atributo == 'Força':
            # tecla.play(-1)
            frase = f'Você escolheu {self.atributo} cabrunco, você pode se dar melhor arrastando objetos pesados!\n\n'
            func.animation(frase)

            input("aperte enter para prosseguir...")
            # tecla.stop()
            os.system('clear')
        elif self.atributo == 'Velocidade':
            # tecla.play(-1)
            frase = f'Você escolheu {self.atributo} cabrunco, você perderá menos tempo a cada escolha\n\n'
            func.animation(frase)
            # tecla.stop()
            input("aperte enter para prosseguir...")
            os.system('clear')
        elif self.atributo == 'Inteligência':
            # tecla.play(-1)
            frase = f'Você escolheu {self.atributo} cabrunco, você pensa fora da caixinha! E terá algumas dicas!\n\n'
            func.animation(frase)
            # tecla.stop()
            input("aperte enter para prosseguir...")
            os.system('clear')
        elif self.atributo == 'Sorte':
            # tecla.play(-1)
            frase = f'Você escolheu {self.atributo} cabrunco, você pode ter escolhas especiais!\n\n'
            func.animation(frase)
            # tecla.stop()
            input("aperte enter para prosseguir...")
            os.system('clear')
