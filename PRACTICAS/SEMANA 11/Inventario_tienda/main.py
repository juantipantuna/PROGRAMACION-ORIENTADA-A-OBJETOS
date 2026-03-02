from inventario import Inventario
from producto import Producto


def menu():
    print("\n" + "=" * 40)
    print("   SISTEMA DE INVENTARIO")
    print("=" * 40)
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto")
    print("5. Mostrar todos")
    print("6. Guardar")
    print("7. Cargar")
    print("8. Salir")
    print("=" * 40)
    return input("Opción (1-8): ")


def main():
    inventario = Inventario()
    inventario.cargar_archivo()

    while True:
        opcion = menu()

        if opcion == "1":
            print("\n--- NUEVO PRODUCTO ---")
            id_prod = input("ID: ")
            nombre = input("Nombre: ")
            try:
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: $"))
                producto = Producto(id_prod, nombre, cantidad, precio)
                inventario.agregar_producto(producto)
            except ValueError:
                print("Error: Cantidad y precio deben ser números")

        elif opcion == "2":
            id_prod = input("ID a eliminar: ")
            inventario.eliminar_producto(id_prod)

        elif opcion == "3":
            id_prod = input("ID a actualizar: ")
            print("(Enter para mantener)")
            cant = input("Nueva cantidad: ")
            prec = input("Nuevo precio: $")

            try:
                cant = int(cant) if cant else None
                prec = float(prec) if prec else None
                inventario.actualizar_producto(id_prod, cant, prec)
            except ValueError:
                print("Error: Ingrese números válidos")

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)
            if resultados:
                for prod in resultados:
                    print(prod)
            else:
                print("No se encontraron productos")

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            inventario.guardar_archivo()

        elif opcion == "7":
            inventario.cargar_archivo()

        elif opcion == "8":
            print("Guardando...")
            inventario.guardar_archivo()
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()