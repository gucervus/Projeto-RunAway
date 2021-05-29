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

    func = Funções(genero=gen)
    tecla = func.teclando()

    tecla.play(-1)
    print(' '*25, end='')
    bemVindo = f"Bem vind{func.generos()} {nome}\n\n"
    func.animation(bemVindo)
    print(' '*20, end='')
    atributo = '»»»» Escolha um atributo ««««\n\n\n\n'
    func.animation(atributo)
    tecla.stop()

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
        atributo = "Força"
    elif opcao == 2:
        atributo = "Velocidade"
    elif opcao == 3:
        atributo = 'Inteligência'
    elif opcao == 4:
        atributo = "Sorte"

    personagem = Personagem(nome, alt, atributo)

    salas = salaVermelha(nome=nome, altura=alt, atributo=atributo, genero=gen)
    sala2 = salaBranca(nome=nome, altura=alt, atributo=atributo, genero=gen)
    personagem.escolhaAtributo()

    # salas.acao()

    sala2.acao()
