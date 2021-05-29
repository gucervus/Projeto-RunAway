from personagem import Personagem
from relogio import Relógio
from funcoes import Funções
from time import sleep
from CORES import cores
import os
import pygame


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

        relogio = Relógio(30, self.nome, self.altura, self.atributo)

        numeroSala = False

        print(' '*20, end='')
        print('', '__________________________')
        print(' '*20, end='')
        print('|', ' '*24, '|')
        print(' '*20, end='')
        print('|', ' '*7, ' SALA BRANCA ', ' '*7, '|')
        print(' '*20, end='')
        print('|__________________________|')
        print('\n'*2)

        # tecla.play(-1)
        sala = "Você está em uma sala com paredes brancas!\n\n"
        # func.animation(sala)

        fraseSala1 = f"Lembre-se que acima da porta há um {cores['red']}relógio {cores['limpa']},marcando agora {relogio.minutos} minutos,\n"
        # func.animation(fraseSala1)
        fraseSala2 = "Você consegue ver uma cadeira, um espelho, um quadro, um bau, uma estátua e uma bolsa de...\n\n"
        # func.animation(fraseSala2)
        # tecla.stop()
        sleep(1)

        pygame.init()
        tecla = pygame.mixer.Sound('teclado.ogg')

        while True:
            if numeroSala == True:

                tecla.play()
                print(' '*20, end='')
                print('', '__________________________')
                print(' '*20, end='')
                print('|', ' '*24, '|')
                print(' '*20, end='')
                print('|', ' '*7, ' SALA BRANCA ', ' '*7, '|')
                print(' '*20, end='')
                print('|__________________________|')
                print('\n'*2)

                tecla.play(-1)
                contador = f"Restam {relogio.minutos} minutos para escapar da sala!\n\n"
                self.animation(contador)
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
                print("A porta está trancada...")

                if self.chavePorta == False:
                    print("Você não tem a chave! Vasculhe a sala para encontra-la")
                    print()
                else:
                    escolha = input("Você deseja usar a chave[sim/não]? ")

                    if escolha == "sim":
                        print(
                            "Parabéns!! Você abriu a porta e avançou para a próxima sala!")
                        relogio.minutos += 30
                        input("Aperte enter para prosseguir...")
                        break
                    elif escolha == "nao":
                        print("Você achou melhor guardar a chave.")

                sleep(5)
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
                          "[3] - Subir na cadeira\n",)

                    opcaoCadeira = int(input(">> "))

                    if opcaoCadeira == 1:
                        relogio.corretempo(4)
                        print()
                        ler = input(
                            "Você não encontrou uma carta grudada na cadeira, deseja ler? [sim/não]: ").upper()
                        sleep(5)
                        os.system('clear')

                        if ler == 'SIM':
                            print('***Mensagem sobre a vida***')
                            print(
                                'Começamos bem, porém ainda não encontramos uma forma de sair daqui, vamos continuar')
                        else:
                            print('Ok, vamos continuar')

                    elif opcaoCadeira == 2:
                        print(
                            "Você quebrou a cadeira na parede, mas um pedaço de farpa machucou seu braço")
                        print('Você perdeu x minutos')
                        sleep(5)
                        os.system('clear')
                        # Decrementa tempo

                        ler = input(
                            'Você percebeu que nos pedaços de madeira quebrados tem uma carta, deseja ler?').upper()
                        sleep(5)
                        os.system('clear')

                        if ler == 'SIM':
                            print("Você está um pouco sonzo, e esta perdendo tempo lendo essa carta, vá enfaixar seu braço\n",
                                  "Caso contrário perderá mais tempo que o normal\n")
                            sleep(5)
                            os.system('clear')
                            # Decrementa tempo

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

                            recuperaVida = int(input(">> "))

                            if recuperaVida == 6:
                                print("Boa escolha, dentro do estojo de remédios temos analgésicos e gaze para o seu machucado\n"
                                      "Pode continuar sem nenhum problema\n")
                                sleep(5)
                                os.system('clear')
                            else:
                                # Decrementa 5 minutos a cada 10 minutos passados
                                continue

                    elif opcaoCadeira == 3:
                        print('Que situação maluca, descansar é sempre bom!\n',
                              'Você conseguiu enxergar o reflexo de alguma coisa\n')

                        sleep(5)
                        os.system('clear')

                        print("Qual item deseja vasculhar?\n\n",
                              "[1] - Cadeira\n",
                              "[2] - Espelho\n",
                              "[3] - Quadro\n",
                              "[4] - Bau\n",
                              "[5] - Estátua\n",
                              "[6] - Bolsa de remédios")

                        opcaoEspelho = int(input('>> '))

                        if opcaoEspelho == 2:
                            print('O que você viu no espelho?\n',
                                  '[1] - Dinossauro\n',
                                  '[2] - guarda-roupa\n',
                                  '[3] - Estatua')

                            visualizar = int(input('>> '))

                            if visualizar != 3:
                                print(
                                    'Você está muito cansado, é impossível isso estar na sala, descanse {}5 minutos{}'.format(cores['red'], cores['limpa']))

                                relogio.corretempo(5)
                                sleep(5)
                                os.system('clear')

                            else:
                                print(
                                    'A sala realmente tem uma estatua, o que quer fazer?')
                                print('[1] - Olhar a estatua\n',
                                      '[2] - Girar a estatua\n',
                                      '[3] - Não fazer nada')
                                estatua = int(input('>>> '))
                                sleep(5)
                                os.system('clear')

                                if estatua == 1:
                                    print(
                                        'Nada de diferente aconteceu, talvez fosse apenas uma impressão sua...')

                                    relogio.corretempo(1)
                                    sleep(5)
                                    os.system('clear')
                                elif estatua == 2:  # =================\\ 1° FINAL //============================
                                    print('Boa escolha, você girou a estatua com delicadeza\n',
                                          'Um buraco se abre no peito da estátua\n',
                                          'lhe dando acesso a chave que abre a porta de saída ...')

                                    self.chavePorta = True  # Como usar a chave da porta?
                                    sleep(5)
                                    os.system('clear')
                                elif estatua == 3:
                                    continue
                elif objetos == 2:
                    print('O que você viu no espelho?\n',
                          '[1] - Seu próprio reflexo\n',
                          '[2] - Qudaro \n',
                          '[3] - Violão')

                    visualizar = int(input('>> '))
                    sleep(5)
                    os.system('clear')

                    if visualizar == 1:

                        print('Você é uma pessoa muito bonita, porém\n',
                              'já tem problemas o suficiente para ficar se olhando no espelho')
                        relogio.corretempo(5)

                    elif visualizar == 2:
                        print(
                            'É um quadro lindo, deseja chegar mais perto? [sim/não]')
                        quadro = input(' ').upper()

                        sleep(5)
                        os.system('clear')

                        if quadro == 'SIM':
                            print('O quadro da sala é a Dama com Arminho de Leonardo da Vinci\n',
                                  'Que linda peça!')

                            print()
                            print('[1] - Vasculhar o quadro\n',
                                  '[2] - Admirar o quadro\n',
                                  '[3] - Rasgar o quadro')

                            acaoQuadro = int(input('>> '))

                            if acaoQuadro == 1:

                                print('Você não encontrou nada...')
                                relogio.corretempo(2)

                            elif acaoQuadro == 2:

                                print('Essa realmente é uma obra muito bonita, entendo você querer adimirá-la\n',
                                      f'Porem seu {cores['red']}tempo{cores['limpa']} está correndo')
                                relogio.corretempo(5)

                            elif acaoQuadro == 3:

                                print('Que loucura rasgar um quadro tão lindo quanto esse...\n',
                                      'Da Vince acaba de se revirar no tumulo\n',
                                      'Porem situações desesperadas pedem medidas desesperadas\n',
                                      'Você encontrou dentrou do quadro uma {}chave{}...'.format(cores['red'],cores['limpa']))
                                self.chaveBau = True

                                sleep(5)
                                os.system('clear')

                                print("Qual item deseja vasculhar?\n\n",
                                      "[1] - Cadeira\n",
                                      "[2] - Espelho\n",
                                      "[3] - Quadro\n",
                                      "[4] - Bau\n",
                                      "[5] - Estátua\n",
                                      "[6] - Bolsa de remédios")

                                opcaoChaveBau = int(input('>> '))
                                sleep(5)
                                os.system('clear')

                                if opcaoChaveBau == 4 and self.chaveBau == True:

                                    print('Abrir o baú com a chave foi uma ótima escolha, nele se encontra uma foto\n',
                                          'Nela se encontra Rodin, ao lado de uma de suas obras mais famósas\n',
                                          'Porque alguém guardaria essa foto em um baú?')

                                    print("Qual item deseja vasculhar?\n\n",
                                          "[1] - Cadeira\n",
                                          "[2] - Espelho\n",
                                          "[3] - Quadro\n",
                                          "[4] - Bau\n",
                                          "[5] - Estátua\n",
                                          "[6] - Bolsa de remédios")

                                    estatua = int(input('>> '))
                                    sleep(5)
                                    os.system('clear')

                                    if estatua == 5 and self.chaveBau == True:

                                        print('Que bela estátua, é uma répica da obra "O Pensador de Agusto Rodin"\n',
                                              '[1] - Olhar a estatua\n',
                                              '[2] - Girar a estatua\n',
                                              '[3] - Não fazer nada')

                                        acaoEstatua = int(input(">> "))

                                        sleep(5)
                                        os.system('clear')

                                        if acaoEstatua == 2 and self.chaveBau == True:  # ===============\\ 2° FINAL //===================
                                            print('Boa escolha, você girou a estatua com delicadeza\n',
                                                  'Um buraco se abre no peito da estátua\n',
                                                  'lhe dando acesso a chave que abre a porta de saída ...')

                                            self.chavePorta = True
                                            sleep(5)
                                            os.system('clear')
                                        else:
                                            print(
                                                'Nada de diferente aconteceu, talvez fosse apenas uma impressão sua...')
