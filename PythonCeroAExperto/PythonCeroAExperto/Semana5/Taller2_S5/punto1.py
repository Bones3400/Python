import time

preguntas = [
    {
        "pregunta": "Cuanto es 2+2 ", 
        "respuestas": ["a. 4", "b. 22", "c. 11", "d. 5"],
        "respuesta": "a"
    },
    {
        "pregunta": "Cuanto es 5+5 ", 
        "respuestas": ["a. 56", "b. 7", "c. 11", "d. 10"],
        "respuesta": "d"
    },
    {
        "pregunta": "Cuanto es 20*20 ", 
        "respuestas": ["a. 500", "b.200", "c. 400", "d. 2000"],
        "respuesta": "c"
    },
    {
        "pregunta": "Cuanto es 175-85 ", 
        "respuestas": ["a. 85", "b. 65", "c. 95", "d. 90"],
        "respuesta": "d"
    },
    {
        "pregunta": "Cuanto es 150 + 125 ", 
        "respuestas": ["a. 225", "b. 275", "c. 325", "d. 300"],
        "respuesta": "b"
    }
]        

tiempos_respuesta = []

correctas = 0
total = 0

for pregunta in preguntas:
    print(pregunta['pregunta'])
    for respuesta in pregunta['respuestas']:
        print(respuesta)
    inicio_tiempo = time.time()
    respuesta_usuario = input('Elige la respuesta correcta (a, b, c, d): ')
    while respuesta_usuario not in ['a', 'b', 'c', 'd']:
        print('Opción no está en la lista. Inténtalo de nuevo.')
        respuesta_usuario = input('Elige la respuesta correcta (a, b, c, d): ')
    tiempo_respuesta = time.time() - inicio_tiempo
    if tiempo_respuesta <= 10:
        total += 1
        if respuesta_usuario == pregunta['respuesta']:
            print('¡Muy bien! Te tomó', round(tiempo_respuesta, 2), 'segundos en dar la respuesta.')
            correctas += 1
        else:
            print('Respuesta incorrecta.')
    else:
        print('Tiempo excedido.')
    print()

porcentaje_correctas = (correctas / total) * 100

if porcentaje_correctas <= 50:
    print('Puedes hacerlo mejor. ¡Ánimo!')
elif porcentaje_correctas <= 70:
    print('¡Muy buen trabajo!')
else:
    print('¡Eres un genio!')

print('Porcentaje de preguntas correctas:', round(porcentaje_correctas, 2), '%')