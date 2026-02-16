"""
Interfaz de consola para el sistema de gestión de inventarios.
"""
from producto import Producto
from inventario import Inventario

def mostrar_menu():
    """Muestra el menú de opciones al usuario."""
    print("\n=== SISTEMA DE GESTIÓN DE INVENTARIOS ===")
    print("1. Añadir nuevo producto")
    print("2. Eliminar producto por ID")
    print("3. Actualizar producto (cantidad/precio)")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")
    print("=========================================")

def obtener_entero(mensaje):
    """Solicita un número entero al usuario con validación."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: Debes ingresar un número entero válido.")

def obtener_flotante(mensaje):
    """Solicita un número decimal al usuario con validación."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: Debes ingresar un número válido.")

def main():
    """Función principal del programa."""
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-6): ")

        if opcion == "1":
            # Añadir producto
            print("\n--- AÑADIR NUEVO PRODUCTO ---")
            id_producto = input("ID del producto: ")
            # Verificar si el ID ya existe
            if any(p.id == id_producto for p in inventario._productos):
                print(f"Error: El ID '{id_producto}' ya está en uso.")
                continue

            nombre = input("Nombre del producto: ")
            cantidad = obtener_entero("Cantidad disponible: ")
            precio = obtener_flotante("Precio unitario: $")

            nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(nuevo_producto)

        elif opcion == "2":
            # Eliminar producto
            print("\n--- ELIMINAR PRODUCTO ---")
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            # Actualizar producto
            print("\n--- ACTUALIZAR PRODUCTO ---")
            id_producto = input("ID del producto a actualizar: ")
            print("Deja en blanco si no deseas cambiar un valor.")
            cantidad_str = input("Nueva cantidad (Enter para omitir): ")
            precio_str = input("Nuevo precio (Enter para omitir): ")

            cantidad = int(cantidad_str) if cantidad_str.strip() else None
            precio = float(precio_str) if precio_str.strip() else None

            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            # Buscar por nombre
            print("\n--- BUSCAR PRODUCTO POR NOMBRE ---")
            nombre = input("Ingresa el nombre o parte del nombre: ")
            resultados = inventario.buscar_por_nombre(nombre)

            if resultados:
                print(f"\nSe encontraron {len(resultados)} producto(s):")
                for prod in resultados:
                    print(prod)
            else:
                print("No se encontraron productos con ese nombre.")

        elif opcion == "5":
            # Mostrar todos
            inventario.mostrar_todos()

        elif opcion == "6":
            print("¡Gracias por usar el sistema de inventarios!")
            break

        else:
            print("Opción no válida. Por favor, elige 1-6.")

if __name__ == "__main__":
    main()