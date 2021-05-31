import matplotlib.pyplot as plt
import matplotlib.image as img
import sys


class Imagens:
    def __init__(self):
        self.imagem = True

    def showImage(self, path):
        image = img.imread(f'{path}')
        sys.stdout.flush()
        plt.imshow(image)
        plt.axis('off')
        plt.show()
