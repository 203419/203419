# Sebastian Ramirez Virves - 203419 
# Diego Chacon Pimentel - 203414

import threading
import time
import queue
import random

capacidad = queue.Queue(maxsize=20)
meseros = queue.Queue(maxsize=2)
cocineros = queue.Queue(maxsize=2)
clientes_esperando = queue.Queue()
reservaciones = queue.Queue(maxsize=4) 
reservaciones_esperando = queue.Queue()
ordenes = queue.Queue()
ordenes_terminadas = queue.Queue()


class Cliente(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        # self.id = id
        self.monitor = threading.Condition()

    def comer(self):
        while True:
            with self.monitor:
                if not ordenes_terminadas.empty():
                    id_cliente = capacidad.get()
                    print(f'Cliente {id_cliente} esta comiendo su orden')
                    time.sleep(random.randint(4, 7))
                    print(f'Cliente {id_cliente} termino de comer y se fue')
                    ordenes.get()
                    self.monitor.notify()


    def run(self):
        self.comer()


class Reservacion(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id
        self.monitor = threading.Condition()

    def reservar(self):
        while True:
            with self.monitor:
                if not reservaciones.full():
                    reservaciones.put(self.id)
                    print(f'Cliente {self.id} de reservaciones reservo un lugar')
                    self.monitor.notify()
                    time.sleep(10)
                else:
                    print(f'Cliente {self.id} quiso reservar pero no hay espacio, se mando a la cola de espera')
                    clientes_esperando.put(self.id)
                    time.sleep(20)
                self.id = self.id + 1


    def run(self):
        self.reservar()


class Mesero(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.monitor = threading.Condition()

    def atender(self):
        while True:
            with self.monitor:
                if not capacidad.empty() and capacidad.qsize()>1:
                    if meseros.empty():
                        meseros.put(1)
                        print(f'Un mesero esta tomando la orden')
                        time.sleep(3)
                        print(f'La orden esta en proceso')
                        ordenes.put(1)
                        meseros.get()
                        self.monitor.notify()
                    else:
                        print(f'Los meseros estan ocupados')
                        time.sleep(2)
                else:
                    print(f'los meseros estan descansando')
                    time.sleep(2)

    def run(self):
        self.atender()


class Cocinero(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.monitor = threading.Condition()

    def cocinar(self):
        while True:
            with self.monitor:
                if not ordenes.empty():
                    if cocineros.empty():
                        cocineros.put(1)
                        print(f'Un cocinero esta cocinando')
                        time.sleep(4)
                        ordenes.get()
                        print(f'La orden esta lista')
                        cocineros.get()
                        ordenes_terminadas.put(1)
                        self.monitor.notify()
                    else:
                        print(f'Los cocineros estan ocupados')
                        time.sleep(2.5)

    def run(self):
        self.cocinar()


class Recepcionista(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.monitor = threading.Condition()
        self.id = id

    def atender(self):
        while True:
            with self.monitor:
                if reservaciones.qsize() > 2:
                    capacidad.put(self.id)
                    print(f'Cliente {self.id} que contaba con una reservacion fue atendido')
                    reservaciones.get()
                    self.monitor.notify()
                    time.sleep(3)
                    
                else:
                    if clientes_esperando.empty():
                        if not capacidad.full():
                            capacidad.put(self.id)
                            print(f'Cliente {self.id} fue atendido')
                            self.monitor.notify()
                            time.sleep(3)
                        else:
                            print(f'Cliente {self.id} esta esperando')
                            clientes_esperando.put(self.id)
                            print(f'Hay {clientes_esperando.qsize()} clientes esperando')
                            time.sleep(6)
                        
                    else:
                        print(f'Cliente {self.id} esta esperando')
                        clientes_esperando.put(self.id)
                        print(f'Hay {clientes_esperando.qsize()} clientes esperando')
                        time.sleep(6)

            self.id = self.id + 1

    def run(self):
        self.atender()


if __name__ == '__main__':
    hilo_recepcion = Recepcionista(1)
    hilo_recepcion.start()

    hilo_cliente = Cliente(1)
    hilo_cliente.start()

    hilo_reservacion = Reservacion(1)
    hilo_reservacion.start()
    
    hilo_mesero = Mesero()
    hilo_mesero.start()

    hilo_cocinero = Cocinero()
    hilo_cocinero.start()
