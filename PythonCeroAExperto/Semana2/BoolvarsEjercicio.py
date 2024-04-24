sentencia_1 = True
sentencia_2 = False

print("sentencia 1 = ", not sentencia_1) #Imprime lo opuesto al valor de sentencia_1
print("sentencia 1 y 2 = ",  not sentencia_1 and  sentencia_2) #imprime lo opuesto a el valor de sentencia_1 e imprime sentencia_2 con su valor original
print("sentencia 1 o sentencia 2 = ", not sentencia_1 or not sentencia_2) #arroja true si almenos una variable es positiva, solo arroja false si ambas son negativas o viceversa
