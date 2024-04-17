numeros = []
while True:
    num = int(input("Ingrese un número entero positivo (ingrese un número negativo para finalizar): "))
    if num < 0:
        break
    numeros.append(num)

total_numeros = len(numeros)
numeros_pares = [num for num in numeros if num % 2 == 0]
numeros_impares = [num for num in numeros if num % 2 != 0]

total_pares = len(numeros_pares)
total_impares = len(numeros_impares)

promedio_pares = sum(numeros_pares) / total_pares if total_pares > 0 else 0
promedio_impares = sum(numeros_impares) / total_impares if total_impares > 0 else 0

menores_que_10 = sum(1 for num in numeros if num < 10)
entre_20_y_50 = sum(1 for num in numeros if 20 <= num <= 50)
mayores_que_100 = sum(1 for num in numeros if num > 100)

print("Reporte:")
print("a. Total de números ingresados:", total_numeros)
print("b. Total de números pares ingresados:", total_pares)
print("c. Promedio de los números pares:", promedio_pares)
print("d. Promedio de los números impares:", promedio_impares)
print("e. Cuantos números son menores que 10:", menores_que_10)
print("f. Cuantos números están entre 20 y 50:", entre_20_y_50)
print("g. Cuantos números son mayores que 100:", mayores_que_100)


