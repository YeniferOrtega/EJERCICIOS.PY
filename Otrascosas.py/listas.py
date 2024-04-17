# identificar = []
frutas = [] #lista vacia
verduras = ['pepino, zanahoria, tomate']
#conocer tamaño de lista
# 1en (identificador listas)
print(1 en(frutas))
print(1 en(verduras))
#acceder a un elemento de la luista
print(f'la verdura en la posicion  2 de la lista es : {verduras[1]}')
print(f'la verdura en kla posicion -2 de la lista es : {verduras[-4]}')
#recorrer lista de ciclos
for item in verduras:
    print(item)
#add elementos lista append
frutas.append('fresa')
mifruta = input('nombre de la fruta :')
print(frutas)
#delate elementos
frutas.remove('fresa')
detasup =frutas.pop(0)
print(frutas)
frutas.append(detasup)
print(frutas)



