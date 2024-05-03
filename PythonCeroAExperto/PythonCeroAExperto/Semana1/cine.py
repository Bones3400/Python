#Definición de Pi y fórmulas

pi = 3.1416
VolumenCilindro = pi * (4**2) * 15
VolumenRectangular = 12*8*10
VolumenCono = 1/3 * pi * (6**2) * 12

#Comparar, identificar y mencionar la mejor opción

if VolumenCilindro > VolumenRectangular and VolumenCilindro > VolumenCono:
    print("La forma cilindrica es la mejor ya que tiene un volumen de ", (VolumenCilindro),"cm3")
elif VolumenRectangular > VolumenCilindro and VolumenRectangular > VolumenCono:
    print("La forma rectangular es la mejor ya que tiene un volumen de ", (VolumenRectangular),"cm3")
else:
    print("La forma de cono es la mejor ya que tiene un volumen de ", (VolumenCono), "cm3")
