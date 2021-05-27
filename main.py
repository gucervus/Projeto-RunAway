from relogio import Relógio
from personagem import Personagem
from salas import salaVermelha
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

    def animation(a, b):
        for cont in a:
            print(cont, end='')
            if b == 1:
                sys.stdout.flush()
                sleep(0.1)
            elif b == 2:
                sys.stdout.flush()
                sleep(0.2)

    def genero(gen):
        if gen == 'masculino':
            return 'o'
        elif gen == 'feminino':
            return 'a'

    def tempo(minuto):
        if personagem.velocidade == 10:
            total = minuto // 2
            relogio.corretempo(total)
        else:
            relogio.corretempo(minuto)
    os.system('clear')

    print("{:^60}\n\n".format("RunAway"))
    print("{:^60}\n\n".format("[CADASTRO]"))

    nome = input("Digite seu nome: ")
    gen = input("Digite seu gênero: ").lower()
    alt = float(input("Digite sua altura: "))
    os.system('clear')

    tecla.play(-1)
    print(' '*25, end='')
    bemVindo = f"Bem vind{genero(gen)} {nome}\n\n"
    animation(bemVindo, 1)
    print(' '*20, end='')
    atributo = '»»»» Escolha um atributo ««««\n\n\n\n'
    animation(atributo, 1)
    tecla.stop()

    personagem = Personagem(nome, gen, alt)
    relogio = Relógio(30)
    salas = salaVermelha()
    salas.chave = False

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
        animation(frase, 1)
        tecla.stop()

        input("aperte enter para prosseguir...")
        os.system('clear')

    elif opcao == 2:
        personagem.velocidade += 10
        personagem.escolha = "Velocidade"

        tecla.play(-1)
        frase = f'{personagem}, você perderá menos tempo a cada escolha\n\n'
        animation(frase, 1)
        tecla.stop()

        input("aperte enter para prosseguir...")
        os.system('clear')

    elif opcao == 3:
        personagem.inteligencia += 10
        personagem.escolha = 'Inteligência'

        tecla.play(-1)
        frase = f'{personagem}, você pensa fora da caixinha! E terá algumas dicas!\n\n'
        animation(frase, 1)
        tecla.stop()

        input("aperte enter para prosseguir...")
        os.system('clear')

    elif opcao == 4:
        personagem.sorte += 10
        personagem.escolha = "Sorte"

        tecla.play(-1)
        frase = f'{personagem}, você pode ter escolhas especiais!\n\n'
        animation(frase, 1)
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
    animation(sala, 1)

    fraseSala1 = f"Você consegue ver uma porta e em cima da porta, um {cores['red']}relógio {cores['limpa']}marcando {relogio.minutos} minutos,\n"
    animation(fraseSala1, 1)
    fraseSala2 = "consegue ver uma escrivaninha, um toca disco, um armário, uma guitarra e uma mesa de bilhar...\n\n"
    animation(fraseSala2, 1)
    tecla.stop()
    sleep(1)

    numeroSala = False
    while True:

        if numeroSala == True:

            tecla.play()
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
            contador = f"Restam {relogio.minutos} minutos para escapar da sala!\n\n"
            animation(contador, 1)
            tecla.stop()

        numeroSala = True

        print("O que você deseja fazer?\n\n",
              "[1] - Abrir a porta\n",
              "[2] - Vasculhar a sala\n",
              "[3] - Quebrar porta\n")

        opcao2 = int(input("»» "))
        print()

        if opcao2 == 1:

            tempo(1)
            print("A porta está trancada...")

            if salas.chave == False:
                print("Você não tem a chave! Vasculhe a sala para encontra-la")
                print()
            else:
                deseja = input("Você deseja usar a chave[sim/não]? ")

                if deseja == "sim":
                    print(
                        "Parabéns!! Você abriu a porta e avançou para a próxima sala!")
                    relogio.minutos += 30
                    input("Aperte enter para prosseguir...")
                    break
                elif deseja == "nao":
                    print("Você achou melhor guardar a chave.")

            sleep(5)
            os.system('clear')

        elif opcao2 == 2:

            sleep(1)
            print("Qual item deseja vasculhar?\n\n",
                  "[1] - Escrivaninha\n",
                  "[2] - Toca disco\n",
                  "[3] - Armário\n",
                  "[4] - Guitarra\n",
                  "[5] - Mesa de bilhar\n")

            sleep(1)
            print()
            escolha = int(input('>> '))
            print()

            if escolha == 1:

                print("Você deseja: \n\n",
                      "[1] - Vasculhar Escrivaninha\n",
                      "[2] - Olhar Escrivaninha\n",
                      "[3] - Empurrar Escrivaninha\n",
                      "[4] - Subir na Escrivaninha\n",)

                opcEscrivaninha = int(input(">> "))

                if opcEscrivaninha == 1:
                    tempo(4)
                    print()
                    print("Você não encontrou nada, só tem lixo!")
                    sleep(5)
                    os.system('clear')
                elif opcEscrivaninha == 2:
                    tempo(4)
                    print()
                    print("É uma escrivaninha bonita e resistente!")
                    sleep(5)
                    os.system('clear')
                elif opcEscrivaninha == 3:
                    tempo(4)

                    if personagem.forca == 10:
                        print()
                        print("Você empurrou a escrivaninha até a parede.")
                        sleep(5)
                        escrivaninhanaparede = True
                        os.system('clear')
                    else:
                        print("Você não tem força para empurrar a escrivaninha!")
                        print()
                        sleep(5)
                        os.system('clear')
                elif opcEscrivaninha == 4:

                    if escrivaninhanaparede == True:
                        print()
                        print(
                            'Você pode ver uma pequena saida de ventilação próxima ao teto.')
                        sleep(5)
                        tempo(4)
                        os.system('clear')
                    else:
                        print()
                        print('O chão parece mais distante')
                        sleep(5)
                        tempo(4)
                        os.system('clear')

            elif escolha == 2:
                print('Você deseja:\n\n',
                      '[1] - Vasculhar toca disco\n',
                      '[2] - Olhar toca disco\n',
                      '[3] - Tocar o disco\n\n')

                escolhaEstante = int(input('>> '))

                if escolhaEstante == 1:
                    print()
                    tempo(4)
                    print(
                        'Você descobriu a modelo do toca disco: Toca disco vinil air LP ion IT55')
                    sleep(5)
                    os.system('clear')
                elif escolhaEstante == 2:
                    print()
                    print(
                        'Econtrei um vinil,esta em ótimo estado, sera que o toca disco funciona? ')
                    sleep(5)
                    tempo(4)
                    os.system('clear')
                elif escolhaEstante == 3:
                    tempo(4)
                    if personagem.inteligencia == 10:
                        print('**While my guitar gently weeps tem um lindo solo!')
                    else:
                        print('O toca disco não funciona!')

                    os.system('clear')
            elif escolha == 3:
                print('Você deseja:\n\n',
                      '[1] - Abrir o armário\n',
                      '[2] - Olhar o armário\n',
                      '[3] - Empurrar o armário\n\n')

                escolhaArm = int(input('>> '))

                if escolhaArm == 1:
                    print()
                    print(
                        'Dentro do armário vc encontra um bilhete escrito: "Pare de perder tempo!')
                    sleep(5)
                    tempo(4)
                    os.system('clear')
                elif escolhaArm == 2:
                    print()
                    print('Você está tentando aprender marcenaria?')
                    sleep(5)
                    tempo(4)
                    os.system('clear')
                elif escolhaArm == 3:
                    if personagem.forca == 10:
                        print()
                        print("Você derrubou o Armário.")
                        print('E encontrou uma dica: {}HOJE É DIA DE ROCK BEBÊ!!!{}'.format(
                            cores['azul'], cores['limpa']))
                        sleep(5)
                        tempo(4)
                        os.system('clear')

                    else:
                        print()
                        if ima == True:
                            print("Você conseguiu pegar a chave com o imã!")
                            salas.chave = True
                        else:
                            print("Você não tem força para empurrar o Armário!")
                        sleep(5)
                        tempo(4)
                        os.system('clear')
            elif escolha == 4:
                print('É uma linda lespaul sunburn Stevie Ray signature 2001\n')

                print('O que deseja:\n\n',
                      '[1] - Limpar a Guitarra\n',
                      '[2] - Quebrar a Guitarra\n',
                      '[3] - Tocar a Guitarra\n\n ')

                escolhaGuitarra = int(input('>> '))

                if escolhaGuitarra == 1:
                    print()
                    print('Por que isso é importante?')
                    sleep(5)
                    tempo(4)
                    os.system('clear')
                elif escolhaGuitarra == 2:
                    print()
                    tempo(8)
                    print(
                        'Você quebrou a guitarra e a chave caiu embaixo do armário, procure algo para pegá-la, voce perdeu 8 minutos')
                    guitarQuebrada = True
                    sleep(5)
                    os.system('clear')
                elif escolhaGuitarra == 3:
                    print()
                    tempo(4)
                    if guitarQuebrada == True:
                        print(
                            "Você tentou tocar uma guitarra quebrada, e perdeu 10 minutos")
                    else:
                        print(
                            'Que música linda! Os deuses do rock estão satisfeitos...')
                        sleep(.5)
                        print('.')
                        sleep(.5)
                        print('.')
                        sleep(.5)
                        print('.')
                        sleep(.5)
                        print('.')
                        sleep(.5)
                        print('.')
                        print('Uma chave caiu em sua cabeça!')
                        sleep(5)
                        salas.chave = True
                    os.system('clear')
            elif escolha == 5:
                print()
                print('Tá com saudade do boteco né minha filha?\n')
                print('Oq deseja fazer:\n\n',
                      '[1] - Jogar bilhar\n',
                      '[2] - Olhar em baixo da mesa\n\n')

                opcMesa = int(input('>> '))

                if opcMesa == 1:
                    print('Você decidiu jogar bilhar e perdeu 5 minutos')
                    tempo(5)
                    sleep(5)
                elif opcMesa == 2:
                    print("Você encontrou um imã, agora consegue atrair metal")
                    tempo(4)
                    sleep(5)
                    ima = True
                os.system('clear')

        elif opcao2 == 3:
            if personagem.forca == 10:
                print()
                print("A porta é de madeira e você conseguiu quebra-la!")
                print("Parabéns, você é forte o suficiente para a próxima sala!")
                personagem.forca -= 2
                sleep(5)
                relogio.minutos += 30
                os.system('clear')
                break

            else:
                print('Você é frac{} demais pra isso'.format(genero(gen)))
                sleep(5)
                tempo(4)
                os.system('clear')

    sala = ""
