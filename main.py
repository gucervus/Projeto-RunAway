from relogio import Relógio
from personagem import Personagem
from salas import salaVermelha
from CORES import cores
from time import sleep
if (__name__ == "__main__"):
    personagem = Personagem()
    relogio = Relógio(30)
    salas = salaVermelha()
    salas.chave = False
    def tempo():
        if personagem.velocidade == True:
            relogio.corretempo(1)
        else:
            relogio.corretempo(2)
    gen='x'
    print(' [1] - Força\n', 
          '[2] - Velocidade\n',
          '[3] - Inteligência\n',
          '[4] - Sorte\n')
    opcao = input("Qual atributo você escolhe?? ")

    print()
    print("Você acorda em uma sala com paredes vermelhas!")
    print()

    if opcao == "1":
        personagem.forca = True
        personagem.escolha = "Força"
        print(personagem)
        print()
        print("Você pode se dar melhor arrastando objetos pesados")

    elif opcao == "2":
        personagem.velocidade = True
        personagem.escolha = "Velocidade"
        print(personagem)
        print()
        print("Você perderá menos tempo a cada escolha")
    elif opcao == '3':
        personagem.inteligencia = True
        personagem.escolha = 'Inteligência'
        print(personagem)
        print()
        print("Você pensa fora da caixinha! E terá algumas dicas")

    elif opcao == '4':
        personagem.sorte = True
        personagem.escolha = "Sorte"
        print(personagem)
        print()
        print('Você pode ter escolhas especiais')

    while True:
        print(
            f"Você consegue ver uma porta e em cima da porta, um {cores['red']}relógio {cores['limpa']}marcando {relogio.minutos} minutos!")
        print()
        print("O que você deseja fazer? ")
        print(" [1] - Abrir a porta\n",
              "[2] - Vasculhar a sala\n",
              "[3] - Quebrar porta")

        opcao2 = int(input("Escolha: "))

        if opcao2 == 1:
            print("Tentar abrir a porta")

            tempo()

            print("A porta está trancada...")
            print(f"Restam {relogio.minutos}")

            if salas.chave == False:
                print("Você não tem a chave! Vasculhe a sala para encontra-la")
            else:
                deseja = input("Você deseja usar a chave? ")
                if deseja == "sim":
                    print(
                        "Parabéns!! Você abriu a porta e avançou para a próxima sala!")
                    relogio.minutos += 30
                    break
                    
                elif deseja == "nao":
                    print("Você achou melhor guardar a chave.")

        elif opcao2 == 2:
            print(
                "Você consegue ver na sala uma escrivaninha, uma estante, um armário, uma guitarra e uma mesa de bilhar...")
            print("[1] - Escrivaninha\n",
                  "[2] - Estante\n",
                  "[3] - Armário\n",
                  "[4] - Guitarra\n",
                  "[5] - Mesa de bilhar\n")

            escolha = int(input("Qual item deseja vasculhar?"))

            if escolha == 1:
                print("Você deseja: \n",
                      "[1] - Vasculhar Escrivaninha\n",
                      "[2] - Olhar Escrivaninha\n",
                      "[3] - Empurrar Escrivaninha\n",
                      "[4] - Subir na Escrivaninha\n",)

                opcEscrivaninha = int(input("Escolha: "))

                if opcEscrivaninha == 1:
                    tempo()
                    print("Você não encontrou nada, só tem lixo!")
                elif opcEscrivaninha == 2:
                    tempo()
                    print("É uma escrivaninha bonita e resistente!")
                elif opcEscrivaninha == 3:
                    tempo()
                    if personagem.forca == True:
                        print("Você empurrou a escrivaninha até a parede.")
                        escrivaninhanaparede=True
                    else:
                        print("Você não tem força para empurrar a escrivaninha!")
                elif opcEscrivaninha == 4:
                    if escrivaninhanaparede==True:
                        print('Você pode ver uma pequena saida de ventilação próxima ao teto.')
                        tempo()
                    else:
                        print('O chão parece mais distante')
                        tempo()
            elif escolha ==2:
                escolhaEstante=int(input('''Você deseja:
                [1] - Vasculhar Estante
                [2] - Olhar Estante
                [3] - Empurrar Estante'''))
                if escolhaEstante == 1:
                    tempo()
                    print('Você encontra os seguintes livros: "O segredo", "A arte da guerra", "A lei da atração", "O capital", "Harry Potter e a Pedra filosofal". ')
                elif escolhaEstante == 2:
                    print('Tem alguns livros na estante.')
                    tempo()
                elif escolhaEstante == 3:
                    tempo()
                    if personagem.forca == True:
                        print("Você derrubou a estante.")
                        
                    else:
                        print("Você não tem força para empurrar a estante!")
            elif escolha == 3:
                escolhaArm=int(input('''Você deseja:
                      [1] - Abrir o armário
                      [2] - Olhar o armário
                      [3] - Empurrar o armário'''))
                if escolhaArm == 1:
                    print('Dentro do armário vc encontra um bilhete escrito: "Pare de perder tempo!')
                    tempo()
                elif escolhaArm == 2:
                    print('Você está tentando aprender marcenaria?')
                    tempo()
                elif escolhaArm == 3:
                    if personagem.forca == True:
                        print("Você derrubou o Armário.")
                        print('E encontrou uma dica: {}HOJE É DIA DE ROCK BEBÊ!!!{}'.format(cores['azul'],cores['limpa']))
                        tempo()
                        
                    else:
                        print("Você não tem força para empurrar o Armário!")
                        tempo()
            elif escolha == 4:
                print('É uma linda lespaul sunburn Stevie Ray signature 2001')
                print('O que vai fazer?')
                print()
                escolhaGuitarra=int(input('''[1] - Limpar a Guitarra
                        [2] - Quebrar a Guitarra
                        [3] - Tocar a Guitarra 
                        '''))
                if escolhaGuitarra == 1:
                    print('Por que isso é importante?')
                    tempo()
                elif escolhaGuitarra== 2:
                    tempo()
                    tempo()
                    tempo()
                    print('Você quebrou a guitarra e uma chave caiu na sua cabeça!')
                elif escolhaGuitarra==3:
                    tempo()
                    #play
                    print('Que música linda! Os deuses do rock estão satisfeitos...')
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
                    salas.chave=True
            elif escolha == 5:
                print('Tá com saudade do boteco né minha filha?')
                tempo()







                
        elif opcao2 == 3:
            if personagem.forca == True:
                print("A porta é de madeira e você conseguiu quebra-la")
                break
            else:
                print('Você é frac{} demais pra isso'.format(gen))
                tempo()
        



            #
