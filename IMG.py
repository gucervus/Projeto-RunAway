import cv2 as cv
import sys

class Imagem:
    def __init__(self):
        self.imagem = True
    
    def createImage(self, path):
        self.imagem = cv.imread(cv.samples.findFile("Quadro.jpg"))
    
    def showImage(self):
        img = self.imagem
        if img is None:
            sys.exit("Could not read the image.")
        
        cv.imshow("A dama de arminho", img)

        k = cv.waitKey(0)

        if k == ord("s"):
            cv.imwrite("Quadro.jpg", img)


        
        
        
        
        
        
        
        
        
        
        
        
        
        


        
        