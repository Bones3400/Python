#Agregarle la informacion de duracion de cada proceso

import time


def CalcularTiempo(funcion):
    def funcionModificada(n):
        TiempoInicial = time.time()
        funcion(n)
        TiempoFinal = time.time()
        Duracion = TiempoFinal - TiempoInicial
        print(f"Duración del proceso: {Duracion}")

    return funcionModificada


@CalcularTiempo
def imprimirNumeros(n): # <--- esta es función, y arriba pasa a ser funcion modificada
    for i in range(n):
        print(i)

imprimirNumeros(1000)