from Imagem import Imagem
from personagem import Personagem
from relogio import Relógio
from funcoes import Funções
from time import sleep
from primeiraSala import salaVermelha
from CORES import cores
import os
import pygame
from random import randint


class salaBranca(Funções, Personagem):

    def __init__(self, *args, genero, **kwargs):
        self.cadeira = False
        self.espelho = False
        self.quadro = False
        self.bau = False
        self.estatua = True
        self.bolsaRemedios = False
        self.chaveBau = False
        self.chavePorta = False

        super().__init__(*args, genero=genero, **kwargs)

    def acao(self):
        sala1 = salaVermelha(nome=self.nome, altura=self.altura,
                             atributo=self.atributo, genero=self.genero)
        tempo = sala1.retornaTempo()
        relogio = Relógio(tempo, self.nome, self.altura, self.atributo)
        tecla = self.teclando()
        numeroSala = False

        print(' '*21, end='')
        print('', '___________________________')
        print(' '*21, end='')
        print('|', ' '*25, '|')
        print(' '*21, end='')
        print('|', ' '*5, ' SALA BRANCA ', ' '*5, '|')
        print(' '*21, end='')
        print('|___________________________|')
        print('\n'*2)

        tecla.play(-1)
        sala = "Você está em uma sala com paredes brancas!\n\n"
        self.animation(sala)

        fraseAnimation = f"Lembre-se que acima da porta há um {cores['red']}relógio {cores['limpa']},marcando agora {relogio.minutos} minutos,\n"
        self.animation(fraseAnimation)
        fraseAnimation = "Você consegue ver uma cadeira, um espelho, um quadro, um bau, uma estátua e uma bolsa de remédios...\n\n"
        self.animation(fraseAnimation)
        tecla.stop()
        sleep(1)

        pygame.init()
        tecla = pygame.mixer.Sound('teclado.ogg')
        global gameover
        gameover = False
        machucado = False
        lembranca = False
        foto = False
        while True:
            if relogio.minutos <= 0:
                gameover = True
                break
            if numeroSala == True:

                tecla.play()
                print(' '*21, end='')
                print('', '___________________________')
                print(' '*21, end='')
                print('|', ' '*25, '|')
                print(' '*21, end='')
                print('|', ' '*5, ' SALA BRANCA ', ' '*5, '|')
                print(' '*21, end='')
                print('|___________________________|')
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

            escolha = int(input("»» "))
            print()

            if escolha == 1:

                relogio.corretempo(4)
                fraseAnimation = "A porta está trancada...\n\n"
                self.animation(fraseAnimation)

                if self.chavePorta == False:
                    fraseAnimation = "Você não tem a chave! Vasculhe a sala para encontra-la\n\n"
                    self.animation(fraseAnimation)
                    print()
                else:
                    escolha = input("Você deseja usar a chave[sim/não]? ")

                    if escolha == "sim":
                        fraseAnimation = "Parabéns!! Jogo zerado!!\n\n"
                        self.animation(fraseAnimation)
                        sleep(2)
                        break
                    elif escolha == "nao":
                        print("Você achou melhor guardar a chave.")

                sleep(2)
                os.system('clear')

            elif escolha == 2:

                sleep(1)
                print("Qual item deseja vasculhar?\n\n",
                      "[1] - Cadeira\n",
                      "[2] - Espelho\n",
                      "[3] - Quadro\n",
                      "[4] - Bau\n",
                      "[5] - Estátua\n",
                      "[6] - Bolsa de remédios")

                sleep(1)
                print()
                objetos = int(input('>> '))
                print()

                if objetos == 1:

                    print("Você deseja: \n\n",
                          "[1] - Vasculhar cadeira\n",
                          "[2] - Quebrar a cadeira\n",
                          "[3] - Sentar na cadeira\n",)

                    opcaoCadeira = int(input(">> "))

                    if opcaoCadeira == 1:
                        relogio.corretempo(2)
                        print()

                        print(
                            "Você encontrou uma carta grudada na cadeira, deseja ler? [sim/não]\n")
                        ler = input('>> ').upper()

                        if ler == 'SIM':
                            carta = '''\033[32m
        ────────────────────────────────────────
        ─────────────▄▄██████████▄▄─────────────
        ─────────────▀▀▀───██───▀▀▀─────────────
        ─────▄██▄───▄▄████████████▄▄───▄██▄─────
        ───▄███▀──▄████▀▀▀────▀▀▀████▄──▀███▄───
        ──████▄─▄███▀──────────────▀███▄─▄████──
        ─███▀█████▀▄████▄──────▄████▄▀█████▀███─
        ─██▀──███▀─██████──────██████─▀███──▀██─
        ──▀──▄██▀──▀████▀──▄▄──▀████▀──▀██▄──▀──
        ─────███───────────▀▀───────────███─────
        ─────██████████████████████████████─────
        ─▄█──▀██──███───██────██───███──██▀──█▄─
        ─███──███─███───██────██───███▄███──███─
        ─▀██▄████████───██────██───████████▄██▀─
        ──▀███▀─▀████───██────██───████▀─▀███▀──
        ───▀███▄──▀███████────███████▀──▄███▀───
        ─────▀███────▀▀██████████▀▀▀───███▀─────
        ───────▀─────▄▄▄───██───▄▄▄──────▀──────
        ──────────── ▀▀███████████▀▀ ────────────
        ────────────────────────────────────────\033[m\n\n'''
                            print(carta)
                            fraseAnimation = '\nQual o significado desse simbolo?'
                            self.animation(fraseAnimation)
                            fraseAnimation = 'Começamos bem, porém ainda não encontramos uma forma de sair daqui, vamos continuar'
                            self.animation(fraseAnimation)
                            sleep(2)
                            os.system('clear')
                            relogio.corretempo(2)
                        else:
                            fraseAnimation = 'Ok, vamos continuar'
                            self.animation(fraseAnimation)
                            sleep(2)
                            os.system('clear')
                            relogio.corretempo(2)

                    elif opcaoCadeira == 2:

                        relogio.corretempo(2)
                        fraseAnimation = '''Você quebrou a cadeira na parede, mas um pedaço de farpa machucou seu braço
Você percebeu que nos pedaços de madeira quebrados tem uma carta, deseja ler?\n\n'''
                        self.animation(fraseAnimation)
                        ler = input('>> ').upper()
                        sleep(2)

                        if ler == 'SIM':

                            fraseAnimation = '''Você está um pouco zonzo, e esta perdendo tempo lendo essa carta, vá enfaixar seu braço
Caso contrário perderá mais {}tempo{} que o normal\n\n'''.format(cores['red'], cores['limpa'])
                            self.animation(fraseAnimation)
                            machucado = True

                            sleep(2)
                            os.system('clear')
                            relogio.corretempo(2)
                        else:
                            print('OK!')
                            sleep(2)
                            relogio.corretempo(2)
                            os.system('clear')
                    elif opcaoCadeira == 3:
                        relogio.corretempo(2)

                        print('Que situação maluca, descansar é sempre bom!\n',
                              'Você conseguiu enxergar o reflexo de alguma coisa\n')

                        sleep(2)

                        print("Para onde está olhando?\n\n",
                              "[1] - Cadeira\n",
                              "[2] - Espelho\n",
                              "[3] - Quadro\n",
                              "[4] - Bau\n",
                              "[5] - Estátua\n",
                              "[6] - Bolsa de remédios\n")

                        opcaoEspelho = int(input('>> '))

                        if opcaoEspelho == 2:
                            print('Você olha para o espelho e vê:\n')

                            visualizar = randint(1, 3)

                            if visualizar != 3:
                                print('Um Dinossauro')
                                sleep(1)
                                fraseAnimation = 'Você está muito cansado, é impossível isso estar na sala, descanse 5 minutos!\n\n'
                                self.animation(fraseAnimation)

                                relogio.corretempo(5)
                                sleep(2)
                                os.system('clear')
                            elif visualizar == 2:
                                fraseAnimation = 'Um guarda-roupa?\n\n'
                                self.animation(fraseAnimation)
                                relogio.corretempo(4)
                                sleep(2)
                                os.system('clear')

                            else:
                                print('A sala realmente tem uma estatua, o que quer fazer?\n',
                                      '[1] - Olhar a estatua\n',
                                      '[2] - Girar a estatua\n',
                                      '[3] - Não fazer nada\n')

                                estatua = int(input('>>> '))
                                sleep(2)

                                if estatua == 1:
                                    fraseAnimation = 'Nada de diferente aconteceu, talvez fosse apenas uma impressão sua...\n\n'
                                    self.animation(fraseAnimation)

                                    relogio.corretempo(1)
                                    sleep(2)
                                    os.system('clear')

                                elif estatua == 2:  # =================\\ 1° FINAL //============================
                                    fraseAnimation = '''Boa escolha, você girou a estatua com delicadeza
Um buraco se abre no peito da estátua
lhe dando acesso a {}chave{} que abre a porta de saída ...\n\n'''.format(cores['ciano'], cores['limpa'])
                                    self.animation(fraseAnimation)
                                    relogio.corretempo(4)
                                    self.chavePorta = True
                                    sleep(2)
                                    os.system('clear')

                                elif estatua == 3:
                                    relogio.corretempo(4)
                                    continue
                        else:
                            print('OK!')
                            relogio.corretempo(4)
                            sleep(2)
                            os.system('clear')
                elif objetos == 2 and lembranca == True:

                    print('O que você vê no espelho?\n',
                          '[1] - Estátua\n',
                          '[2] - Baú\n',
                          '[3] - Seu reflexo')

                    acaoEspelho = int(input(">> "))

                    if acaoEspelho == 3:

                        fraseAnimation = '''Ao se olhar você começa a se lembrar do que realmente aconteceu!
Você estava em uma estrada com sua família e um caminhão entrou na pista
Aparentemente o caminhoneiro estava embriagado e causou um acidente
Você e sua familia vivenciaram um trauma muito grande, e nesse momento
Você está em uma cama de hospital...\n\n'''
                        self.animation(fraseAnimation)
                        sleep(2)
                        relogio.corretempo(3)
                        os.system('clear')
                    else:
                        print('OK!')
                        sleep(2)
                        os.system('clear')

                elif objetos == 2:

                    print('O que você viu no espelho?\n',
                          '[1] - Seu próprio reflexo\n',
                          '[2] - Quadro \n',
                          '[3] - Violão')

                    visualizar = int(input('>> '))
                    sleep(2)

                    if visualizar == 1:

                        fraseAnimation = '''Você é uma pessoa muito bonita, porém
já tem problemas o suficiente para ficar se olhando no espelho\n\n'''
                        self.animation(fraseAnimation)
                        relogio.corretempo(5)
                        sleep(2)
                        os.system('clear')

                    elif visualizar == 2:

                        quadro = input(
                            'Deseja chegar mais perto? [sim/não]').upper()
                        print()
                        sleep(1)

                        if quadro == 'SIM':
                            fraseAnimation = 'O quadro da sala é uma figura estranha, quem será?\n\n'
                            self.animation(fraseAnimation)
                            relogio.corretempo(5)

                            quadr = '''{}
            ─────▄██▀▀▀▀▀▀▀▀▀▀▀▀▀██▄─────
            ────███───────────────███────
            ───███─────────────────███───
            ──███───▄▀▀▄─────▄▀▀▄───███──
            ─████─▄▀────▀▄─▄▀────▀▄─████─
            ─████──▄████─────████▄──█████
            █████─██▓▓▓██───██▓▓▓██─█████
            █████─██▓█▓██───██▓█▓██─█████
            █████─██▓▓▓█▀─▄─▀█▓▓▓██─█████
            ████▀──▀▀▀▀▀─▄█▄─▀▀▀▀▀──▀████
            ███─▄▀▀▀▄────███────▄▀▀▀▄─███
            ███──▄▀▄─█──█████──█─▄▀▄──███
            ███─█──█─█──█████──█─█──█─███
            ███─█─▀──█─▄█████▄─█──▀─█─███
            ███▄─▀▀▀▀──█─▀█▀─█──▀▀▀▀─▄███
            ████─────────────────────████
            ─███───▀█████████████▀───████
            ─███───────█─────█───────████
            ─████─────█───────█─────█████
            ───███▄──█────█────█──▄█████─
            ─────▀█████▄▄███▄▄█████▀─────
            ──────────█▄─────▄█──────────
            ──────────▄█─────█▄──────────
            ───────▄████─────████▄───────
            ─────▄███████───███████▄─────
            ───▄█████████████████████▄───
            ─▄███▀───███████████───▀███▄─
            ███▀─────███████████─────▀███
            ▌▌▌▌▒▒───███████████───▒▒▐▐▐▐
            ─────▒▒──███████████──▒▒─────
            ──────▒▒─███████████─▒▒──────
            ───────▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒───────
            ─────────████░░█████─────────
            ────────█████░░██████────────
            ──────███████░░███████───────
            ─────█████──█░░█──█████──────
            ─────█████──████──█████──────
            ──────████──████──████───────
            ──────████──████──████───────
            ──────████───██───████───────
            ──────████───██───████───────
            ──────████──████──████───────
            ─██────██───████───██─────██─
            ─██───████──████──████────██─
            ─███████████████████████████─
            ─██─────────████──────────██─
            ─██─────────████──────────██─
            ────────────████─────────────
            ─────────────██──────────────{}'''.format(cores['ciano'],cores['limpa'])
                            print(quadr)
                            print()
                            if self.atributo=='Sorte':
                                  print('[1] - Vasculhar o quadro\n',
                                      '[2] - Admirar o quadro\n',
                                      '[3] -{}Rasgar o quadro{}'.format(cores['red'],cores['limpa']))

                            else:
                                print('[1] - Vasculhar o quadro\n',
                                      '[2] - Admirar o quadro\n',
                                      '[3] - Rasgar o quadro')

                            acaoQuadro = int(input('>> '))

                            if acaoQuadro == 1:

                                fraseAnimation = 'Você não encontrou nada...'
                                self.animation(fraseAnimation)
                                sleep(2)
                                relogio.corretempo(2)
                                os.system('clear')

                            elif acaoQuadro == 2:

                                fraseAnimation = '''Essa realmente é uma obra muito bonita, entendo você querer adimirá-la
Porem seu {}tempo{} está {}correndo{}'''.format(cores['mage'],cores['limpa'],cores['amarelo'],cores['limpa'])
                                self.animation(fraseAnimation)
                                sleep(2)
                                relogio.corretempo(5)
                                os.system('clear')

                            elif acaoQuadro == 3:

                                fraseAnimation = '''Que loucura rasgar um quadro tão lindo quanto esse...
Porem situações desesperadas pedem medidas desesperadas
Você encontrou dentro do quadro uma {}chave pequena{}...\n\n'''.format(cores['Mage'], cores['limpa'])
                                self.animation(fraseAnimation)
                                self.chaveBau = True

                                sleep(2)
                                os.system('clear')
                        else:
                            print('OK!')
                            relogio.corretempo(2)
                            sleep(2)
                            os.system('clear')
                elif objetos == 3:

                    print("Você deseja: \n\n",
                          "[1] - Vasculhar o quadro\n",
                          "[2] - Quebrar o quadro\n",
                          "[3] - Admirar o quadro\n",)

                    acaoQuadro = int(input('>> '))

                    if acaoQuadro == 1:
                        relogio.corretempo(4)
                        fraseAnimation = '''O quadro da sala é uma referência a JigSaw!
Ao vasculhar o quadro você encontrou uma bilhete de viagem
O que um bilhete de viagem faria atrás de um quadro?\n\n'''  # Conceito para a próxima versão
                        self.animation(fraseAnimation)

                        bilhete = True
                        print('Você deseja: \n\n',
                              '[1] - Ler o bilhete\n',
                              '[2] - Guardar o bilhete\n',
                              '[3] - Rasgar o bilhete?\n')
                              
                        acaoBilhete = int(input(">> "))

                        if acaoBilhete == 1 and bilhete == True:

                            fraseAnimation = '''Bilhete de onibus:
Valor da passagem: R$5,50
Destino: Praia do sono
O que um bilhete de viagem faria aqui?\n\n'''  # Melhorar pergunta com o atributo inteligencia
                            self.animation(fraseAnimation)
                            relogio.corretempo(2)
                            sleep(2)
                            os.system('clear')

                        elif acaoBilhete == 2 and bilhete == True:

                            fraseAnimation = 'Ele pode vir a ser útil em outro momento...\n\n'
                            self.animation(fraseAnimation)
                            sleep(2)
                            relogio.corretempo(2)
                            os.system('clear')

                        elif acaoBilhete == 3 and bilhete == True:

                            fraseAnimation = '''Você nem se interessou em saber o que estava escrito
provavelmente não tem intenção nenhuma de sair daqui\n'''
                            self.animation(fraseAnimation)
                            sleep(2)
                            relogio.corretempo(5)
                            bilhete = False
                            os.system('clear')

                    elif acaoQuadro == 2:

                        fraseAnimation = '''Você quebrou um belo quadro, sem nem mesmo observar!
Você começa a se sentir cansado e sem forças
Continuar agora sem descansar pode lhe trazer {}consequências{}
Deseja tomar um descanso?[sim/não]\n\n'''.format(cores['Mage'], cores['limpa'])
                        self.animation(fraseAnimation)

                        descanso = input(">> ").upper()

                        if descanso == 'SIM':
                            fraseAnimation = 'Descanse um pouco...'
                            self.animation(fraseAnimation)
                            relogio.corretempo(2)
                            sleep(2)
                            os.system('clear')

                        else:
                            fraseAnimation = 'A vida é feita de {}escolhas{}...\n\n'.format(
                                cores['red'], cores['limpa'])
                            self.animation(fraseAnimation)
                            relogio.corretempo(10)
                            sleep(2)
                            os.system('clear')

                    elif acaoQuadro == 3:
                        quadr = '''{}
            ─────▄██▀▀▀▀▀▀▀▀▀▀▀▀▀██▄─────
            ────███───────────────███────
            ───███─────────────────███───
            ──███───▄▀▀▄─────▄▀▀▄───███──
            ─████─▄▀────▀▄─▄▀────▀▄─████─
            ─████──▄████─────████▄──█████
            █████─██▓▓▓██───██▓▓▓██─█████
            █████─██▓█▓██───██▓█▓██─█████
            █████─██▓▓▓█▀─▄─▀█▓▓▓██─█████
            ████▀──▀▀▀▀▀─▄█▄─▀▀▀▀▀──▀████
            ███─▄▀▀▀▄────███────▄▀▀▀▄─███
            ███──▄▀▄─█──█████──█─▄▀▄──███
            ███─█──█─█──█████──█─█──█─███
            ███─█─▀──█─▄█████▄─█──▀─█─███
            ███▄─▀▀▀▀──█─▀█▀─█──▀▀▀▀─▄███
            ████─────────────────────████
            ─███───▀█████████████▀───████
            ─███───────█─────█───────████
            ─████─────█───────█─────█████
            ───███▄──█────█────█──▄█████─
            ─────▀█████▄▄███▄▄█████▀─────
            ──────────█▄─────▄█──────────
            ──────────▄█─────█▄──────────
            ───────▄████─────████▄───────
            ─────▄███████───███████▄─────
            ───▄█████████████████████▄───
            ─▄███▀───███████████───▀███▄─
            ███▀─────███████████─────▀███
            ▌▌▌▌▒▒───███████████───▒▒▐▐▐▐
            ─────▒▒──███████████──▒▒─────
            ──────▒▒─███████████─▒▒──────
            ───────▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒───────
            ─────────████░░█████─────────
            ────────█████░░██████────────
            ──────███████░░███████───────
            ─────█████──█░░█──█████──────
            ─────█████──████──█████──────
            ──────████──████──████───────
            ──────████──████──████───────
            ──────████───██───████───────
            ──────████───██───████───────
            ──────████──████──████───────
            ─██────██───████───██─────██─
            ─██───████──████──████────██─
            ─███████████████████████████─
            ─██─────────████──────────██─
            ─██─────────████──────────██─
            ────────────████─────────────
            ─────────────██──────────────{}\n\n'''.format(cores['verde'],cores['limpa'])
                        print(quadr)
                        print('Uma pequena entrada se abre na lateral do quadro...\n',
                              'Deseja entrar? [sim/não]\n')

                        entrar = input(">> ").upper()
                        relogio.corretempo(2)
                        os.system('clear')
                        if entrar == 'SIM':

                            fraseAnimation = "Você agora se encontra em uma casa...\n\n"
                            self.animation(fraseAnimation)
                            sleep(2)
                            print(' '*20, end='')
                            print('', '__________________________')
                            print(' '*20, end='')
                            print('|', ' '*24, '|')
                            print(' '*20, end='')
                            print('|', ' '*8, ' CASA ', ' '*8, '|')
                            print(' '*20, end='')
                            print('|__________________________|')
                            print('\n'*2)

                            print()

                            fraseAnimation = '''Seus pais te chamam para uma volta de carro
aparentemente estão indo visitar alguém.
Você entra no carro e todos partem para viagem
porém já na estrada você nota que esqueceu o celular\n\n'''
                            self.animation(fraseAnimation)
                            sleep(2)

                            lembranca = True
                            relogio.corretempo(3)
                            os.system('clear')

                        else:
                            continue

                elif objetos == 4 and self.chaveBau == True:
                    relogio.corretempo(4)
                    fraseAnimation = '''Abrir o baú com a {}chave{} foi uma ótima escolha, nele se encontra uma foto
Nela se encontra Rodin, ao lado de uma de suas obras mais famosas
Porque alguém guardaria essa foto em um baú?\n\n'''.format(cores['Mage'], cores['limpa'])
                    self.animation(fraseAnimation)
                    foto = True

                elif objetos == 4:

                    print("Você deseja: \n\n",
                          "[1] - Abrir o baú\n",
                          "[2] - Vasculhar o baú\n",
                          "[3] - Não fazer nada\n",)

                    acaoBau = int(input('>> '))
                    self.chaveBau = False

                    if acaoBau == 1 and self.chaveBau == False:
                        relogio.corretempo(2)
                        fraseAnimation = 'Você necessita de uma chave para abri-lo'
                        self.animation(fraseAnimation)
                        sleep(2)
                        os.system('clear')

                    elif acaoBau == 2:
                        fraseAnimation = 'Você não encontrou nada ao verificar o baú...'
                        self.animation(fraseAnimation)
                        sleep(2)
                        os.system('clear')
                    elif acaoBau == 2 and self.atributo== 'Sorte':
                        relogio.corretempo(2)
                        fraseAnimation = 'Você não encontrou nada ao verificar o baú...'
                        self.animation(fraseAnimation)
                        sleep(2)
                        os.system('clear')
                    elif acaoBau == 3:
                        os.system('clear')
                        continue

                elif objetos == 5 and foto == True:
                    relogio.corretempo(4)
                    print('Que bela estátua, é uma réplica da obra "O Pensador de Agusto Rodin"\n',
                          '[1] - Olhar a estatua\n',
                          '[2] - Girar a estatua\n',
                          '[3] - Não fazer nada')

                    acaoEstatua = int(input(">> "))

                    sleep(2)

                    if acaoEstatua == 2:  # ===============\\ 2° e 3° FINAL //===================

                        fraseAnimation = '''Boa escolha, você girou a estatua com delicadeza
Um buraco se abre no peito da estátua
lhe dando acesso a {}chave{} que abre a porta de saída ...\n\n'''.format(cores['red'], cores['limpa'])
                        relogio.corretempo(4)
                        self.chavePorta = True
                        sleep(2)
                        os.system('clear')
                    else:
                        fraseAnimation = 'Nada de diferente aconteceu, talvez fosse apenas uma {}impressão{} sua...\n\n'.format(
                            cores['ciano'], cores['limpa'])
                        self.animation(fraseAnimation)
                        relogio.corretempo(4)
                        sleep(2)
                        os.system('clear')

                elif objetos == 5:

                    print("Você deseja: \n\n",
                          "[1] - Admirar a estátua\n",
                          "[2] - Não fazer nada\n",)

                    acaoEstatua = int(input('>> '))

                    if acaoEstatua == 1:
                        relogio.corretempo(4)

                        fraseAnimation = '''Que bela estátua, é uma réplica da obra "O {}Pensador{} de Agusto Rodin.
é uma das mais famosas esculturas de bronze do escultor francês Auguste Rodin.
Retrata um homem em meditação soberba, lutando com uma poderosa força interna.
O Pensador originalmente procurava retratar Dante em frente dos Portões do Inferno
ponderando seu grande poema...\n\n'''.format(cores['amarelo'], cores['limpa'])
                        self.animation(fraseAnimation)
                        sleep(2)
                        os.system('clear')

                    else:
                        continue

                elif objetos == 6 and machucado == True:
                    deseja = input(
                        'Você deseja abrir a bolsa de remédios? ').lower()
                    if deseja == 'sim':
                        fraseAnimation = '''{}Boa escolha, dentro da bolsa de remédios temos analgésicos e gaze para o seu machucado{}
Pode continuar sem nenhum problema\n\n'''.format(cores['ciano'], cores['limpa'])
                        self.animation(fraseAnimation)
                        relogio.corretempo(2)
                        sleep(2)
                        os.system('clear')
                    else:
                        fraseAnimation = 'Você está machucado e mesmo assim não quis abrir a bolsa de remédios, isso terá consequências!'
                        self.animation(fraseAnimation)
                        relogio.corretempo(7)
                        sleep(2)
                        os.system('clear')

                elif objetos == 6 and lembranca == True:

                    print("Você deseja: \n\n",
                          "[1] - Abrir a bolsa\n",
                          "[2] - Jogar a bolsa no lixo\n",
                          "[3] - Não fazer nada\n",)

                    acaoBolsa = int(input('>> '))

                    if acaoBolsa == 1:
                        fraseAnimation = "Você abre a bolsa e encontra o que aparentemente é a {}chave de um baú{}\n\n".format(
                            cores['Mage'], cores['limpa'])
                        self.animation(fraseAnimation)
                        relogio.corretempo(3)

                        self.chaveBau = True

                        sleep(2)
                        os.system('clear')
                    elif acaoBolsa == 2:
                        print('*Jogando a bolsa no lixo..*')
                    else:
                        continue

                elif objetos == 6:

                    fraseAnimation = '''Uma bolsa de remédios pode ser útil em momentos de necessidade
'Fique atento caso precise de cuidados médicos\n'''
                    self.animation(fraseAnimation)

                    print("Você deseja: \n\n",
                          "[1] - Abrir a bolsa\n",
                          "[2] - Não fazer nada\n",)

                    acaoBolsa = int(input('>> '))

                    if acaoBolsa == 1:
                        relogio.corretempo(2)
                        fraseAnimation = '{}Na bolsa temos analgésicos e gaze para uma eventual necessidade{}\n\n'.format(
                            cores['azul'], cores['limpa'])
                        self.animation(fraseAnimation)
                    else:
                        continue
            elif escolha == 3:
                if self.atributo == 'Força':
                    fraseAnimation = "A porta é de ferro e você esta machucado, dessa vez não poderá contar com sua força!"
                    self.animation(fraseAnimation)
                    sleep(2)
                    os.system('clear')
                else:
                    fraseAnimation = "Você é frac{} demais para isso!".format(
                        self.generos())
                    self.animation(fraseAnimation)
                    sleep(2)
                    os.system('clear')
