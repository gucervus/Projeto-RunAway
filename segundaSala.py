class salaBranca:
    def __init__(self):
        self.cadeira = True
        self.abajur = True
        self.quadro = True
        self.luminaria = True
        self.estatua = True
        
    def acao(self):
      while True:
        print('[1] - cadeira\n[2] - espelho\n[3] - quadro\n[4] - baú\n[5] - estatua\n[6] - candelabro\n[7] - estojo de remédios\n')
        objeto = input('Qual objeto deseja interagir escolha?: ')

        if objeto == '1':
          print('Você escolheu a cadeira...')
          print('[1] - Vasculhar cadeira\n[2] - Jogar cadeira na parede\n[3] - Sentar para descansar')
          escolha= int(input('>>> '))
          if escolha == 1:
            ler = input('Você encontrou uma carta grudada na cadeira, deseja ler?[sim/não]: ').upper()
            if ler == 'SIM':
              print('***Mensagem sobre a vida***')
              print('Começamos bem, porém ainda não encontramos uma forma de sair daqui, vamos continuar')
            else:
              print('Ok, vamos continuar')
          elif escolha == 2:
            print("Você quebrou a cadeira na parede, mas um pedaço de farpa machucou seu braço")
            print('**Decrementa tempo**')
            ler = input('Você percebeu que nos pedaços de madeira quebrados tem uma carta, deseja ler?').upper()
            if ler == 'SIM':
              print('Você está um pouco "sonzo", e esta perdendo tempo lendo essa carta, vá enfaixar seu braço')
              print('Caso contrário perderá mais tempo que o normal')
              print('**decrementa tempo**')
              print()
              print('[1] - cadeira\n[2] - abajur\n[3] - quadro\n[4] - luminaria\n[5] - estatua\n[6] - candelabro\n[7] - estojo de remédios\n')
              recuperarVida = int(input('>>> '))
              if recuperarVida == 7:
                print('Boa escolha, dentro do estojo de remédios temos analgésicos e gaze para o seu machucado')
                print("Pode continuar sem nenhum problema")
                # Decrementa normalmente
              else:
                #Decrementa 5 minutos a cada 10 minutos passados
                continue
            
          elif escolha == 3:
            print('Que situação maluca, descansar é sempre bom!')
            print('Você conseguiu enxergar o reflexo de alguma coisa')
            print('O que deseja fazer?')

            print('[1] - cadeira\n[2] - espelho\n[3] - quadro\n[4] - luminaria\n[5] - estatua\n[6] - candelabro\n[7] - estojo de remédios\n')
            objeto = input('Qual objeto deseja interagir escolha?: ')
            if objeto == '2':
              print('O que você viu no espelho?')
              print('[1] - Dinossauro\n[2] - guarda - roupa\n[3] - Estatua')
              visualizar = int(input('>>> '))
              if visualizar != 3:
                print('Você está muito cansado, é impossível isso estar na sala, descanse 5 minutos')
                # Decrementa 5 mintuos
              else:
                print('A sala realmente tem uma estatua, o que quer fazer?')
                print('''
                [1] - Quebrar a estatua 
                [2] - Girar a estatua
                [3] - Não fazer nada
                ''')
                estatua = int(input('>>> '))
                if estatua == 1:
                  print('Seu emocional está quebrado... Você está quebrando objetos como se não ouvesse consequencias')
                  #Decrementa 1 minuto
                elif estatua == 2: #        =================\\FIM //============================
                  print('Boa escolha, você girou a estatua com delicadeza, isso possibilitou a porta de saida abrir')
                  break
                elif estatua == 3:
                  continue

        elif objeto == '2':
          print('O que você viu no espelho?')
          print('[1] - Seu próprio reflexo\n[2] - Qudaro \n[3] - Violão')
          visualizar = int(input('>>> '))
          
          if visualizar == 1:
            print('''
            Você é uma pessoa muito bonita, porém 
            já tem problemas o suficiente para ficar se olhando no espelho
            ''')
            # Decrementa 5 minutos
          elif visualizar == 2:
            print('''
            É um quadro lindo, deseja chegar mais perto?
            ''') 
            quadro = input(' ').upper()

            if quadro == 'SIM':
              print('O quadro da sala é a Dama com Arminho de Leonardo da Vince')
              print('Que linda peça!')
              print('''
              [1] - Vasculhar o quadro
              [2] - Admirar o quadro
              [3] - Rasgar o quadro''')
              acao = input('O que deseja fazer? ')

              if acao == 1: 
                print('Você não encontrou nada...')
                #Decrementa 5
              elif acao == 2:
                print('Essa realmente é uma obra muito bonita, entendo você querer adimirá-la')
                print('Porem seu tempo está correndo')
                #Decrementa 5 minutos
              elif acao == 3: 
                print('Que loucura rasgar um quadro tão lindo quanto esse...Da Vince acaba de se revirar no tumulo')
                print('Porem situações desesperadas pedem medidas desesperadas')
                print('Você encontrou dentrou do quadro uma chave... O que deseja fazer?')
                chave == True
                print('[1] - cadeira\n[2] - espelho\n[3] - quadro\n[4] - luminaria\n[5] - estatua\n[6] - candelabro\n[7] - estojo de remédios\n')
                objeto = input('Qual objeto deseja interagir escolha?: ')
                if objeto == '5' and chave == True:
                  print('Abrir o baú com a chave foi uma ótima escolha, nele se encontra uma foto')
                  print('Nela se encontra Rodin, ao lado de uma de suas obras mais famósas')
                  print('Porque alguém guardaria essa foto em um baú?')

                  print('[1] - cadeira\n[2] - espelho\n[3] - quadro\n[4] - luminaria\n[5] - estatua\n[6] - candelabro\n[7] - estojo de remédios\n')
                objeto = input('Qual objeto deseja interagir escolha?: ')
                if objeto == '6' and chave == True:
                  print('Que bela estátua, é uma répica da obra "O Pensador de Agusto Rodin"')
                  print('''
                [1] - Quebrar a estatua 
                [2] - Girar a estatua
                [3] - Não fazer nada
                ''')
                estatua = int(input('O que deseja fazer com ela? '))
                if estatua == 2:
                  print('Boa escolha, você girou a estatua com delicadeza, isso possibilitou a porta de saida abrir')
                  break
                else:
                  print('Nada de diferente aconteceu, talvez fosse apenas uma impressão sua...')
              


  