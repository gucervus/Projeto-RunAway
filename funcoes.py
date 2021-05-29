import sys
from time import sleep


class Funções:
    def __init__(self, *args, genero, **kwargs):
        super().__init__(*args, **kwargs)
        self.genero = genero

    def animation(self, frase):
        for cont in frase:
            print(cont, end='')
            sys.stdout.flush()
            sleep(0.1)

    def generos(self):
        if self.genero == 'masculino':
            return 'o'
        elif self.genero == 'feminino':
            return 'a'
        else:
            return 'e'
