from personagem import Personagem


class Relógio(Personagem):
    def __init__(self, minutos, nome, altura, atributo):
        self.minutos = minutos
        super().__init__(nome, altura, atributo)


    def corretempo(self, minutos):

        if self.atributo == 'Velocidade':
            total = minutos // 2
            self.minutos -= total
        else:
            self.minutos -= minutos

    def __str__(self):
        return f'{self.minutos:02d}'
