import os
from tabulate import tabulate

def AddBook(repo : list):
    isAddBook = True
    categoria = "1. Bases de datos\n2. Fundamentos\n3. Programacion\n4. Frontend\n5. Backend\n6. Terminar"
    while (isAddBook):
        os.system('cls')
        print(categoria)
        op = int(input(":) "))
        if (op <= len(repo)):
            data = repo[op-1]
            codBook = str(len(data[1])+1).zfill(4)
            isb = input('Ingrese el ISB : ')
            nombre = input('Ingrese el Nombre del Libro : ')
            level = int(input('Seleccione nivel del libro (1. Basico 2. Intermedio 3. Avanzado)'))
            while (level > 3):
                print('El nivel seleccionado es invalido...Verifique las opciones')
                level = int(input('Seleccione nivel del libro (1. Basico 2. Intermedio 3. Avanzado)'))
            nameLevel = ''
            match level:
                case 1:
                    nameLevel = 'Basico'
                case 2:
                    nameLevel = 'Intermedio'
                case 3:
                    nameLevel = 'Avanzado'
                case _:
                    pass
            autor = input('Ingrese el nombre del autor : ')
            eje = input('Ingrese el eje tematico del libro : ')
            data[1].append([codBook,isb,nombre,nameLevel,autor,eje,True])
            repo[op-1] = data
            print(repo)
            os.system('pause')
            isAddBook = bool(input('Desea ingresar otro libro S(Si) o Enter(No)'))
        elif (op == 6):
            isAddBook = False
        else:
            print('La opcion que ingreso no es valida....')
            isAddBook = bool(input('Desea ingresar otro libro S(Si) o Enter(No)'))

def SearchBook(repo : list):
    categoria = "1. Bases de datos 2. Fundamentos 3. Programacion 4. Frontend 5. Backend"
    print(f'Seleccione una categoria : {categoria}')
    op = int(input(":) "))
    while (op > 5):
        os.system('cls')
        print('El valor ingresado es invalido')
        print(f'Seleccione una categoria : {categoria}')
        op = int(input(":) "))
    data = repo[op-1]
    return data

def MovBook(repo : list, estado : bool):
    os.system('cls')
    print(tabulate(repo[1],headers = ['Cod Interno','ISB Libro','Nombre del Libro','Nivel del libro','Autor libro','Eje Tematico','Estado']))
    cod = input('Ingrese codigo interno a prestar :').zfill(4)
    for i,item in enumerate(repo[1]):
        if cod in item:
            item[6]=estado
            break