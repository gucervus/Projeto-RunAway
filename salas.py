class salaVermelha():

  def __init__(self):
    self.escrivaninha = False
    self.estante = False
    self.armario = False
    self.guitarra = True
    self.mesaBilhar = False
    
  def acao(self):
    objeto = int(input('Escolha um objeto: '))
    if objeto == 1:
      print('Boa escolha')
    else:
      print('Se fodeu')

