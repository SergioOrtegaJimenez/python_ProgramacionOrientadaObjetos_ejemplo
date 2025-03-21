from mundo_pc.dispositivo_entrada import DispositivoEntrada


class Teclado(DispositivoEntrada):
    contador_teclados = 0
    def __init__(self, marca, tipo_entrada):
        Teclado.contador_teclados += 1
        self.id_teclado = Teclado.contador_teclados
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return (f'ID: {self.id_teclado}, MARCA: {self.marca},'
                f' TIPO ENTRADA: {self.tipo_entrada}')

# Codigo principal (PRUEBA)
if __name__ == '__main__':
    teclado1 = Teclado('Acer', 'Bluetooth')
    print(teclado1)