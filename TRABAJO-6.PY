class Dependencia:
    def _init_(self, nombre):
        self.nombre = nombre
        self.consumo_electricidad = 0
        self.consumo_dispositivos = 0
    
    def agregar_consumo(self, electricidad, dispositivos):
        self.consumo_electricidad += electricidad
        self.consumo_dispositivos += dispositivos
    
    def calcular_emisiones_totales(self, factor_emision_electricidad):
        emisiones_electricidad = self.consumo_electricidad * factor_emision_electricidad
        emisiones_totales = emisiones_electricidad + self.consumo_dispositivos
        return emisiones_totales

dependencias = []

def registrar_dependencia():
    nombre = input("Nombre de la dependencia: ")
    dependencias.append(Dependencia(nombre))
    print("Dependencia registrada.")

def registrar_consumo_dependencia():
    nombre = input("Nombre de la dependencia: ")
    for dependencia in dependencias:
        if dependencia.nombre == nombre:
            electricidad = float(input("Consumo de electricidad (kWh): "))
            dispositivos = float(input("Consumo de dispositivos (kWh): "))
            dependencia.agregar_consumo(electricidad, dispositivos)
            print("Consumo registrado.")
            return
    print("Dependencia no encontrada.")

def ver_CO2_producido(factor_emision_electricidad):
    for dependencia in dependencias:
        print("Dependencia:", dependencia.nombre)
        print("CO2 producido:", dependencia.calcular_emisiones_totales(factor_emision_electricidad))
        print()

def dependencia_mayor_CO2(factor_emision_electricidad):
    if dependencias:
        max_emisiones = max(dependencias, key=lambda x: x.calcular_emisiones_totales(factor_emision_electricidad))
        print("La dependencia que produce mayor CO2 es:", max_emisiones.nombre)
    else:
        print("No hay dependencias registradas.")

factor_emision_electricidad = 0.5

while True:
    print("\nMenú:")
    print("1. Registrar Dependencia")
    print("2. Registrar Consumo")
    print("3. Ver CO2 Producido")
    print("4. Dependencia Mayor CO2")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        registrar_dependencia()
    elif opcion == "2":
        registrar_consumo_dependencia()
    elif opcion == "3":
        ver_CO2_producido(factor_emision_electricidad)
    elif opcion == "4":
        dependencia_mayor_CO2(factor_emision_electricidad)
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")