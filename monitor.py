class Monitor:
    contador_monitores = 0

    def __init__(self, marca, tamanio):
        Monitor.contador_monitores += 1
        self.id_monitor = Monitor.contador_monitores
        self.marca = marca
        self.tamanio = tamanio

    def __str__(self):
        return (f'ID: {self.id_monitor}, MARCA: {self.marca},'
                f' TAMAÑO: {self.tamanio}')

# Codigo principal (PRUEBA)
if __name__ == '__main__':
    monitor1 = Monitor('MSI', 18)
    print(monitor1)