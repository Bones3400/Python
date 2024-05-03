print("/------------------EJEMPLOS--------------------/")
# definir una lista con la edad de 5 amigos
lista_edades = [24,30,27,26,25]

#Agregar la edad de un nuevo amigo
lista_edades.append(30)

#consultar cuantas personas tienen 30 años

print("\npersonas del grupo con 30 años: ",lista_edades.count(30))

#sumar la edad de todas las personas

print("\nla suma de las edades de todos los miembros de la lista es de: ",sum(lista_edades))


#EJERCICIOS
print("\n/-------------------EJERCICIOS--------------------/")
#1 Definir una lista de valores de materiales escolares 
     #1.2 agregar 3 elementos a la lista
     #1.3 sumar el total de la compra
     #1.4 agregar un ultimo elemento de 500 pesos
     #1.5 volver a sumar todo

#DESARROLLO
#1.1 | 5000 por caja de lapiceros, 12000 por cuaderno, 7000 por reglas
ListaEscolar = [5000, 12000, 7000]

#1.2 |  2000 por lapicero, 1000 por borrador y 2500 por sacapuntas
ListaEscolar.append(2000)
ListaEscolar.append(1000)
ListaEscolar.append(2500)

#1.3
print("\nla suma total de todos los materiales es de: ",sum(ListaEscolar))

#1.4 | 500 por sticker
ListaEscolar.append(500)

#1.5 volver a sumar todo

print("\nla suma de todos los materiales, incluyendo los agregados es de: ",sum(ListaEscolar) )


