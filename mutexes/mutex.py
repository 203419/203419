import threading
import threading
from time import sleep

mutex= threading.Lock()
def crito(id):
    global x;
    x = x + id
    print("Hilo =" +str(id)+ " =>" + str(x))
    x=1

class Hilo(threading.Thread):
    def _init_(self, id):
        threading.Thread._init_(self)
        self.id=id

    def run(self):
        mutex.acquire()
        # sleep(3-self.id)
        crito(self.id)
        # print('valor '+ str(self.id))
        mutex.release()
        

hilos = [Hilo(1), Hilo(2), Hilo(3)]
x=1;
for h in hilos:
    h.start()