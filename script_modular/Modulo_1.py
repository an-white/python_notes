# si se desean definir funciones llamables desde otro programa se establece la condicion
# if aqui def: y dentro de ella se colocan todas las funciones que se desean definir
# en el modulo establecido, todo esto debe estar contenido en la misma carpeta 

def modulo_lunar():
    print("¡Hola desde Modulo_1.py!")
    print('Ejecutando trayectoria definida')
    print("¡Desacoplando del cohete principal!")
    print("¡Adiós desde Modulo_1.py!")


if __name__ == "__main__":
    modulo_lunar()
