from mundo_pc.monitor import Monitor
from mundo_pc.teclado import Teclado
from mundo_pc.raton import Raton

class Computadora:
    contador_computadora = 0

    def __init__(self, nombre, monitor, raton, teclado):
        Computadora.contador_computadora += 1
        self.id_computadora = Computadora.contador_computadora
        self.nombre = nombre
        self.monitor = monitor
        self.raton = raton
        self.teclado = teclado

    def __str__(self):
        return (f'''{self.nombre}: {self.id_computadora}
                    MONITOR: {self.monitor} 
                    TECLADO: {self.teclado} 
                    RATON: {self.raton}''')


# Codigo principal (PRUEBA)
if __name__ == '__main__':
    teclado1 = Teclado('HP', 'USB')
    raton1 = Raton('Acer', 'Bluetooth')
    monitor1 = Monitor('MSI', 18)
    computadora1 = Computadora('MSI TITAN', monitor1, raton1, teclado1)
    print(computadora1)