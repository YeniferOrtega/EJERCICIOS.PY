# registro de sismos
class Ciudad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.sismos = []

class Sismo:
    def __init__(self, magnitud, profundidad):
        self.magnitud = magnitud
        self.profundidad = profundidad

ciudades = {}

def registrar_ciudad():
    nombre_ciudad = input("Ingrese el nombre de la ciudad: ")
    if nombre_ciudad in ciudades:
        print("La ciudad ya está registrada.")
    else:
        ciudades[nombre_ciudad] = Ciudad(nombre_ciudad)
        print("Ciudad registrada exitosamente.")

def registrar_sismo():
    nombre_ciudad = input("Ingrese el nombre de la ciudad donde ocurrió el sismo: ")
    if nombre_ciudad in ciudades:
        magnitud = float(input("Ingrese la magnitud del sismo: "))
        profundidad = float(input("Ingrese la profundidad del sismo: "))
        ciudades[nombre_ciudad].sismos.append(Sismo(magnitud, profundidad))
        print("Sismo registrado exitosamente.")
    else:
        print("La ciudad no está registrada.")

def buscar_sismos_por_ciudad():
    nombre_ciudad = input("Ingrese el nombre de la ciudad para buscar sismos: ")
    if nombre_ciudad in ciudades:
        if ciudades[nombre_ciudad].sismos:
            print(f"Sismos en {nombre_ciudad}:")
            for sismo in ciudades[nombre_ciudad].sismos:
                print(f"Magnitud: {sismo.magnitud}, Profundidad: {sismo.profundidad}")
        else:
            print("No se encontraron sismos en esta ciudad.")
    else:
        print("La ciudad no está registrada.")

while True:
    print("\nMenú:")
    print("1. Registrar Ciudad")
    print("2. Registrar Sismo")
    print("3. Buscar sismos por ciudad")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_ciudad()
    elif opcion == "2":
        registrar_sismo()
    elif opcion == "3":
        buscar_sismos_por_ciudad()
    elif opcion == "4":
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")


