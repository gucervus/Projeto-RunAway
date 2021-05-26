from relogio import Relógio
from personagem import Personagem
from salas import salaVermelha
<<<<<<< Updated upstream


if (__name__ == "__main__"):
    personagem = Personagem()
    relogio = Relógio(30)
    salas = salaVermelha()
    salas.chave = False

    opcao = input("Qual atributo você escolhe?? ")
=======
from CORES import cores
from time import sleep
import sys


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

    def tempo():
        if personagem.velocidade == True:
            relogio.corretempo(1)
        else:
            relogio.corretempo(2)
>>>>>>> Stashed changes

    print()
    print('-~'*4, 'RunAway', '-~'*4, '\n'*2)

    print(' '*7, '[CADASTRO]', ' '*7, '\n')
    nome = input("Digite seu nome: ")
    gen = input("Digite seu gênero: ").lower()
    alt = float(input("Digite sua altura: "))
    print()
    print()

    bemVindo = f"-~-~-~-~ Bem vind{genero(gen)} -~-~-~-~\n\n"
    animation(bemVindo, 1)

    atributo = '»»»» Escolha um atributo ««««\n\n'
    animation(atributo, 1)

    personagem = Personagem(nome, gen, alt)
    relogio = Relógio(30)
    salas = salaVermelha()
    salas.chave = False

    sleep(1)
    print(''' [1] - Força
 [2] - Velocidade
 [3] - Inteligência
 [4] - Sorte''')
    sleep(.5)

    print()
    print()
    print("Qual atributo você escolhe? \n")
    opcao = int(input('»» '))
    print()
    if opcao == 1:
        personagem.forca = True
        personagem.escolha = "Força"
        frase = f'{personagem}, você pode se dar melhor arrastando objetos pesados!'
        animation(frase, 1)

    elif opcao == 2:
        personagem.velocidade = True
        personagem.escolha = "Velocidade"
<<<<<<< Updated upstream
        print(personagem)
        print()
        print("Você perderá menos tempo a cada escolha")

    while True:
        print(
            f"Você consegue ver uma porta e em cima da porta, um relógio marcando {relogio.minutos} minutos!")
        print()
=======
        frase = f'{personagem}, você perderá menos tempo a cada escolha"'
        animation(frase, 1)

    elif opcao == 3:
        personagem.inteligencia = True
        personagem.escolha = 'Inteligência'
        frase = f'{personagem}, você pensa fora da caixinha! E terá algumas dicas!'
        animation(frase, 1)

    elif opcao == 4:
        personagem.sorte = True
        personagem.escolha = "Sorte"
        frase = f'{personagem}, você pode ter escolhas especiais!'
        animation(frase, 1)

    print('\n'*2)
    print('', '__________________________')
    print('|', ' '*24, '|')
    print('|', ' '*7, ' SALA 1 ', ' '*7, '|')
    print('|__________________________|')
    print('\n'*2)

    sala = "Você acorda em uma sala com paredes vermelhas!\n\n"
    animation(sala, 1)

    fraseSala1 = f"Você consegue ver uma porta e em cima da porta, um {cores['red']}relógio {cores['limpa']}marcando {relogio.minutos} minutos!\n\n"
    animation(fraseSala1, 1)
    sleep(1)

    while True:
        print(f"Você tem {relogio.minutos} minutos para escapar da sala!")
>>>>>>> Stashed changes
        print("O que você deseja fazer? ")
        print(" [1] - Abrir a porta\n",
              "[2] - Vasculhar a sala\n",
              "[3] - Quebrar porta\n")

        opcao2 = int(input("»» "))
        print()

        if opcao2 == 1:
<<<<<<< Updated upstream
            print("Tentar abrir a porta")

            if personagem.velocidade == True:
                relogio.corretempo(2)
            else:
                relogio.corretempo(5)

=======
            tempo()
>>>>>>> Stashed changes
            print("A porta está trancada...")

            if salas.chave == False:
                print("Você não tem a chave! Vasculhe a sala para encontra-la")
                print()
            else:
                deseja = input("Você deseja usar a chave? ")
                if deseja == "sim":
                    print(
                        "Parabéns!! Você abriu a porta e avançou para a próxima sala!")
<<<<<<< Updated upstream
=======
                    relogio.minutos += 30
                    break

>>>>>>> Stashed changes
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
                      "[2] - Olhar Escrivainha\n",
                      "[3] - Empurrar Escrivaninha\n",
                      "[4] - Subir na Escrivaninha\n",)

                opcEscrivaninha = int(input("Escolha: "))

                if opcEscrivaninha == 1:
                    relogio.corretempo(2)
                    print("Você não encontrou nada, só tem lixo!")
                elif opcEscrivaninha == 2:
                    relogio.corretempo(2)
                    print("É uma escrivaninha bonita e resistente!")
                elif opcEscrivaninha == 3:
                    if personagem.forca == True:
                        print("Você empurrou a escrivaninha até a parede.")
<<<<<<< Updated upstream
                    else:
                        print("Você não tem força para empurrar a escrivaninha!")

            #print("A porta é de madeira e você conseguiu quebra-lá")
=======
                        escrivaninhanaparede = True
                    else:
                        print("Você não tem força para empurrar a escrivaninha!")
                elif opcEscrivaninha == 4:
                    if escrivaninhanaparede == True:
                        print(
                            'Você pode ver uma pequena saida de ventilação próxima ao teto.')
                        tempo()
                    else:
                        print('O chão parece mais distante')
                        tempo()
            elif escolha == 2:
                escolhaEstante = int(input('''Você deseja:
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
                escolhaArm = int(input('''Você deseja:
                      [1] - Abrir o armário
                      [2] - Olhar o armário
                      [3] - Empurrar o armário'''))
                if escolhaArm == 1:
                    print(
                        'Dentro do armário vc encontra um bilhete escrito: "Pare de perder tempo!')
                    tempo()
                elif escolhaArm == 2:
                    print('Você está tentando aprender marcenaria?')
                    tempo()
                elif escolhaArm == 3:
                    if personagem.forca == True:
                        print("Você derrubou o Armário.")
                        print('E encontrou uma dica: {}HOJE É DIA DE ROCK BEBÊ!!!{}'.format(
                            cores['azul'], cores['limpa']))
                        tempo()

                    else:
                        print("Você não tem força para empurrar o Armário!")
                        tempo()
            elif escolha == 4:
                print('É uma linda lespaul sunburn Stevie Ray signature 2001')
                print('O que vai fazer?')
                print()
                escolhaGuitarra = int(input('''[1] - Limpar a Guitarra
                        [2] - Quebrar a Guitarra
                        [3] - Tocar a Guitarra 
                        '''))
                if escolhaGuitarra == 1:
                    print('Por que isso é importante?')
                    tempo()
                elif escolhaGuitarra == 2:
                    tempo()
                    tempo()
                    tempo()
                    print('Você quebrou a guitarra e uma chave caiu na sua cabeça!')
                elif escolhaGuitarra == 3:
                    tempo()
                    # play
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
                    salas.chave = True
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

    sala = ""
>>>>>>> Stashed changes
