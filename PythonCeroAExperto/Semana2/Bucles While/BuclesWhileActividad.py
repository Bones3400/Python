#Crear un programa en Python que presente al usuario opciones de seleccion:"""
#Para visualizar los numeros del 1 al 100"""
#Para visualizar los numeros impares"""
#Para visualizar los numeros pares"""
#Para visualizar una tabla de multiplicar"""

while True:
    print("Bienvenido al contador de números9000, que deseas hacer?")
    print("1. Visualizar numeros del 1 al 100")
    print("2. Visualizar numeros pares")
    print("3. Visualizar numeros impares")
    print("4. visualizar tabla de multiplicar")
    print("0. Salir")

    opcion = input("Por favor, ingresa el número de tu opción: ")

    if opcion == "1":
        print("Aqui están los numeros del 1 al 100:")
        def contador():
            for i in range(1,101,1):
                print(f"{i}")
            
        contador()


    elif opcion == "2":
        print("Establece un limite para ver los numeros pares: ")
        NumberParLimit = int(input("Establece el límite acá: "))
        def numerospares():
            for i in range(1,NumberParLimit):
                if i % 2 == 0:
                    print(f"{i} es par")
                else:
                    print("")

        numerospares()
    elif opcion == "3":
        print("Establece un limite para ver los numeros impares: ")
        NumberImparLimit = int(input("Establece el límite acá: "))
        def numerosimpares():
            for i in range(1,NumberImparLimit):
                if i % 2 == 0:
                    print("")
                else:
                    print(f"{i} es Impar")

        numerosimpares()

    elif opcion == "4":
        print("Visualizar tablas de multiplicar")
        NumeroMultiplicando = int(input("Ingresa el numero que deseas multiplicar: "))
        NumeroLimite = int(input("Ingresa HASTA que número deseas multiplicar el numero anterior: "))
        def TablaDeMultiplicar():
            for i in range(1, NumeroLimite + 1):
             resultado = NumeroMultiplicando * i
             print(f"{NumeroMultiplicando} x {i} = {resultado}")

        TablaDeMultiplicar()

    elif opcion == "0":
        print("Gracias por usar el programa")

        break
    
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")