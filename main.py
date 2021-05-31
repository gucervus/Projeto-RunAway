from personagem import Personagem
from _firstroom.primeiraSala import salaVermelha
from _secondrom.segundaSala  import salaBranca
from funcoes import Funções
from . import Imagem
from _color.colors import cores
from time import sleep
from _clear.clear import *
import pygame


pygame.mixer.init()
pygame.mixer.music.load('trilhasuspensa.ogg')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

objeto = Imagem()
clear = Clear()
if (__name__ == "__main__"):

    clear.clearSystem()
    clear.clearAll()

    while True:

        nome = '''
                █▀█ █░█ █▄░█ ▄▀█ █░█░█ ▄▀█ █▄█
                █▀▄ █▄█ █░▀█ █▀█ ▀▄▀▄▀ █▀█ ░█░\n\n'''

        objeto.animation(nome)
        print('\n\n')
        print(' [1] - Login\n',
              '[2] - Cadastro\n\n')
        escolha = input('>> ')

        while escolha != '1' and escolha != '2':
            print('Opção inválida! tente novamente.')
            escolha = input('>> ')
        if escolha == '1' or escolha == '2':
            break
    clear.clearSystem()
    clear.clearAll()

    usuario1 = ''
    senha1 = ''
    gen = ''
    while True:
        if escolha == '1':
            print(nome)
            print("{:^60}\n\n".format("[LOGIN]"))
            usuario = input('Usuário:')
            senha = input('Senha: ')
            if usuario != usuario1 or senha != senha1:
                print("Usuário ou senha inválido\n")
                cadastro = input('Deseja se cadastrar [sim/não]? ').lower()
                clear.clearSystem()
                clear.clearAll()
                while cadastro != 'sim' and cadastro != 'nao':
                    print(nome)
                    print("{:^60}\n\n".format("[LOGIN]"))
                    cadastro = input('Deseja se cadastrar [sim/não]? ').lower()
                    clear.clearSystem()
                    clear.clearAll()
                if cadastro == 'nao':
                    print(nome)
                    print('Programa finalizado!')
                    break

                elif cadastro == 'sim':
                    print(nome)
                    print("{:^60}\n\n".format("[CADASTRO]"))
                    nome = input("Digite seu nome: ")
                    alt = float(input("Digite sua altura: "))
                    gen += input("Digite seu gênero: ").lower()
                    usuario1 += input("Usuário: ")
                    senha1 = input("Senha: ")

        elif escolha == '2':
            print(nome)
            print("{:^60}\n\n".format("[CADASTRO]"))
            nome = input("Digite seu nome: ")
            alt = float(input("Digite sua altura: "))
            gen += input("Digite seu gênero: ").lower()
            usuario1 += input("Usuário: ")
            senha1 += input("Senha: ")
            clear.clearSystem()
            clear.clearAll()

        func = Funções(genero=gen)
        tecla = func.teclando()

        tecla.play(-1)
        print(' '*25, end='')
        bemVindo = f"Bem vind{func.generos()} {usuario1}\n\n"
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

        sala1.acao()

        if sala1.gameover() == True:
            pygame.mixer.music.stop()
            teste = pygame.mixer.Sound('gameo4.ogg')
            teste.play()
            print('Fim de jogo!')
            sleep(5)
            break
        else:
            sala2.acao()
            break
