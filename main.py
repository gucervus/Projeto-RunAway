from relogio import Relógio
from personagem import Personagem
from salas import salaVermelha
from segundaSala import salaBranca
from funcoes import Funções
from CORES import cores
from time import sleep
import pygame
import sys
import os


pygame.init()
tecla = pygame.mixer.Sound('teclado.ogg')
pygame.mixer.music.load('trilhasuspensa.ogg')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

if (__name__ == "__main__"):

    print("{:^60}\n\n".format("RunAway"))
    print("{:^60}\n\n".format("[CADASTRO]"))

    nome = input("Digite seu nome: ")
    alt = float(input("Digite sua altura: "))
    gen = input("Digite seu gênero: ").lower()
    os.system('clear')
    # tecla.play(-1)
    print(' '*25, end='')
    bemVindo = f"Bem vindo {nome}\n\n"
    # func.animation(bemVindo)
    print(' '*20, end='')
    atributo = '»»»» Escolha um atributo ««««\n\n\n\n'
    # func.animation(atributo)
    # tecla.stop()

    sleep(1)
    print("Qual atributo você escolhe? \n\n",
          '[1] - Força\n',
          '[2] - Velocidade\n',
          '[3] - Inteligência\n',
          '[4] - Sorte\n\n')
    sleep(.5)

    opcao = int(input('»» '))
    print()

    if opcao == 1:
        escolha = "Força"
    elif opcao == 2:
        escolha = "Velocidade"
    elif opcao == 3:
        escolha = 'Inteligência'
    elif opcao == 4:
        escolha = "Sorte"

    personagem = Personagem(nome, alt, gen, escolha)
    func = Funções(nome, alt, gen, escolha)
    relogio = Relógio(30, nome, alt, gen, escolha)
    salas = salaVermelha(nome, alt, gen, escolha)
    sala2 = salaBranca()
    salas.chave = False
    if opcao == 1:
        # tecla.play(-1)
        frase = f'{personagem}, você pode se dar melhor arrastando objetos pesados!\n\n'
        func.animation(frase)
        # tecla.stop()
        input("aperte enter para prosseguir...")
        os.system('clear')
    elif opcao == 2:
        # tecla.play(-1)
        frase = f'{personagem}, você perderá menos tempo a cada escolha\n\n'
        func.animation(frase)
        # tecla.stop()
        input("aperte enter para prosseguir...")
        os.system('clear')
    elif opcao == 3:
        # tecla.play(-1)
        frase = f'{personagem}, você pensa fora da caixinha! E terá algumas dicas!\n\n'
        func.animation(frase)
        # tecla.stop()
        input("aperte enter para prosseguir...")
        os.system('clear')
    elif opcao == 4:
        # tecla.play(-1)
        frase = f'{personagem}, você pode ter escolhas especiais!\n\n'
        func.animation(frase)
        # tecla.stop()

        input("aperte enter para prosseguir...")
        os.system('clear')

    salas.acao()

    sala2.acao()
