from PIL import Image

class Img():
    def __init__(self):
        self.imagem = True
    
    def insertImage(self, path):
        self.imagem = Image.open(f'{path}')
    
    def showImage(self):
        return self.imagem

        
        