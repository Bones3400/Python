# Bucle principal
while True:
    print("Bienvenido al restaurante XYZ")
    print("1. Ver menú")
    print("2. Realizar pedido")
    print("3. Ver carrito")
    print("4. Salir")

    opcion = input("Por favor, ingresa el número de tu opción: ")

    if opcion == "1":
        print("Aquí está el menú:")
        # Aquí iría la lógica para mostrar el menú
    elif opcion == "2":
        print("¡Vamos a tomar tu pedido!")
        # Aquí iría la lógica para tomar el pedido
    elif opcion == "3":
        print("Este es tu carrito de compras:")
        # Aquí iría la lógica para mostrar el carrito
    elif opcion == "4":
        print("¡Gracias por visitar nuestro restaurante! ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")