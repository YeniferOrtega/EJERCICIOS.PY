import os
def Calculadora(valoraA : int, valorB : int, op : str):
    resultado = 0
    match op:
        case '+' :
            return valoraA + valorB
        case '-' :
            return valoraA + valorB
        case '*' :
            return valoraA + valorB
        case '/' :
            return valoraA + valorB
        case _:
            print('ops...operaciones no existen')
            return -1
    os.system('pause')

    if __name__== '__main__':
        opcion = 1
        titulo = ""
        ************************
        * OPERACIONES MATEMATICAS *
        ************************
        """""" 

        while (opcion < 5):
            os.system('cls') 
            print(titulo)
            menu = "\t1. suma \n\t2. resta \n\t3. multiplicacion \n\t4. division \n\t5. salir"
            print(menu) 
            opcion = int(input('\t:)_'))
            match opcion:
                case 1:
                    print(f'\tla suma de los sumas es = {Calculadora(2,3,'+')}')
                case 2:
                    print(f'\la suma delos numeros es = {Calculadora(2,3), '+'}')
                case 3:
                    print(f'\tla suma de los sumas es = {Calculadora(2,3,'+')}')
                case 4:
                    print(f'\la suma delos numeros es = {Calculadora(2,3), '+'}')
                case 5:
                    print('\tvuelve pronto')
                case _:
                    print('ops...la opcion no es validad')
                    opcion = 1
            os.system('pause')
            