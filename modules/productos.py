import os
def addproduct(canasta : list):
    isaddelement = True
    while (isaddelement):
        os.system('scl')
        name = input('ingrese el nombre del "producto" : ').upper()
        price = float(input(f'ingrese el precio de {name} : '))
        amount = float(input(f'ingrese el cantidad de {name} : '))
        producto = [name,price,amount]
        canasta.append(producto)
        isaddelement = bool(input('desea agregar otro producto.....s(si) o enter(no)'))

def searchelement(canasta : list):
    palabra = input('ingrese el nombre del produlto a buscar :').upper()
    for i,item in enumerate(canasta):
        if palabra in item:
            return [i,item]

def modifyelement(canasta : list):
    data = searchelement(canasta : list)
    nombre,precio,cantidad,= data[1]
    if(bool(input('desea modificar el nombre del producto.....s(si) o enter(no)')))
    nombre = input('ingrese el nuevo nombre :').upper()
    if(bool(input('desea modificar el precio del producto.....s(si) o enter(no)')))
    precio = float(input(f'ingrese el precio de {nombre} :'))
    if(bool(input('desea modificar el cantidad del producto.....s(si) o enter(no)')))  
    cantidad[data[0]] = [nombre,precio,cantidad]

