"""
Clase Inventario: Gestiona una colección de objetos Producto.
"""
from producto import Producto

class Inventario:
    def __init__(self):
        """Inicializa el inventario con una lista vacía de productos."""
        self._productos = []  # Lista de objetos Producto

    def añadir_producto(self, producto):
        """
        Añade un nuevo producto al inventario.
        Verifica que el ID sea único.
        :param producto: Objeto de tipo Producto
        :return: True si se añadió, False si el ID ya existe
        """
        if any(p.id == producto.id for p in self._productos):
            print(f"Error: Ya existe un producto con ID {producto.id}.")
            return False
        self._productos.append(producto)
        print(f"Producto '{producto.nombre}' añadido correctamente.")
        return True

    def eliminar_producto(self, id_producto):
        """
        Elimina un producto por su ID.
        :param id_producto: ID del producto a eliminar
        :return: True si se eliminó, False si no se encontró
        """
        for i, producto in enumerate(self._productos):
            if producto.id == id_producto:
                eliminado = self._productos.pop(i)
                print(f"Producto '{eliminado.nombre}' eliminado.")
                return True
        print(f"Error: No se encontró producto con ID {id_producto}.")
        return False

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """
        Actualiza cantidad y/o precio de un producto por su ID.
        :param id_producto: ID del producto a actualizar
        :param cantidad: Nueva cantidad (opcional)
        :param precio: Nuevo precio (opcional)
        :return: True si se actualizó, False si no se encontró
        """
        for producto in self._productos:
            if producto.id == id_producto:
                if cantidad is not None:
                    producto.cantidad = cantidad
                if precio is not None:
                    producto.precio = precio
                print(f"Producto ID {id_producto} actualizado.")
                return True
        print(f"Error: No se encontró producto con ID {id_producto}.")
        return False

    def buscar_por_nombre(self, nombre):
        """
        Busca productos cuyo nombre contenga el texto buscado (insensible a mayúsculas).
        :param nombre: Texto a buscar en el nombre
        :return: Lista de productos que coinciden
        """
        resultados = [p for p in self._productos if nombre.lower() in p.nombre.lower()]
        return resultados

    def mostrar_todos(self):
        """Muestra todos los productos en el inventario."""
        if not self._productos:
            print("El inventario está vacío.")
        else:
            print("\n--- INVENTARIO COMPLETO ---")
            for producto in self._productos:
                print(producto)
            print("----------------------------")