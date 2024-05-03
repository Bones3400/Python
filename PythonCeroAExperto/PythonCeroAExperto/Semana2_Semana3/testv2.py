print("Visualizar tablas de multiplicar")
NumeroMultiplicando = int(input("Ingresa el numero que deseas multiplicar: "))
NumeroLimite = int(input("Ingresa HASTA que número deseas multiplicar el numero anterior: "))

def TablaDeMultiplicar():
    print(f"Tabla de Multiplicar del {NumeroMultiplicando} hasta el {NumeroLimite}:")
    print("_________________________")
    for i in range(1, NumeroLimite + 1):
        resultado = NumeroMultiplicando * i
        print(f"{NumeroMultiplicando} x {i} = {resultado}")
    print("_________________________")

TablaDeMultiplicar()