"""
SISTEMA DE TIENDA ONLINE - EJEMPLO POO
Modela productos, carrito y clientes.
"""

class Producto:
    """Representa un producto en la tienda."""
    
    def __init__(self, id_producto, nombre, precio, stock):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def reducir_stock(self, cantidad):
        """Reduce el stock del producto."""
        if self.stock >= cantidad:
            self.stock -= cantidad
            return True
        else:
            print(f"Stock insuficiente de {self.nombre}. Solo hay {self.stock} unidades.")
            return False
    
    def __str__(self):
        return f"Producto: {self.nombre} | Precio: ${self.precio} | Stock: {self.stock}"


class Cliente:
    """Representa a un cliente de la tienda."""
    
    def __init__(self, id_cliente, nombre, email):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.email = email
        self.carrito = []
    
    def agregar_al_carrito(self, producto, cantidad=1):
        """Agrega un producto al carrito."""
        if producto.reducir_stock(cantidad):
            self.carrito.append((producto, cantidad))
            print(f"Agregado: {cantidad} x {producto.nombre}")
    
    def mostrar_carrito(self):
        """Muestra los productos en el carrito."""
        if not self.carrito:
            print("El carrito está vacío.")
            return
        
        print(f"\n--- Carrito de {self.nombre} ---")
        total = 0
        for producto, cantidad in self.carrito:
            subtotal = producto.precio * cantidad
            total += subtotal
            print(f"{producto.nombre} x{cantidad}: ${subtotal}")
        print(f"TOTAL: ${total}")
    
    def __str__(self):
        return f"Cliente: {self.nombre} | Email: {self.email} | Productos en carrito: {len(self.carrito)}"


# === DEMOSTRACIÓN ===
if __name__ == "__main__":
    print("=== TIENDA ONLINE - EJEMPLO POO ===\n")
    
    p1 = Producto(1, "Laptop", 1200, 10)
    p2 = Producto(2, "Mouse", 25, 50)
    p3 = Producto(3, "Teclado", 75, 30)
    
    cliente = Cliente(101, "Carlos Ruiz", "carlos@email.com")
    
    print("Productos disponibles:")
    print(p1)
    print(p2)
    print(p3)
    
    print(f"\n--- {cliente.nombre} está comprando ---")
    cliente.agregar_al_carrito(p1, 1)
    cliente.agregar_al_carrito(p2, 2)
    cliente.agregar_al_carrito(p3, 1)
    
    cliente.mostrar_carrito()
    
    print("\nStock actualizado:")
    print(p1)
    print(p2)
    print(p3)
    
    print(f"\n{cliente}")
