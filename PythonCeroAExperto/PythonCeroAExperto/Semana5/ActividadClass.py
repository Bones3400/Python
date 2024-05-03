class Persona():
    def __init__(self, nombre, apellido, peso, estatura, ):
        self.nombre = nombre
        self.apellido = apellido
        self.peso = int(peso)
        self.estatura = float(estatura)
        self.imc = self.peso / (self.estatura**2)

    def caminar(self):
        print('estoy caminando')


    def saludar(self):
            print(f"hola, mi nombre es: {self.nombre}{self.apellido}, peso {self.peso}kg y mido {self.estatura}m")

    def hallarimc(self):
         print(f"hola, mi nombre es: {self.nombre} {self.apellido}, peso {self.peso}kg y mido {self.estatura}m, por lo cual mi IMC = {self.imc}")
persona = Persona('Santiago', "Aceros", "72", "1.91")

persona.hallarimc()



# Actividad, modificar la clase persona, para tener un metodo que nos ayude a calcular el IMC, para esto necesitamos agregar nuevos atributos
