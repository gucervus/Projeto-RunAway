
<<<<<<< Updated upstream
class Relógio:
    def __init__(self, minutos):
        self.minutos = minutos
        self.fimdotempo = False
=======

class Relógio(Personagem):
    def __init__(self, minutos, nome, altura, escolha):
        self.minutos = minutos
        super().__init__(nome, altura, escolha)

    def corretempo(self, minutos):

        if self.escolha == 'Velocidade':
            total = minutos // 2
            self.minutos -= total
        else:
            self.minutos -= minutos
>>>>>>> Stashed changes

    def __str__(self):
        return f'{self.minutos:02d}'
    
    def corretempo(self, minutos):
        self.minutos -= minutos
        if minutos<=0:
            fimdotempo=True
fimdotempo=False
relogio = Relógio(30)

#Parte de teste
"""while fimdotempo == False:
    print("---")
    print("Ainda restam "+str(relogio)+" minutos")
    print("")
    print("Ações:")
    print("1 - Tentar")
    
    print("0 - Sair do jogo")
    opcao = input("Escolha sua ação:")
    if(opcao == "1") and (relogio.minutos > 0):
        relogio.corretempo(5)
    if relogio.minutos <= 0:
        fimdotempo = True   
        print('ACABOU O TEMPO')
        break
        
    elif(opcao == '0'):
        print('Tente amanhã!')
        break
    """

    

    