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
        guitarQuebrada = False
        pygame.init()

        func = Funções(genero='')
        tecla = func.teclando()

        relogio = Relógio(30, self.nome, self.altura, self.atributo)
        global tempo
        tempo = relogio.minutos

        numeroSala = False

        print('\033[4;31m '*21, end='')
        print('', '___________________________')
        print(' '*21, end='')
        print('|', ' '*25, '|')
        print(' '*21, end='')
        print('|', ' '*4, ' SALA VERMELHA ', ' '*4, '|')
        print(' '*21, end='')
        print('|___________________________|\033[m')
        print('\n'*2)

        tecla.play(-1)
        fraseAnimation = "Você acorda em uma sala com \033[4;31mparedes vermelhas!\033[m\n\n"
        self.animation(fraseAnimation)

        fraseAnimation = f"Você consegue ver uma porta e em cima da porta, um {cores['red']}relógio {cores['limpa']}marcando {relogio.minutos} minutos,\n"
        self.animation(fraseAnimation)
        fraseAnimation = "consegue ver uma escrivaninha, um toca disco, um armário, uma guitarra e uma mesa de bilhar...\n\n"
        self.animation(fraseAnimation)
        tecla.stop()
        sleep(1)
        global gameover
        gameover = False
        escrivaninhanaparede = False
        ima = False
        while True:
            if relogio.minutos <= 0:
                gameover = True
                break

            if numeroSala == True:

                tecla.play()
                print('\033[4;31m '*21, end='')
                print('', '___________________________')
                print(' '*21, end='')
                print('|', ' '*25, '|')
                print(' '*21, end='')
                print('|', ' '*4, ' SALA VERMELHA ', ' '*4, '|')
                print(' '*21, end='')
                print('|___________________________|\033[m')
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
                tecla.play(-1)
                relogio.corretempo(4)
                fraseAnimation = "A porta está trancada...\n\n"
                self.animation(fraseAnimation)

                if self.chave == False:

                    fraseAnimation = "Você não tem a chave! Vasculhe a sala para encontra-la\n\n"
                    self.animation(fraseAnimation)
                    tecla.stop()
                    print()
                else:
                    tecla.stop()
                    deseja = input("Você deseja usar a chave[sim/não]? ")

                    if deseja == "sim":
                        tecla.play(-1)
                        fraseAnimation = "Parabéns!! Você abriu a porta e avançou para a próxima sala!\n\n"
                        self.animation(fraseAnimation)
                        tecla.stop()

                        tempo = relogio.minutos

                        input("Aperte enter para prosseguir...")
                        break
                    elif deseja == "nao":
                        tecla.play(-1)
                        fraseAnimation = "Você achou melhor guardar a chave.\n\n"
                        self.animation(fraseAnimation)
                        tecla.stop()

                sleep(2)
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
                        tecla.play(-1)
                        fraseAnimation = "Você não encontrou nada, {}só tem lixo!{}\n\n".format(
                            cores['red'], cores['limpa'])
                        self.animation(fraseAnimation)
                        tecla.stop()
                        sleep(2)
                        os.system('clear')
                    elif opcEscrivaninha == 2:
                        relogio.corretempo(4)
                        print()
                        tecla.play(-1)
                        fraseAnimation = "É uma escrivaninha bonita e resistente!\n\n"
                        self.animation(fraseAnimation)
                        tecla.stop()
                        sleep(2)
                        os.system('clear')
                    elif opcEscrivaninha == 3:
                        relogio.corretempo(4)

                        if self.atributo == 'Força':
                            print()
                            tecla.play(-1)
                            fraseAnimation = "Você empurrou a escrivaninha até a parede.\n\n"
                            self.animation(fraseAnimation)
                            tecla.stop()
                            sleep(2)
                            escrivaninhanaparede = True
                            os.system('clear')
                        else:
                            print()
                            tecla.play(-1)
                            fraseAnimation = "Você não tem força para empurrar a escrivaninha!\n\n"
                            self.animation(fraseAnimation)
                            tecla.stop()
                            print()
                            sleep(2)
                            os.system('clear')
                    elif opcEscrivaninha == 4:

                        if escrivaninhanaparede == True:
                            print()
                            tecla.play(-1)
                            fraseAnimation = 'Você pode ver uma pequena {}saída{} de ventilação próxima ao teto.\n\n'.format(
                                cores['red'], cores['limpa'])
                            self.animation(fraseAnimation)
                            tecla.stop()
                            sleep(2)
                            relogio.corretempo(4)

                            if self.altura >= 1.8:
                                print('Você alcança a saída, deseja subir?')
                                janelinha = int(input('1-S / 0-N >>> '))
                                if janelinha == 0:
                                    os.system('clear')
                                    break
                                elif janelinha == 1:
                                    tecla.play(-1)
                                    fraseAnimation = 'Você pode se pendurar na janela, mas não tem {}força{} para passar para o outro lado, na parede do lado oposto está escrita a seguinte mensagem:\n\n'.format(
                                        cores['amarelo'], cores['limpa'])
                                    self.animation(fraseAnimation)
                                    fraseAnimation = '{}O conhecimento liberta!{}\n\n'.format(
                                        cores['amarelo'], cores['limpa'])
                                    self.animation(fraseAnimation)
                                    tecla.stop()
                                    sleep(2)
                                    os.system('clear')

                        else:
                            print()
                            tecla.play(-1)
                            fraseAnimation = 'O chão parece mais distante\n\n'
                            self.animation(fraseAnimation)
                            tecla.stop()
                            sleep(2)
                            relogio.corretempo(4)
                            os.system('clear')

                elif escolha == 2:
                    print('Você deseja:\n\n',
                          '[1] - Vasculhar toca disco\n',
                          '[2] - Olhar toca disco\n',
                          '[3] - Tocar o disco\n\n')

                    escolhaTocaDisco = int(input('>> '))

                    if escolhaTocaDisco == 1:
                        print()
                        relogio.corretempo(4)
                        tecla.play(-1)
                        fraseAnimation = 'Você descobriu o modelo do {}toca{} disco: Toca disco vinil air LP ion IT55\n\n'.format(
                            cores['azul'], cores['limpa'])
                        self.animation(fraseAnimation)
                        tecla.stop()
                        sleep(2)
                        os.system('clear')
                    elif escolhaTocaDisco == 2:
                        print()
                        tecla.play(-1)
                        fraseAnimation = 'Econtrou um vinil,esta em ótimo estado, sera que o toca disco funciona?\n\n '
                        self.animation(fraseAnimation)
                        tecla.stop()
                        sleep(2)
                        relogio.corretempo(4)
                        os.system('clear')
                    elif escolhaTocaDisco == 3:
                        relogio.corretempo(4)
                        if self.atributo == 'Inteligência':
                            tecla.play(-1)
                            fraseAnimation = '**While my {}guitar{} gently weeps tem um lindo {}solo{}!\n\n'.format(
                                cores['azul'], cores['limpa'], cores['amarelo', cores['limpa']])
                            self.animation(fraseAnimation)
                            tecla.stop()
                            sleep(2)

                        else:
                            print()
                            tecla.play(-1)
                            fraseAnimation = 'O toca disco não funciona!\n\n'
                            self.animation(fraseAnimation)
                            tecla.stop()
                            sleep(2)

                        os.system('clear')
                elif escolha == 3:
                    if ima == True:
                        print('Você deseja:\n\n',
                              '[1] - Abrir o armário\n',
                              '[2] - Olhar o armário\n',
                              '[3] - Empurrar o armário\n',
                              '[4] - Pegar a chave embaixo do armário\n\n')

                        escolhaArm = int(input('>> '))
                    else:
                        print('Você deseja:\n\n',
                              '[1] - Abrir o armário\n',
                              '[2] - Olhar o armário\n',
                              '[3] - Empurrar o armário\n\n')

                        escolhaArm = int(input('>> '))

                    if escolhaArm == 1:
                        print()
                        tecla.play(-1)
                        fraseAnimation = 'Dentro do armário vc encontra um bilhete escrito: "Pare de perder {}tempo!{}\n\n'.format(
                            cores['red'], cores['limpa'])
                        self.animation(fraseAnimation)
                        tecla.stop()
                        sleep(2)
                        relogio.corretempo(4)
                        os.system('clear')
                    elif escolhaArm == 2:
                        print()
                        tecla.play(-1)
                        fraseAnimation = 'Você está {}tentando{} aprender marcenaria?\n\n'.format(
                            cores['red'], cores['limpa'])
                        self.animation(fraseAnimation)
                        tecla.stop()
                        sleep(2)
                        relogio.corretempo(4)
                        os.system('clear')
                    elif escolhaArm == 3:
                        if self.atributo == 'Força':
                            print()
                            tecla.play(-1)
                            fraseAnimation = "Você derrubou o Armário.\n"
                            self.animation(fraseAnimation)
                            fraseAnimation = 'E encontrou uma dica: {}HOJE É DIA DE ROCK BEBÊ!!!{}\n\n'.format(
                                cores['azul'], cores['limpa'])
                            self.animation(fraseAnimation)
                            tecla.stop()
                            sleep(2)
                            relogio.corretempo(4)
                            os.system('clear')

                        else:
                            print()
                            if ima == True:
                                tecla.play(-1)
                                fraseAnimation = "Você conseguiu pegar a {}chave{} com o {}imã!{}\n\n".format(
                                    cores['red'], cores['limpa'], cores['azul'], cores['limpa'])
                                self.animation(fraseAnimation)
                                tecla.stop()
                                self.chave = True
                            else:
                                tecla.play(-1)
                                fraseAnimation = "Você não tem {}força{} para empurrar o Armário! Mas consegue olhar embaixo dele.\n\n".format(
                                    cores['amarelo'], cores['limpa'])
                                self.animation(fraseAnimation)
                                tecla.stop()
                            sleep(2)
                            relogio.corretempo(4)
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
                        tecla.play(-1)
                        fraseAnimation = 'Por que isso é importante?\n\n'
                        self.animation(fraseAnimation)
                        tecla.stop()
                        sleep(2)
                        relogio.corretempo(4)
                        os.system('clear')
                    elif escolhaGuitarra == 2:
                        print()
                        relogio.corretempo(8)
                        tecla.play(-1)
                        fraseAnimation = 'Você quebrou a guitarra e a {}chave{} caiu embaixo do armário, procure algo para pegá-la, voce perdeu {}8 minutos{}\n\n'.format(
                            cores['red'], cores['limpa'], cores['red'], cores['limpa'])
                        self.animation(fraseAnimation)
                        tecla.stop()
                        guitarQuebrada = True
                        sleep(2)
                        os.system('clear')
                    elif escolhaGuitarra == 3:
                        print()
                        relogio.corretempo(4)
                        if guitarQuebrada == True:
                            tecla.play(-1)
                            fraseAnimation = "Você tentou tocar uma guitarra quebrada, e perdeu {}10 minutos{}\n\n".format(
                                cores['red'], cores['limpa'])
                            self.animation(fraseAnimation)
                            tecla.stop()
                            sleep(2)
                        else:
                            pygame.mixer.music.load('guitar.ogg')
                            pygame.mixer.music.play()
                            tecla.play(-1)
                            fraseAnimation = 'Que música linda! Os deuses do rock estão satisfeitos...\n\n'
                            self.animation(fraseAnimation)
                            tecla.stop()
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
                            sleep(.5)
                            print('.')
                            tecla.play(-1)
                            fraseAnimation = 'Uma \033[4;31mchave\033[m caiu em sua cabeça!\n\n'
                            self.animation(fraseAnimation)
                            tecla.stop()
                            pygame.event.wait()
                            pygame.mixer.music.load('trilhasuspensa.ogg')
                            pygame.mixer.music.set_volume(0.3)
                            pygame.mixer.music.play(-1)
                            sleep(2)
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
                        tecla.play(-1)
                        fraseAnimation = 'Você decidiu jogar bilhar e perdeu {}5 minutos{}\n\n'.format(
                            cores['red'], cores['limpa'])
                        self.animation(fraseAnimation)
                        tecla.stop()
                        relogio.corretempo(5)
                        sleep(2)
                    elif opcMesa == 2:
                        tecla.play(-1)
                        fraseAnimation = "Você encontrou um {}imã{}, agora consegue atrair metal\n\n".format(
                            cores['azul'], cores['limpa'])
                        self.animation(fraseAnimation)
                        tecla.stop()
                        relogio.corretempo(4)
                        sleep(2)
                        ima = True
                    os.system('clear')

            elif opcao2 == 3:
                if self.atributo == 'Força':
                    print()
                    tecla.play(-1)
                    fraseAnimation = "A porta é de madeira e você conseguiu quebra-la! Mas uma farpa de madeira te {}machucou.{}\n\n".format(
                        cores['red'], cores['limpa'])
                    self.animation(fraseAnimation)
                    fraseAnimation = "Parabéns, você é {}forte{} o suficiente para a próxima sala! Mas perderá mais tempo por estar machucado!\n\n".format(
                        cores['amarelo'], cores['limpa'])
                    self.animation(fraseAnimation)
                    tecla.stop()
                    tempo = relogio.minutos
                    input('Aperte enter para continuar...')
                    os.system('clear')
                    break
                else:
                    tecla.play(-1)
                    fraseAnimation = 'Você é frac{} demais pra isso\n\n'.format(
                        self.generos())
                    self.animation(fraseAnimation)
                    tecla.stop()
                    sleep(2)
                    relogio.corretempo(4)
                    os.system('clear')

    def gameover(self):
        if gameover == True:
            return True
        else:
            return False

    def retornaTempo(self):
        total = tempo + 30
        return total
