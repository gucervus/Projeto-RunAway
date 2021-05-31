import os 
from time import sleep
class Clear:
    def __init__(self):
        self.clear = True
    
    def clearSystem(self):
        if os.name == 'nt':
            self.clear = os.system('cls')
        else:
            self.clear = os.system('clear')

    def clearAll(self):
        return self.clear


clear = Clear()
print('iuasdhuisahfuidshfiudshfuidsafhdsiufhds')
print('sadifdisuhfiudshfdsafidsafhdisafdsafdsaf')
print('sadfdsafhdsuifhiudshfiudshfiudshfiuhds')
sleep(2)
clear.clearSystem()
clear.clearAll()