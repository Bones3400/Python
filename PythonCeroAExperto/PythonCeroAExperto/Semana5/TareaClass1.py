#Crear una Clase Circulo, con atributos como radio y definir un método para hallar el area.

class Circulo():
    def __init__(self, radio):
        self.radio = radio
      
    def area(self):
        Pi = 3.1415
        area = Pi * (self.radio**2)
        print(f"el area del circulo = {int(area)}m³") 

circulo = Circulo(5)
circulo.area()
