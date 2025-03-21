from mundo_pc.computadora import Computadora
from mundo_pc.monitor import Monitor
from mundo_pc.raton import Raton
from mundo_pc.teclado import Teclado
from mundo_pc.venta import Venta

# Creamos los objetos
teclado1 = Teclado('HP', 'USB')
raton1 = Raton('Acer', 'Bluetooth')
monitor1 = Monitor('MSI', 18)
computadora1 = Computadora('MSI TITAN', monitor1, raton1, teclado1)

# Creamos la lista de computadoras
computadoras1 = [computadora1]
venta1 = Venta(computadoras1)

# Agregamos una nueva computadora
teclado2 = Teclado('Dell', 'USB')
raton2 = Raton('HP', 'USB')
monitor2 = Monitor('Philips', 16)
computadora2 = Computadora('PC Oficina', monitor2, raton2, teclado2)
venta1.agregar_computadora(computadora2)
print(venta1)