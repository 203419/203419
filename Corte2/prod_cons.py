
import threading
import time
import random
import queue


buffer = queue.Queue(10)


class Bodega(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id

    def almacenar(self):
        while True:
            if buffer.qsize() < 10:
                valor = random.randint(1, 10)
                buffer.put(valor)
                print(f'Productor inserta producto: {valor}')
                print(f'Buffer Actual: {list(buffer.queue)}')
                time.sleep(3)
            else:
                time.sleep(3)

    def extraer(self):
        while True:
            if buffer.qsize() > 0:
                valor = buffer.get()
                print(f'Consumidor toma producto: {valor}')
                print(f'Buffer Actual: {list(buffer.queue)}')
                time.sleep(3)
            else:
                time.sleep(3)

    def run(self):
        if self.id < 6:
            self.almacenar()
        else:
            self.extraer()


productores = [Bodega(i) for i in range(5)]
consumidores = [Bodega(i) for i in range(5, 10)]

for p in productores:
    p.start()

for c in consumidores:
    c.start()

