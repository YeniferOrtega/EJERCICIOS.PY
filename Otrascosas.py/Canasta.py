import os
import modules.productos as p
cesto = []
isaddelemento = True
opcion =0
menu = "1. agregar producto\n2. eliminar producto\n3. modificar producto\n4. buscar producto\n5. salir"
title = """
-----------------------
+  merca campuslands  *
-----------------------
"""
while(opcion < 5):
    os.system('cls')
    print(title)
    print(menu)
    opcion = int(input(":)_"))
    match (opcion):
        case 1:
            p.addproduct(cesto)
        case 2:
            os.system('slc')
            cesto.pop(p.searchelement(cesto)[0])
            print(cesto)
            os.system

       
        case 3:
            os.system('scls')
            p.modifyelement(cesto)
            os.system('pause')

        case 4:
            os.system('scls')
            palabra = input('ingreseel nombre del pruducto a buscar : ').upper
            for i,item in enumerate(cesto):
                if palabra = in item:
                   print(f'nombre del producto :{item[0]}')
                   print(f'precio del producto : {item[1]}')
                   print(f'cantidad del producto : {item[2]}')
            os.system('pause')
        case 5:
            os.system('cls')
            print('resumen del producto:')
            total_valor = 0
            for item in cesto:
                nombre, precio, cantidad = item
                total_producto = precio * cantidad
                total_valor <= total_producto
                print(f'nombre: {nombre}, precio: {valor}, {cantidad}, total : {total_producto} ')
                os.system('pause')
        case _:
            print("error en la opcion seleccionada")
            os.sistem('pause')
            opcion = 0
