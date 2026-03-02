class Producto:
    def __init__(self, id_unico, nombre, cantidad, precio):
        self.id_unico = id_unico
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_unico} | {self.nombre} | Cant: {self.cantidad} | $ {self.precio}"