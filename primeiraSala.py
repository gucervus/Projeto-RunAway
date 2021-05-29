from personagem import Personagem
from relogio import Relógio
from funcoes import Funções
from time import sleep
from CORES import cores
import os
import pygame


class salaVermelha(Funções, Personagem):

    def __init__(self, *args, genero, **kwargs):
        self.escrivaninha = False
        self.estante = False
        self.armario = False
        self.guitarra = True
        self.mesaBilhar = False
        self.chave = False
        super().__init__(*args, genero=genero, **kwargs)

    def acao(self):
        pygame.init()
        func = Funções(genero='')
        tecla = func.teclando()

        relogio = Relógio(30, self.nome, self.altura, self.atributo)

        numeroSala = False

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
        fraseAnimation = "Você acorda em uma sala com paredes vermelhas!\n\n"
        self.animation(fraseAnimation)

        fraseAnimation = f"Você consegue ver uma porta e em cima da porta, um {cores['red']}relógio {cores['limpa']}marcando {relogio.minutos} minutos,\n"
        self.animation(fraseAnimation)
        fraseAnimation = "consegue ver uma escrivaninha, um toca disco, um armário, uma guitarra e uma mesa de bilhar...\n\n"
        self.animation(fraseAnimation)
        tecla.stop()
        sleep(1)

        while True:
            escrivaninhanaparede = False
            ima = False

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
                fraseAnimation = f"Restam {relogio.minutos} minutos para escapar da sala!\n\n"
                self.animation(fraseAnimation)
                tecla.stop()

            numeroSala = True

            print("O que você deseja fazer?\n\n",
                  "[1] - Abrir a porta\n",
                  "[2] - Vasculhar a sala\n",
                  "[3] - Quebrar porta\n")

            opcao2 = int(input("»» "))
            print()

            if opcao2 == 1:

                relogio.corretempo(4)
                print("A porta está trancada...")

                if self.chave == False:
                    print("Você não tem a \033[4;31mchave\033[m! Vasculhe a sala para encontra-la")
                    print()
                else:
                    deseja = input("Você deseja usar a \033[4;31mchave\033[m[sim/não]? ")

                    if deseja == "sim":
                        print(
                            "Parabéns!! Você abriu a porta e avançou para a próxima sala!")
                        relogio.minutos += 30
                        input("Aperte enter para prosseguir...")
                        break
                    elif deseja == "nao":
                        print("Você achou melhor guardar a chave.")

                sleep(3)
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
                        relogio.corretempo(4)
                        print()
                        print("Você não encontrou nada, {}só tem lixo!{}".format(
                            cores['red'], cores['limpa']))
                        sleep(3)
                        os.system('clear')
                    elif opcEscrivaninha == 2:
                        relogio.corretempo(4)
                        print()
                        print("É uma escrivaninha bonita e resistente!")
                        sleep(3)
                        os.system('clear')
                    elif opcEscrivaninha == 3:
                        relogio.corretempo(4)

                        if self.atributo == 'Força':
                            print()
                            print("Você empurrou a escrivaninha até a parede.")
                            sleep(3)
                            escrivaninhanaparede = True
                            os.system('clear')
                        else:
                            print("Você não tem \033[33mforça\033[m para empurrar a escrivaninha!")
                            print()
                            sleep(3)
                            os.system('clear')
                    elif opcEscrivaninha == 4:

                        if escrivaninhanaparede == True:
                            print()
                            print(
                                'Você pode ver uma pequena {}saída{} de ventilação próxima ao teto.'.format(cores['red'], cores['limpa']))
                            sleep(5)
                            relogio.corretempo(4)
                            os.system('clear')
                            if self.altura >= 1.8:
                                print('Você alcança a saída, deseja subir?')
                                janelinha = int(input('1-S / 0-N >>> '))
                                if janelinha == 0:
                                    break
                                elif janelinha == 1:
                                    print('Você pode se pendurar na janela, mas não tem {}força{} para passar para o outro lado, na parede do lado oposto está escrita a seguinte mensagem:'.format(
                                        cores['amarelo'], cores['limpa']))
                                    print('{}O conhecimento liberta!{}'.format(
                                        cores['amarelo'], cores['limpa']))

                        else:
                            print()
                            print('O chão parece mais distante')
                            sleep(5)
                            relogio.corretempo(4)
                            os.system('clear')

                elif escolha == 2:
                    print('Você deseja:\n\n',
                          '[1] - Vasculhar toca disco\n',
                          '[2] - Olhar toca disco\n',
                          '[3] - Tocar o disco\n\n')

                    escolhaEstante = int(input('>> '))

                    if escolhaEstante == 1:
                        print()
                        relogio.corretempo(4)
                        print(
                            'Você descobriu a modelo do {}toca{} disco: Toca disco vinil air LP ion IT55'.format(cores['azul'], cores['limpa']))
                        sleep(3)
                        os.system('clear')
                    elif escolhaEstante == 2:
                        print()
                        print(
                            'Econtrei um vinil,esta em ótimo estado, sera que o toca disco funciona? ')
                        sleep(3)
                        relogio.corretempo(4)
                        os.system('clear')
                    elif escolhaEstante == 3:
                        relogio.corretempo(4)
                        if self.atributo == 'Inteligência':
                            print(
                                '**While my {}guitar{} gently weeps tem um lindo {}solo{}!'.format(cores['azul'], cores['limpa'], cores['amarelo', cores['limpa']]))
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
                            'Dentro do armário vc encontra um bilhete escrito: "Pare de perder {}tempo!{}'.format(cores['red'], cores['limpa']))
                        sleep(3)
                        relogio.corretempo(4)
                        os.system('clear')
                    elif escolhaArm == 2:
                        print()
                        print('Você está {}tentando{} aprender marcenaria?'.format(
                            cores['red'], cores['limpa']))
                        sleep(5)
                        relogio.corretempo(4)
                        os.system('clear')
                    elif escolhaArm == 3:
                        if self.atributo == 'Força':
                            print()
                            print("Você derrubou o Armário.")
                            print('E encontrou uma dica: {}HOJE É DIA DE ROCK BEBÊ!!!{}'.format(
                                cores['azul'], cores['limpa']))
                            sleep(3)
                            relogio.corretempo(4)
                            os.system('clear')

                        else:
                            print()
                            if ima == True:
                                print("Você conseguiu pegar a {}chave{} com o {}imã!{}".format(
                                    cores['red'], cores['limpa'], cores['azul'], cores['limpa']))
                                self.chave = True
                            else:
                                print("Você não tem {}força{} para empurrar o Armário!".format(
                                    cores['amarelo'], cores['limpa']))
                            sleep(3)
                            relogio.corretempo(4)
                            os.system('clear')
                elif escolha == 4:
                    print('É uma linda lespaul sunburn Stevie Ray signature 2001\n')

                    print('O que deseja:\n\n',
                          '[1] - Limpar a Guitarra\n',
                          '[2] - Quebrar a Guitarra\n',
                          '[3] - Tocar a Guitarra\n\n ')
                    guitarQuebrada=False

                    escolhaGuitarra = int(input('>> '))

                    if escolhaGuitarra == 1:
                        guitarQuebrada=False
                        print()
                        print('Por que isso é importante?')
                        sleep(3)
                        relogio.corretempo(4)
                        os.system('clear')
                    elif escolhaGuitarra == 2:
                        print()
                        relogio.corretempo(8)
                        print(
                            'Você quebrou a guitarra e a {}chave{} caiu embaixo do armário, procure algo para pegá-la, voce perdeu {}8 minutos{}'.format(cores['red'], cores['limpa'], cores['red'], cores['limpa']))
                        guitarQuebrada = True
                        sleep(3)
                        os.system('clear')
                    elif escolhaGuitarra == 3:
                        print()
                        relogio.corretempo(4)
                        if guitarQuebrada == True:
                            print(
                                "Você tentou tocar uma guitarra quebrada, e perdeu {}10 minutos{}".format(cores['red'], cores['limpa']))
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
                            self.chave = True
                        os.system('clear')
                elif escolha == 5:
                    print()
                    print('Tá com saudade do boteco né minha filha?\n')
                    print('Oq deseja fazer:\n\n',
                          '[1] - Jogar bilhar\n',
                          '[2] - Olhar em baixo da mesa\n\n')

                    opcMesa = int(input('>> '))

                    if opcMesa == 1:
                        print('Você decidiu jogar bilhar e perdeu {}5 minutos{}'.format(
                            cores['red'], cores['limpa']))
                        relogio.corretempo(5)
                        sleep(5)
                    elif opcMesa == 2:
                        print("Você encontrou um {}imã{}, agora consegue atrair metal".format(
                            cores['azul'], cores['limpa']))
                        relogio.corretempo(4)
                        sleep(5)
                        ima = True
                    os.system('clear')

            elif opcao2 == 3:
                if self.atributo == 'Força':
                    print()
                    print("A porta é de madeira e você conseguiu quebra-la!")
                    print("Parabéns, você é {}forte{} o suficiente para a próxima sala!".format(
                        cores['amarelo'], cores['limpa']))
                    sleep(5)
                    relogio.minutos += 30
                    os.system('clear')
                    break
                else:
                    print('Você é frac{} demais pra isso'.format(
                        self.generos()))
                    sleep(5)
                    relogio.corretempo(4)
                    os.system('clear')
