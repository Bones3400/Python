
def facturacion():
    print(f"Bienvenido al SmoothGym, deseas conocer tu facturación mensual?")
    Horas = int(input("Ingresa cuantas horas estuviste en el gym este mes: "))
    if Horas >= 0 and Horas <= 14:
        print(f"Eres categoría Bronce, debes pagar ${Horas * 5000}, recuerda que la categoría Bronce paga 5000 por hora")
    elif Horas >= 15 and Horas <= 29:
        print(f"Eres categoría Plata, debes pagar ${Horas * 3500}, recuerda que la categoría Plata paga 3500 por hora")
    elif Horas >=30:
        print(f"Felicidades! Eres categoría Oro, así que debes pagar ${Horas*2000} este mes")
    else:
        print(f"Por favor escribe un NUMERO válido")
        facturacion()

facturacion()