# Hallar el area de un cuadrado  de lado L = 21 usando variables 

lado = 21 
area = lado*lado
print("el area del cuadrado es de ", area)

#Hallar el volumen de una esfera de radio = 100
pi = 3.1416
radio = 100
volumen = 4/3*(pi * (radio**3)) 
print("el volumen de la esfera es de ", volumen)




#Ejercicios
print("/---------------------------EJERCICIOS-----------------------/")
#1 Hallar el volumen de un cubo de lado 15
#2 Hallar el total de compras de un mercado que tienen los siguientes items: Arroz = 4000 ;  Aceite = 13000 ;  huevos = 15000 ;  pan = 10000 ; leche = 45000
#3 Hallar el area de un triangulo de base 10 y altura 30 

#Desarrollo 1

LadoCubo = 15
VolumenCubo = LadoCubo**3
print("el volumen del cubo es igual a: ", VolumenCubo)

#Desarrollo 2
Arroz = 4000
Aceite = 13000
Huevos = 15000
Pan = 10000
Leche = 45000
TotalaPagar = Arroz+Aceite+Huevos+Pan+Leche
print("para comprar una unidad de cada articulo debes pagar: ", TotalaPagar, "en total")

#Desarrollo 3 

BaseTriangulo = 10
AlturaTriangulo = 30

AreaTriangulo = (BaseTriangulo*AlturaTriangulo)/2
print("El area del triangulo es de: ", AreaTriangulo)