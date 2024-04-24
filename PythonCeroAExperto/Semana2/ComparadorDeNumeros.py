Numero1 = int(input("Ingresa el primer numero: "))
Numero2 = int(input("Ingresa el segundo numero: "))

#Identificar si son iguales
if Numero1 == Numero2:
    print("los numeros son iguales")
else:
    print("\nlos numeros No son iguales")




print("/-------------Cual numero es mayor------------/")
#Identificar cual de los dos numeros es el mayor
if Numero1 > Numero2:
    print("el numero mayor es: ", Numero1)
elif Numero2 < Numero1:
    print("\nel numero mayor es: ", Numero2)
else:
    print("\nlos numeros son iguales")

print("/-------------Identificacion numero PAR o IMPAR-------------/")
if Numero1 % 2 == 0:
    print("el numero ", Numero1, "es par")
else:
    print("el numero", Numero1, "es impar")

if Numero2 % 2 == 0:
    print("el numero ", Numero2, "es par")
else:
    print("el numero", Numero2, "es impar")


print("/----------------Clasificador de Triangulos-----------/")


lado1 = int(input("Ingresa el valor del primer lado del triangulo: "))
lado2 = int(input("Ingresa el valor del segundo lado del triangulo: "))
lado3 = int(input("Ingresa el valor del tercer lado del triangulo: "))

if lado1 == lado2 and lado1 == lado3:
    print("Es un triangulo EQUILATERO")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("es un triangulo ISOSCELES")
else:
    print("es un triangulo ESCALENO")

print("/------------Determinacion de EDAD--------------/")
#Determinar si una persona se puede jubilar

edad = int(input("Ingresa tu edad: "))

if edad <= 12:
    print("aun eres un niño, aún no te puedes jubilar")
elif edad > 12 and edad <= 18:
    print("eres un adolescente, aún no te puedes jubilar")
elif edad > 18 and edad <=30:
    print("eres un adulto joven, aún no te puedes jubilar")
elif edad > 30 and edad <= 60:
    print("eres un adulto pero, aún no te puedes jubilar")
elif edad > 60 and edad <= 100:
    print("eres un adulto y ya te puedes jubilar")
else:
    print("Tu edad no es valida")

print("/-------------Identificacion de Dias entre semana o fin de semana--------------/")
#Dia laboral
DiaHoy = input(str("escribe un dia de la semana: "))
EntreSemana = ["lunes", "martes", "miercoles", "jueves", "viernes"]
FinDeSemana = ["sabado", "domingo"]

if DiaHoy.lower() in EntreSemana:
    print(DiaHoy, "es un dia laboral")
elif DiaHoy.lower() in FinDeSemana:
    print(DiaHoy, "es parte del fin de semana")
else:
    print("Ingresa un dia válido")


      

