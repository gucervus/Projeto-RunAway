from relogio import Relógio
from personagem import Personagem
from salas import salaVermelha


if (__name__ == "__main__"):
    personagem = Personagem()
    relogio = Relógio(30)
    salas = salaVermelha()
    salas.chave = False

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

    while True:
        print(
            f"Você consegue ver uma porta e em cima da porta, um relógio marcando {relogio.minutos} minutos!")
        print()
        print("O que você deseja fazer? ")
        print(" [1] - Abrir a porta\n",
              "[2] - Vasculhar a sala\n",
              "[3] - Quebrar porta")

        opcao2 = int(input("Escolha: "))

        if opcao2 == 1:
            print("Tentar abrir a porta")

            if personagem.velocidade == True:
                relogio.corretempo(2)
            else:
                relogio.corretempo(5)

            print("A porta está trancada...")
            print(f"Restam {relogio.minutos}")

            if salas.chave == False:
                print("Você não tem a chave! Vasculhe a sala para encontra-la")
            else:
                deseja = input("Você deseja usar a chave? ")
                if deseja == "sim":
                    print(
                        "Parabéns!! Você abriu a porta e avançou para a próxima sala!")
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
                    else:
                        print("Você não tem força para empurrar a escrivaninha!")

            #print("A porta é de madeira e você conseguiu quebra-lá")
