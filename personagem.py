class Personagem:
    def __init__(self, nome, altura, genero, escolha):
        self.nome = nome
        self.altura = altura
        self.genero = genero
        self.escolha = escolha

    def __str__(self):
        return "Você escolheu" + (f" {self.escolha} cabrunco")
