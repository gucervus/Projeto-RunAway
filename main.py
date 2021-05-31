from PIL import Image
from relogio import Relógio
from personagem import Personagem
from primeiraSala import salaVermelha
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
    login = input("Ja tem uma conta? ")
    os.system('clear')
    usuario1 = ''
    senha1 = ''
    gen = ''
    while True:
        if login == 'sim':
            print("{:^60}\n\n".format("RunAway"))
            print("{:^60}\n\n".format("[LOGIN]"))
            usuario = input('Usuário:')
            senha = input('Senha: ')
            if usuario != usuario1 or senha != senha1:
                print("Usuário ou senha inválido\n")
                cadastro = input('Deseja se cadastrar?')
                os.system('clear')
                while cadastro != 'sim' and cadastro != 'nao':
                    print("{:^60}\n\n".format("RunAway"))
                    print("{:^60}\n\n".format("[LOGIN]"))
                    cadastro = input('Deseja se cadastrar?')
                    os.system('clear')
                if cadastro == 'nao':

                    print('Programa finalizado!')
                    break

                elif cadastro == 'sim':
                    print("{:^60}\n\n".format("RunAway"))
                    print("{:^60}\n\n".format("[CADASTRO]"))
                    nome = input("Digite seu nome: ")
                    alt = float(input("Digite sua altura: "))
                    gen += input("Digite seu gênero: ").lower()
                    usuario1 += input("Usuário: ")
                    senha1 += input("Senha: ")

        elif login == 'nao':
            print("{:^60}\n\n".format("RunAway"))
            print("{:^60}\n\n".format("[CADASTRO]"))
            nome = input("Digite seu nome: ")
            alt = float(input("Digite sua altura: "))
            gen += input("Digite seu gênero: ").lower()
            usuario1 += input("Usuário: ")
            senha1 += input("Senha: ")
        os.system('clear')

        func = Funções(genero=gen)
        tecla = func.teclando()

        tecla.play(-1)
        print(' '*25, end='')
        bemVindo = f"Bem vind{func.generos()} {nome}\n\n"
        func.animation(bemVindo)
        print(' '*20, end='')
        atributo = '»»»» Escolha um \033[33matributo\033[m ««««\n\n\n\n'
        func.animation(atributo)
        tecla.stop()

        sleep(1)
        print("Qual \033[33matributo\033[m você escolhe? \n\n",
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

        sala1 = salaVermelha(nome=nome, altura=alt,
                             atributo=atributo, genero=gen)

        sala2 = salaBranca(nome=nome, altura=alt,
                           atributo=atributo, genero=gen)
        personagem.escolhaAtributo()

        # sala1.acao()

        sala2.acao()
