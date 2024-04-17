import os 

def registro_de_alumnos():
    peso_normal = 0
    obesidad_grado_1 = 0
    obesidad_grado_2 = 0
    obesidad_grado_3 = 0
    sobrepeso = 0

    n = int(input("Ingrese el número de estudiantes: "))

    for i in range(n):
        print(f"\nEstudiante {i+1}:")
        nombre = input('Ingrese el nombre del estudiante: ')
        edad = float(input('Ingrese la edad del estudiante en años: '))
        peso = float(input('Ingrese el peso del estudiante en kg: '))
        altura = float(input('Ingrese la altura del estudiante en metros: '))

        imc = peso / (altura ** 2)

        if imc < 18.5:
            peso_normal += 1
        elif 18.5 <= imc <= 30:
            pass  # peso normal
        elif 30 <= imc <= 35:
            sobrepeso += 1
        elif 35 <= imc <= 40:
            obesidad_grado_1 += 1
        elif 40 <= imc <= 50:
            obesidad_grado_2 += 1
        else:
            obesidad_grado_3 += 1

    print("\nReporte de salud de la comunidad estudiantil:")
    print("a. Alumnos en peso normal:", peso_normal)
    print("b. Alumnos en obesidad grado 1:", obesidad_grado_1)
    print("c. Alumnos en obesidad grado 2:", obesidad_grado_2)
    print("d. Alumnos en obesidad grado 3:", obesidad_grado_3)
    print("e. Alumnos en sobrepeso:", sobrepeso)

# Llamamos a la función para probarla
registro_de_alumnos()

        

