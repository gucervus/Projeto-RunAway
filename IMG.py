import matplotlib.pyplot as plt
import matplotlib.image as img

class Imagens:
    def __init__(self):
        self.imagem = True
        
    def showImage(self,path):
        image = img.imread(f'{path}')
        plt.imshow(image)
        plt.axis('off')
        plt.show()


        
