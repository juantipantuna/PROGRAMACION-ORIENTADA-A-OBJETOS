import json


class Inventario:
    def __init__(self):
        self.productos = {}
        self.nombres = []
        self.ids = set()

    def agregar_producto(self, producto):
        if producto.id_unico in self.ids:
            print(f"Error: ID {producto.id_unico} ya existe")
            return False

        self.productos[producto.id_unico] = producto
        self.nombres.append(producto.nombre)
        self.ids.add(producto.id_unico)
        print(f"Producto '{producto.nombre}' agregado")
        return True

    def eliminar_producto(self, id_unico):
        if id_unico in self.productos:
            producto = self.productos[id_unico]
            self.nombres.remove(producto.nombre)
            self.ids.remove(id_unico)
            del self.productos[id_unico]
            print(f"Producto '{producto.nombre}' eliminado")
        else:
            print(f"ID {id_unico} no encontrado")

    def actualizar_producto(self, id_unico, cantidad=None, precio=None):
        if id_unico in self.productos:
            producto = self.productos[id_unico]
            if cantidad:
                producto.cantidad = cantidad
            if precio:
                producto.precio = precio
            print(f"Producto '{producto.nombre}' actualizado")

    def buscar_por_nombre(self, nombre_buscar):
        resultados = []
        for producto in self.productos.values():
            if nombre_buscar.lower() in producto.nombre.lower():
                resultados.append(producto)
        return resultados

    def mostrar_todos(self):
        print("\n--- INVENTARIO ---")
        for producto in self.productos.values():
            print(producto)
        print(f"Total: {len(self.productos)} productos")

    def guardar_archivo(self, archivo="inventario.json"):
        datos = []
        for producto in self.productos.values():
            datos.append({
                'id': producto.id_unico,
                'nombre': producto.nombre,
                'cantidad': producto.cantidad,
                'precio': producto.precio
            })

        with open(archivo, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=2, ensure_ascii=False)
        print(f"Datos guardados en {archivo}")

    def cargar_archivo(self, archivo="inventario.json"):
        try:
            with open(archivo, 'r', encoding='utf-8') as f:
                datos = json.load(f)

            self.productos.clear()
            self.nombres.clear()
            self.ids.clear()

            for item in datos:
                from producto import Producto
                producto = Producto(item['id'], item['nombre'],
                                    item['cantidad'], item['precio'])
                self.productos[producto.id_unico] = producto
                self.nombres.append(producto.nombre)
                self.ids.add(producto.id_unico)

            print(f"Datos cargados de {archivo}")
        except FileNotFoundError:
            print("Archivo no encontrado. Inventario vacío.")