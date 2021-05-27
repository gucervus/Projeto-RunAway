class Personagem:
    def __init__(self, nome, altura, genero):
        self.nome = nome
        self.altura = altura
        self.genero = genero
        self.forca = 0
        self.velocidade = 0
        self.inteligencia = 0
        self.sorte = 0
        self.escolha = 0

    def __str__(self):
        return "Você escolheu" + (f" {self.escolha} cabrunco")
