class Producto:
    def __init__(self, codigo, nombre, valor_compra, valor_venta, stock_minimo, stock_maximo, proveedor):
        self.codigo = codigo
        self.nombre = nombre
        self.valor_compra = valor_compra
        self.valor_venta = valor_venta
        self.stock_actual = 0
        self.stock_minimo = stock_minimo
        self.stock_maximo = stock_maximo
        self.proveedor = proveedor

def registrar_producto(productos):
    codigo = input("Ingrese el código del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    valor_compra = float(input("Ingrese el valor de compra del producto: "))
    valor_venta = float(input("Ingrese el valor de venta del producto: "))
    stock_minimo = int(input("Ingrese el stock mínimo permitido: "))
    stock_maximo = int(input("Ingrese el stock máximo permitido: "))
    proveedor = input("Ingrese el nombre del proveedor del producto: ")

    producto = Producto(codigo, nombre, valor_compra, valor_venta, stock_minimo, stock_maximo, proveedor)
    productos.append(producto)

def visualizar_productos(productos):
    print("Lista de productos:")
    for producto in productos:
        print("Código:", producto.codigo)
        print("Nombre:", producto.nombre)
        print("Valor de compra:", producto.valor_compra)
        print("Valor de venta:", producto.valor_venta)
        print("Stock actual:", producto.stock_actual)
        print("Stock mínimo permitido:", producto.stock_minimo)
        print("Stock máximo permitido:", producto.stock_maximo)
        print("Proveedor:", producto.proveedor)
        print()

def actualizar_stock(productos):
    codigo = input("Ingrese el código del producto: ")
    cantidad = int(input("Ingrese la cantidad a agregar o restar al stock (use negativo para restar): "))
    for producto in productos:
        if producto.codigo == codigo:
            producto.stock_actual += cantidad
            print("Stock actualizado con éxito.")
            return
    print("Producto no encontrado.")

def informe_productos_criticos(productos):
    print("Productos con stock por debajo del mínimo:")
    for producto in productos:
        if producto.stock_actual < producto.stock_minimo:
            print("Código:", producto.codigo)
            print("Nombre:", producto.nombre)
            print("Stock actual:", producto.stock_actual)
            print("Stock mínimo permitido:", producto.stock_minimo)
            print()

def calcular_ganancia_potencial(productos):
    ganancia_total = 0
    for producto in productos:
        ganancia_total += (producto.valor_venta - producto.valor_compra) * producto.stock_actual
    print("La ganancia potencial total es:", ganancia_total)

# Función principal
def main():
    productos = []

    while True:
        print("\nBienvenido al sistema de gestión de inventarios")
        print("1. Registrar Producto")
        print("2. Visualizar Productos")
        print("3. Actualizar Stock")
        print("4. Informe de Productos Críticos")
        print("5. Cálculo de Ganancia Potencial")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_producto(productos)
        elif opcion == "2":
            visualizar_productos(productos)
        elif opcion == "3":
            actualizar_stock(productos)
        elif opcion == "4":
            informe_productos_criticos(productos)
        elif opcion == "5":
            calcular_ganancia_potencial(productos)
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()


