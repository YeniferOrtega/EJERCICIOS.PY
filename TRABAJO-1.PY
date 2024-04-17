# Suma de tres numeros enteros
num1 = int(input("Ingrese el primer número entero positivo: "))
num2 = int(input("Ingrese el segundo número entero positivo: "))
num3 = int(input("Ingrese el tercer número entero positivo: "))

# Verificar si los números son positivos
if num1 <= 0 or num2 <= 0 or num3 <= 0:
    print("Por favor, ingrese números enteros positivos.")
else:
    # Calcular la suma de los tres números
    suma = num1 + num2 + num3
    
    # Imprimir el resultado
    print("La suma de los tres números enteros positivos es:", suma)
