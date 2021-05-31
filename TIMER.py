import time

class Timer:
    def __init__(self, value = 0):
        self.start = time.time()
        self.set(value)

    def start(self, args):
        self.timer = Timer(10)

    def update(self):
        print(self.timer.get())

        
    def set(self, value : float):
        self.start = time.time() - value


    def get(self) -> float:
        return time.time() - self.start 
    
    def __str__(self):
        value = self.get()
        sec = int(value)
        min = int(sec/60)
        sec=int(value)
        return str(min) +'m '+str(sec)+'s ' 
        