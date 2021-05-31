from time import sleep
import sys


class Imagem:
    def animation(self, imagem):
        for c in imagem:
            print(c, end='')
            sys.stdout.flush()
            sleep(0.01)
