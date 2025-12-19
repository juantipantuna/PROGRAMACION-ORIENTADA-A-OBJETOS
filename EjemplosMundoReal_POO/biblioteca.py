"""
SISTEMA DE BIBLIOTECA - EJEMPLO POO
Modela libros, usuarios y préstamos en una biblioteca.
"""

class Libro:
    """Representa un libro en la biblioteca."""
    
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True
    
    def prestar(self):
        """Presta el libro si está disponible."""
        if self.disponible:
            self.disponible = False
            return True
        else:
            print(f"El libro '{self.titulo}' no está disponible.")
            return False
    
    def devolver(self):
        """Devuelve el libro a la biblioteca."""
        self.disponible = True
    
    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"Libro: {self.titulo} | Autor: {self.autor} | Estado: {estado}"


class Usuario:
    """Representa a un usuario de la biblioteca."""
    
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []
    
    def tomar_prestado(self, libro):
        """Un usuario toma prestado un libro."""
        if libro.prestar():
            self.libros_prestados.append(libro)
            print(f"{self.nombre} ha tomado prestado: {libro.titulo}")
    
    def devolver_libro(self, libro):
        """Un usuario devuelve un libro."""
        if libro in self.libros_prestados:
            libro.devolver()
            self.libros_prestados.remove(libro)
            print(f"{self.nombre} ha devuelto: {libro.titulo}")
    
    def __str__(self):
        return f"Usuario: {self.nombre} | ID: {self.id_usuario} | Libros: {len(self.libros_prestados)}"


# === DEMOSTRACIÓN ===
if __name__ == "__main__":
    print("=== SISTEMA DE BIBLIOTECA - EJEMPLO POO ===\n")
    
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "978-0307474728")
    libro2 = Libro("1984", "George Orwell", "978-0451524935")
    
    usuario1 = Usuario("Ana Pérez", "U001")
    usuario2 = Usuario("Luis Gómez", "U002")
    
    print("Estado inicial:")
    print(libro1)
    print(libro2)
    
    print("\n--- Préstamos ---")
    usuario1.tomar_prestado(libro1)
    usuario2.tomar_prestado(libro2)
    
    print("\nEstado después:")
    print(libro1)
    print(libro2)
    print(usuario1)
    print(usuario2)
    
    print("\n--- Devolución ---")
    usuario1.devolver_libro(libro1)
    
    print("\nEstado final:")
    print(libro1)
    print(usuario1)
