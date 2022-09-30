
from threading import Thread
from threading import Lock
import time

lock = Lock()

def tomar_palillo(id):
    lock.acquire()
    print(f"Persona {id} tomo palillo")
    

def dejar_palillo(id):
    lock.release()
    print(f"Persona {id} dejo palillo")


def comer(id):
    print(f"Persona {id} comiendo")
    time.sleep(3)
    print(f"Persona {id} termino de comer")
    time.sleep(3)


class Persona(Thread):
    def __init__(self, id):
        Thread.__init__(self)
        self.id = id

    def run(self):
        tomar_palillo(self.id)
        comer(self.id)
        dejar_palillo(self.id)


personas = [Persona(1), Persona(2), Persona(3), Persona(4), Persona(5), Persona(6), Persona(7), Persona(8)]

for p in personas:
    p.start()

