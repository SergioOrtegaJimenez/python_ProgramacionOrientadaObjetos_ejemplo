from mundo_pc.dispositivo_entrada import DispositivoEntrada


class Raton(DispositivoEntrada):
    contador_ratones = 0
    # Constructor
    def __init__(self, marca, tipo_entrada):
        Raton.contador_ratones += 1
        self.id = Raton.contador_ratones
        #self.marca = marca
        #self.tipo_entrada = tipo_entrada
        super().__init__(marca, tipo_entrada) #  Esta forma de reutilizacion del constructor de la clase Padre es mas recomendable. Realiza la misma funcion que las 2 lineas anteriores.

    def __str__(self):
        return (f'ID: {self.id}, MARCA: {self.marca},'
                f' TIPO ENTRADA: {self.tipo_entrada}')

# Codigo principal (PRUEBA)
if __name__ == '__main__': # Indica que el codigo a continuacion solo se ejecutara si se hace desde este mismo archivo (raton.py)
    raton1 = Raton('HP', 'USB')
    print(raton1)