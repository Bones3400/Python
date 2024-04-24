def ProgramaMultiFunciones():
    
    def main():
        print("Bienvenido a mi programa multifunciones\n")
        print("Que te gustaría hacer?")
        print("1. Visualizar números del 1 hasta el número que tu quieras")
        print("2. Determinador de número par/impar\n")
        respuesta = int(input("Ingresa tu opción: "))
        if respuesta == 1:
            def visualizador():
                n = int(input("Ingresa hasta que número deseas visualizar: "))
                if n <= 0:
                    for i in range(1, n, -1):
                        print(i)
                else:
                    for i in range(1, n, +1):
                        print(i)
            
            visualizador()
        else:
            def determinadorParImpar():
                n = int(input("Ingresa el número que deseas conocer si es par o impar: "))
                if n % 2 == 0:
                    print(f"El número {n} es PAR")
                else:
                    print(f"El número {n} es IMPAR")

            determinadorParImpar()

    main()
    def Repetidor():
        print("Desea seguir en el programa? ")
        r = input("si/no: ")
        if r.lower() == "si":
            ProgramaMultiFunciones()
        else:
            print("Gracias por usar mi programa")
    Repetidor()
    
ProgramaMultiFunciones()

#Made By Smoothy


        



                
              


    
    
        

