def NumeroPrimo(numero):
    if numero <= 1:
        return False
    return all(numero % i for i in range(2, numero)) #si el residuo de x numero llega a ser divisible por un numero en el rango, este número NO será primo


numero = int(input("Ingresa un número: "))
if NumeroPrimo(numero):
    print(numero, "es primo")
else:
    print(numero, "NO es primo")