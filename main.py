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

    personagem = Personagem(nome, alt, gen)
    func = Funções(nome, alt, gen)
    relogio = Relógio(30)
    salas = salaVermelha(nome, alt, gen)
    sala2 = salaBranca()
    salas.chave = False

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
        personagem.forca += 10
        personagem.escolha = "Força"

        tecla.play(-1)
        frase = f'{personagem}, você pode se dar melhor arrastando objetos pesados!\n\n'
        func.animation(frase)
        tecla.stop()

        input("aperte enter para prosseguir...")
        os.system('clear')

    elif opcao == 2:
        personagem.velocidade += 10
        personagem.escolha = "Velocidade"

        tecla.play(-1)
        frase = f'{personagem}, você perderá menos tempo a cada escolha\n\n'
        func.animation(frase)
        tecla.stop()

        input("aperte enter para prosseguir...")
        os.system('clear')

    elif opcao == 3:
        personagem.inteligencia += 10
        personagem.escolha = 'Inteligência'

        tecla.play(-1)
        frase = f'{personagem}, você pensa fora da caixinha! E terá algumas dicas!\n\n'
        func.animation(frase)
        tecla.stop()

        input("aperte enter para prosseguir...")
        os.system('clear')

    elif opcao == 4:
        personagem.sorte += 10
        personagem.escolha = "Sorte"

        tecla.play(-1)
        frase = f'{personagem}, você pode ter escolhas especiais!\n\n'
        func.animation(frase)
        tecla.stop()

        input("aperte enter para prosseguir...")
        os.system('clear')

    print(' '*20, end='')
    print('', '__________________________')
    print(' '*20, end='')
    print('|', ' '*24, '|')
    print(' '*20, end='')
    print('|', ' '*7, ' SALA 1 ', ' '*7, '|')
    print(' '*20, end='')
    print('|__________________________|')
    print('\n'*2)

    tecla.play(-1)
    sala = "Você acorda em uma sala com paredes vermelhas!\n\n"
    # func.animation(sala)

    fraseSala1 = f"Você consegue ver uma porta e em cima da porta, um {cores['red']}relógio {cores['limpa']}marcando {relogio.minutos} minutos,\n"
    # func.animation(fraseSala1)
    fraseSala2 = "consegue ver uma escrivaninha, um toca disco, um armário, uma guitarra e uma mesa de bilhar...\n\n"
    # func.animation(fraseSala2)
    tecla.stop()
    sleep(1)

    salas.acao()

    sala2.acao()
