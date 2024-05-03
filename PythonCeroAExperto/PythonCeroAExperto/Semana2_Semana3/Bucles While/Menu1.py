while True:
    print("Bienvenido al gym People Fitness, que deseas mirar?")
    print("1. Ver deportes en equipo")
    print("2. Ver deportes en solitario")
    print("3. Ver deportes extremos")
    print("4. Salir")

    opcion = input("Por favor, ingresa el número de tu opción: ")

    if opcion == "1":
        print("Estos son todos los deportes en equipo que puedes realizar en nuestro gym")
        # 
    elif opcion == "2":
        print("Estos son todos los deportes en solitario que puedes realizar en nuestro gym!")
        # Aquí iría la lógica para tomar el pedido
    elif opcion == "3":
        print("Estos son todos los deportes extremos que puedes realizar en nuestro gym")
        # Aquí iría la lógica para mostrar el carrito
    elif opcion == "4":
        print("¡Gracias por visitar nuestro restaurante! ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")