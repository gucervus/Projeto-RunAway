from funcoes import Funções
import os


class Personagem:
<<<<<<< Updated upstream
    def __init__(self, nome, altura, genero):
        self.nome = nome
        self.altura = altura
        self.genero = genero
        self.forca = False
        self.velocidade = False
        self.inteligencia = False
        self.sorte = False
        self.escolha = False
=======
    def __init__(self, nome, altura, escolha):
        self.nome = nome
        self.altura = altura
        self.escolha = escolha
>>>>>>> Stashed changes

    def escolhaAtributo(self):
        func = Funções(genero='')
        if self.escolha == 'Força':
            # tecla.play(-1)
            frase = f'Você escolheu {self.escolha} cabrunco, você pode se dar melhor arrastando objetos pesados!\n\n'
            func.animation(frase)

            input("aperte enter para prosseguir...")
            # tecla.stop()
            os.system('clear')
        elif self.escolha == 'Velocidade':
            # tecla.play(-1)
            frase = f'Você escolheu {self.escolha} cabrunco, você perderá menos tempo a cada escolha\n\n'
            func.animation(frase)
            # tecla.stop()
            input("aperte enter para prosseguir...")
            os.system('clear')
        elif self.escolha == 'Inteligência':
            # tecla.play(-1)
            frase = f'Você escolheu {self.escolha} cabrunco, você pensa fora da caixinha! E terá algumas dicas!\n\n'
            func.animation(frase)
            # tecla.stop()
            input("aperte enter para prosseguir...")
            os.system('clear')
        elif self.escolha == 'Sorte':
            # tecla.play(-1)
            frase = f'Você escolheu {self.escolha} cabrunco, você pode ter escolhas especiais!\n\n'
            func.animation(frase)
            # tecla.stop()

            input("aperte enter para prosseguir...")
            os.system('clear')
