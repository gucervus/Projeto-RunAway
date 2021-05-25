class Personagem:
    def __init__(self):
        self.forca = False
        self.velocidade = False
        self.inteligencia = False
        self.sorte = False
        self.escolha = False

    def __str__(self):

        return "Você escolheu" + (f" {self.escolha} cabrunco")

 

