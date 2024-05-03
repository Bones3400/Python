import random

def adivinador_juego():
    numero_adivinar = random.randint(1, 100)
    intentos = 0

    print("Adivina Adivinador....")
    print("Un número del 1 al 100, será el ganador")

    while intentos < 10:
        intento = int(input("Ingresa un número para adivinar: "))

        if intento < 1 or intento > 100:
            print("Número no válido, debes ingresar un número del 1 al 100")
            continue
        intentos += 1

        if intento == numero_adivinar:
            print(f"Felicidades! Adivinaste el número en {intentos} intentos!")
            return

        elif intento < numero_adivinar:
            print("El número es mayor")
    
        else:
            print("El número es menor")

    print(f"Has perdido! el número era {numero_adivinar} :(")
    reintentar()

def reintentar():
        print("Deseas volver a jugar?")
        reintentar = input("SI/NO:  ")

        if reintentar.upper() == "SI":
            adivinador_juego()

        else:
            print("Gracias por jugar")
            return


adivinador_juego()
reintentar()
 
