my_diccionario = {"key": "value"}

#diccionario del idioma ingles
my_diccionario = {
    "key": "llave",
    "hello": "hola",
    "cat": "gato"
    }
print(my_diccionario.get("cat"))

print("este es el valor completo del diccionario: ", my_diccionario)
print("este es el valor de todas las llaves: ", my_diccionario.keys())
print("voy a agregar un valor al diccionario: ")
my_diccionario["dog"] = "perro"
print("\neste es el valor completo del diccionario: ", my_diccionario)
print("\neste es el valor de todos los items: ", my_diccionario.values())

for key, value in my_diccionario.items():
    print(key, value)


persona = {
    "nombre": "yurley",
    "apellido": "sanchez",
    "edad": "30",
}
# Lista de personas
persona_list = [
    {
        "nombre": "yurley",
        "apellido": "sanchez",
        "edad": "30",
    },
    {
        "nombre": "estefano",
        "apellido": "ramirez",
        "edad": "24",
    },
    {
        "nombre": "enrique",
        "apellido": "martinez",
        "edad": "32",
    }
]
print(persona_list)

