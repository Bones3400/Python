class GestorArchivos:
    def __init__(self, ruta_predeterminada):
        self.ruta_predeterminada = ruta_predeterminada

    def abrir_archivo(self, ruta=None, modo='r'):
        if ruta is None:
            ruta = self.ruta_predeterminada
        try:
            archivo = open(ruta, modo)
            return archivo
        except FileNotFoundError:
            print("El archivo no fue encontrado.")
            return None

    def escribir_archivo(self, contenido, ruta=None):
        if ruta is None:
            ruta = self.ruta_predeterminada
        try:
            with open(ruta, 'w') as archivo:
                archivo.write(contenido)
                print("Archivo escrito exitosamente.")
        except FileNotFoundError:
            print("El archivo no fue encontrado.")
    
    
    def escribir_alfinal_archivo(self, contenido, ruta=None):
        if ruta is None:
            ruta = self.ruta_predeterminada
        try:
            with open(ruta, 'a') as archivo:
                archivo.write(contenido)
                print("Archivo escrito exitosamente.")
        except FileNotFoundError:
            print("El archivo no fue encontrado.")

    def actualizar_ruta(self, nueva_ruta):
        self.ruta_predeterminada = nueva_ruta
        print("Ruta predeterminada actualizada.")

# Ejemplo de uso
path = 'C:\\Users\\DrSmooth\\Downloads\\erchivo\\Smooth.txt'
gestor = GestorArchivos(path)
archivo = gestor.abrir_archivo()
if archivo:
    contenido = archivo.read()
    print("Contenido del archivo:", contenido)
    archivo.close()

new_path = 'C:\\Users\\DrSmooth\\Downloads\\erchivo\\Smooth.txt'

gestor.actualizar_ruta(new_path)
gestor.escribir_archivo("Hola, mundo")
gestor.escribir_archivo("Hola, mundo 123")

gestor.escribir_alfinal_archivo("\nhi")
gestor.escribir_alfinal_archivo("\nhello")
gestor.escribir_alfinal_archivo("\naloha")
gestor.escribir_alfinal_archivo("\nhola")
gestor.escribir_alfinal_archivo("\nchao")
gestor.escribir_archivo("Smoothy was here")