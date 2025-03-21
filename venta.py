class Venta:
    contador_ventas = 0

    def __init__(self, computadoras):
        Venta.contador_ventas += 1
        self.id_venta = Venta.contador_ventas
        self.computadoras = computadoras # Recibimos la lista de objetos de tipo computadoras

    def agregar_computadora(self, computadora):
        self.computadoras.append(computadora)

    def __str__(self):
        computadoras_str = '' # Creamos una cadena vacia
        for computadora in self.computadoras: # Iteramos cada uno de los objetos de tipo computadora que tenemos en la lista de computadoras
            computadoras_str += '\n' + computadora.__str__() # Concatenamos
        return f'''*** VENTA {self.id_venta} ***
        COMPUTADORAS: {computadoras_str}'''
