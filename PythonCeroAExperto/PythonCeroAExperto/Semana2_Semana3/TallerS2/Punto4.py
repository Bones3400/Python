"Explica con tus palabras que significan las siguientes terminos en programacion:"


"""
    Respuesta:
    - Bucle: Una acción que repite x numero de veces un bloque de código
    - For: Es un tipo de bucle que permite iterar en ciertos grupos que se encuentren dentro del bucle como: listas, diccionarios etc
    - While: Ejecuta un Blucle mientras una condición especifica sea verdadera 
"""



"TABLAS DE MULTIPLICAR"

"""
    Haciendo uso de los bucles vistos en clase crea un programa
    que le solicite al usurario ingresar un numer entero y muestra
    las tablas de multiplicar de dicho numero.
"""
def tabla_multiplicar():
    numero = int(input("Ingresa un número: "))
    for i in range(1,11,1):
        print(f"{numero} x {i} = {numero * i}")
#tabla_multiplicar()




"ESCALA - MULTIPLICACION Y DIVISION"

"""
    Haciendo uso de los bucles vistos en clase crea un programa que
    le solicite al usurario ingresar un numer entero y muestra
    en pantalla una “escala”
    
"""
#multiplicacion
def escala():
    numero = int(input("Ingresa un numero: "))
    for i in range(2,10,1):
        print(f"{numero} x {i} = {numero * i}")
        numero *= i

        #division
    for i in range(9,1,-1):
        print(f"{int(numero)} / {i} = {int(numero)/ i}")
        numero /= i

    respuesta = input("Quieres continuar? (si/no) ")
    if respuesta.lower() == "si":
        escala()
    else:
        print("Gracias por usar el programa!")

escala()


        