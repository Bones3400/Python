"""
Ejercicios practicos

    - Pide al usuario que ingrese su edad y calcula el año de nacimiento,
      luego muéstralo en pantalla. (el año actual es 2024)

    - Solicita al usuario que ingrese su edad y verifica si es elegible para
      conducir un auto en su país (generalmente a partir de los 16 años).
      Imprime un mensaje que indique si es elegible o no.

    - Del ejercicio anterior agregar una validación si la persona no esta
      habilitada para conducir si es mayor de edad 85 años
    
"""

def calculo_año():
    AñoActual = 2024
    Edad = int(input("Ingrese su edad: "))
    AñoNacimiento = AñoActual - Edad
    print(f"su fecha de nacimiento es: {AñoNacimiento}")

#calculo_año()



def calcular_licencia():
    Edad = int(input("Ingrese su edad: "))
    EdadMinima = 16
    EdadMaxima = 85
    if Edad >= EdadMinima and Edad < EdadMaxima:
        print("Ud es elegible para conducir un vehiculo")
    else:
        print("Ud ya no es elegible para conducir un vehiculo")

#calcular_licencia()



