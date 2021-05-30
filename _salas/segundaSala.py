from personagem import Personagem
from relogio import Relógio
from funcoes import Funções
from time import sleep
from CORES import cores
import os
import pygame
from IMG import Img


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
        imagem = Img()

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
        self.animation(sala)

        fraseSala1 = f"Lembre-se que acima da porta há um {cores['red']}relógio {cores['limpa']},marcando agora {relogio.minutos} minutos,\n"
        self.animation(fraseSala1)
        fraseSala2 = "Você consegue ver uma cadeira, um espelho, um quadro, um bau, uma estátua e uma bolsa de...\n\n"
        self.animation(fraseSala2)
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
                        
                        relogio.corretempo(2)
                        print()
                        
                        print("Você não encontrou uma carta grudada na cadeira, deseja ler? [sim/não]\n")
                        ler = input('>> ').upper()

                        if ler == 'SIM':
                            
                            imagem.insertImage('_img/poerma3.jpg')
                            imagem.showImage()
                            
                            continuar = input('Pressione Enter para continuar: ')
                            if continuar == '':
                                os.system('clear')
                                relogio.corretempo(2)

                            print('Começamos bem, porém ainda não encontramos uma forma de sair daqui, vamos continuar')
                            sleep(5)
                            os.system('clear')
                        else:
                            print('Ok, vamos continuar')
                            sleep(5)
                            os.system('clear')

                    elif opcaoCadeira == 2:
                        
                        relogio.corretempo(2)
                        print("Você quebrou a cadeira na parede, mas um pedaço de farpa machucou seu braço\n",
                              'Você percebeu que nos pedaços de madeira quebrados tem uma carta, deseja ler?\n')
                        ler = input('>> ').upper()
                        
                        sleep(5)
                        os.system('clear')

                        if ler == 'SIM':
                            
                            print("Você está um pouco sonzo, e esta perdendo tempo lendo essa carta, vá enfaixar seu braço\n",
                                  "Caso contrário perderá mais tempo que o normal\n")
                            
                            sleep(5)
                            os.system('clear')
                            relogio.corretempo(2)
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
                                relogio.corretempo(7)
                                
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
                                print('Você está muito cansado, é impossível isso estar na sala.\n',
                                      'descanse 5 minutos!')

                                relogio.corretempo(5)
                                sleep(5)
                                os.system('clear')

                            else:
                                print('A sala realmente tem uma estatua, o que quer fazer?\n',
                                      '[1] - Olhar a estatua\n',
                                      '[2] - Girar a estatua\n',
                                      '[3] - Não fazer nada\n')
                                
                                estatua = int(input('>>> '))
                                sleep(5)
                                os.system('clear')

                                if estatua == 1:
                                    print('Nada de diferente aconteceu, talvez fosse apenas uma impressão sua...')

                                    relogio.corretempo(1)
                                    sleep(5)
                                    os.system('clear')
                                    
                                elif estatua == 2:  # =================\\ 1° FINAL //============================
                                    print('Boa escolha, você girou a estatua com delicadeza\n',
                                          'Um buraco se abre no peito da estátua\n',
                                          'lhe dando acesso a chave que abre a porta de saída ...')

                                    self.chavePorta = True  
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
                        
                        print('É um quadro lindo, deseja chegar mais perto? [sim/não]')
                        quadro = input(' ').upper()

                        sleep(5)
                        os.system('clear')

                        if quadro == 'SIM':
                            print('O quadro da sala é a Dama com Arminho de Leonardo da Vince\n',
                                  'Que linda peça!')
                            
                            imagem.insertImage('_img/DamaArminho.jpg')   
                            imagem.showImage()
                            
                            continuar = input("Pressione enter para continuar: ")
                            if continuar == '':
                                os.system('clear')
                                relogio.corretempo(2)
                                 

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
                                      'Porem seu tempo está correndo')
                                relogio.corretempo(5)

                            elif acaoQuadro == 3:

                                print('Que loucura rasgar um quadro tão lindo quanto esse...\n',
                                      'Da Vince acaba de se revirar no tumulo\n',
                                      'Porem situações desesperadas pedem medidas desesperadas\n',
                                      'Você encontrou dentrou do quadro uma chave...')
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
                                          'Nela se encontra Rodin, ao lado de uma de suas obras mais famosas\n',
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

                                        print('Que bela estátua, é uma réplica da obra "O Pensador de Agusto Rodin"\n',
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
                                            print('Nada de diferente aconteceu, talvez fosse apenas uma impressão sua...\n')
                elif objetos == 3:
                    
                    print("Você deseja: \n\n",
                          "[1] - Vasculhar o quadro\n",
                          "[2] - Quebrar o quadro\n",
                          "[3] - Admirar o quadro\n",)
                    
                    acaoQuadro = int(input('>> '))
                    
                    if acaoQuadro == 1:
                        print('O quadro da sala é a Dama com Arminho de Leonardo da Vince!\n\n',
                              'Ao vasculhar o quadro você encontrou uma bilhete de viagem\n,'
                              'Oque um bilhete de viagem faria atrás de um quadro?\n')  # Conceito para a próxima versão
                        
                        bilhete = True
                        print('Você deseja: \n\n',
                              '[1] - Ler o bilhete\n',
                              '[2] - Guardar o bilhete\n',
                              '[3] - Rasgar o bilhete?\n')
                        
                        acaoBilhete = int(input(">> "))
                        
                        if acaoBilhete == 1 and bilhete == True:
                            
                            print('Bilhete de onibus: \n',
                                  'Valor da passagem: R$5,50\n',
                                  'Destino: Praia do sono\n\n',
                                  'O que um bilhete de viagem faria aqui?') # Melhorar pergunta com o atributo inteligencia
                            
                        elif acaoBilhete == 2 and bilhete == True:
                            
                            print('Ele pode vir a ser útil em outro momento...\n')
                        
                        elif acaoBilhete == 3 and bilhete == True:
                            
                            print('Você nem se interessou em saber o que estava escrito\n',
                                  'provavelmente não tem intenção nenhuma de sair daqui\n')
                            
                            relogio.corretempo(5)
                            bilhete = False
                            
                    elif acaoQuadro == 2:
                        
                        print('Você quebrou um belo quadro, sem nem mesmo observar!\n\n',
                              'Você começa a se sentir cansado e sem forças\n',
                              'Continuar agora sem descansar pode lhe trazer consequências\n\n',
                              'Deseja tomar um descanso?[sim/não]\n')
                        
                        descanso = input(">> ").upper()
                        
                        if descanso == 'SIM':
                            print('Descanse um pouco...')
                            relogio.corretempo(2)  
                        
                        else:
                            print('A vida é feita de escolhas...')
                            relogio.corretempo(10)
                    
                    elif acaoQuadro == 3:
                        
                        print('O quadro da sala é a Dama com Arminho de Leonardo da Vince!\n',
                              'Uma de suas grandes obras, hoje estimada em 350 Milhões de Euros...\n\n',
                              'Essa era uma das obras preferidas da sua mãe\n',
                              'Ela com certeza tinha um gosto refinado para quadros\n',)
                        
                        print('Uma pequena entrada se abre na lateral do quadro...\n',
                              'Deseja entrar? [sim/não]\n')
                        
                        entrar = input(">> ").upper()
                        
                        if entrar == 'SIM':
                            
                            print("Você agora se encontra em uma casa...\n\n")
                            
                            print(' '*20, end='')
                            print('', '__________________________')
                            print(' '*20, end='')
                            print('|', ' '*24, '|')
                            print(' '*20, end='')
                            print('|', ' '*7, ' CASA ', ' '*7, '|')
                            print(' '*20, end='')
                            print('|__________________________|')
                            print('\n'*2)
                            
                            print()
                            
                            print("Seus pais te chamam para uma volta de carro\n",
                                  'aparentemente estão indo visitar alguém.\n\n',
                                  'Você entra no carro e todos partem para viagem\n',
                                  'porém já na estrada você nota que esqueceu o celular\n',)
                            
                            lembranca = True
                            relogio.corretempo(3)
                            
                        else:
                            continue
                        
                elif objetos == 2 and lembranca == True:
                    
                    print('O que você vê no espelho?\n',
                        '[1] - Estátua\n',
                        '[2] - Baú\n',
                        '[3] - Seu reflexo')
                    
                    acaoEspelho = int(input(">> "))
                    
                    if acaoEspelho == 3:
                        
                        print('Ao se ollhar você começa a se lembrar do que realmente aconteceu!\n\n',
                              'Você estava em uma estrada com sua família e um caminhão entrou na pista\n',
                              'Aparentemente o caminhoneiro estava embriagado e causou um acidente\n',
                              'Você e sua familia vivenciaram um trauma muito grande, e nesse momento\n',
                              'Você está em uma cama de hospital...\n\n')
                        
                        relogio.corretempo(3)
                        
                elif objetos == 6 and lembranca == True:
                    
                    print("Você deseja: \n\n",
                          "[1] - Abrir a bolsa\n",
                          "[2] - Jogar a bolsa no lixo\n",
                          "[3] - Não fazer nada\n",)
                    
                    acaoBolsa = int(input('>> '))
                    
                    if acaoBolsa == 1:
                        print("Você abre a bolsa e encontra o que aparentemente é a chave de um baú\n")
                        
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
                                    'Nela se encontra Rodin, ao lado de uma de suas obras mais famosas\n',
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

                                if acaoEstatua == 2 and self.chaveBau == True:  # ===============\\ 3° FINAL //===================
                                    print('Boa escolha, você girou a estatua com delicadeza\n',
                                            'Um buraco se abre no peito da estátua\n',
                                            'lhe dando acesso a chave que abre a porta de saída ...')

                                    self.chavePorta = True
                                    sleep(5)
                                    os.system('clear')
                                else:
                                    print('Nada de diferente aconteceu, talvez fosse apenas uma impressão sua...\n')
                    
                elif objetos == 4:
                    
                    print("Você deseja: \n\n",
                          "[1] - Abrir o baú",
                          "[2] - Vasculhar o baú\n",
                          "[3] - Não fazer nada\n",)
                    
                    acaoBau = int(input('>> '))
                    self.chaveBau = False
                    
                    if acaoBau == 1 and self.chaveBau == False:
                        print('Você necessita de uma chave para abri-lo')
                    
                    elif acaoBau == 2:
                        print('Você não encontrou nada ao vasculhar o baú...')
                    elif acaoBau == 3:
                        continue
                
                elif objetos == 5:
                    
                    print("Você deseja: \n\n",
                          "[1] - Admirar a estátua\n",
                          "[2] - Não fazer nada\n",)

                    acaoEstatua = int(input('>> '))
                    
                    if acaoEstatua == 1:
                        
                        print('Que bela estátua, é uma réplica da obra "O Pensador de Agusto Rodin\n',
                              'é uma das mais famosas esculturas de bronze do escultor francês Auguste Rodin.\n',
                              'Retrata um homem em meditação soberba, lutando com uma poderosa força interna.\n',
                              'O Pensador originalmente procurava retratar Dante em frente dos Portões do Inferno,\n',
                              'ponderando seu grande poema...\n')
                    
                    else:
                        continue
                elif objetos == 6:
                    
                    print('Uma bolsa de remédios pode ser útil em momentos de necessidade\n',
                          'Fique atento caso precise de cuidados médicos\n') 
                    
                    print("Você deseja: \n\n",
                          "[1] - Abrir a bolsa\n",
                          "[2] - Não fazer nada\n",)
                    
                    acaoBolsa = int(input('>> '))
                    
                    if acaoBolsa == 1:
                        print('Na bolsa temos analgésicos e gaze para uma eventual necessidade\n')
                    else: 
                        continue          
                            
                                
                            