"""
Sistema de Gestión de Libros
Autores: Juan Tipantuña
Fecha: 25 de enero del 2026
Descripción: Programa que demuestra el uso de constructores (__init__)
             y destructores (__del__) en Python usando solo UNA clase.
"""


class Libro:
    """
    Clase que representa un libro.
    Demuestra claramente el uso del constructor __init__ para inicializar
    y el destructor __del__ para realizar limpieza.
    """

    # Variable de clase para contar cuántos libros se han creado
    total_libros = 0

    def __init__(self, titulo, autor, año, paginas):
        """
        CONSTRUCTOR: Se ejecuta AUTOMÁTICAMENTE al crear un objeto Libro.
        Su función es INICIALIZAR todos los atributos del libro.

        Args:
            titulo (str): Título del libro
            autor (str): Autor del libro
            año (int): Año de publicación
            paginas (int): Número de páginas
        """
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.paginas = paginas
        self.prestado = False  # Valor por defecto
        self.veces_leido = 0

        # Incrementar contador de libros
        Libro.total_libros += 1

        print("=" * 50)
        print(f"[CONSTRUCTOR ejecutado] Libro #{Libro.total_libros} creado:")
        print(f"   Título: {self.titulo}")
        print(f"   Autor: {self.autor}")
        print(f"   Año: {self.año}")
        print(f"   Páginas: {self.paginas}")
        print("=" * 50)

    def leer(self):
        """
        Método para simular la lectura del libro.
        """
        self.veces_leido += 1
        print(f" '{self.titulo}' ha sido leído {self.veces_leido} veces")

    def prestar(self):
        """
        Método para prestar el libro.
        """
        if not self.prestado:
            self.prestado = True
            print(f"✓ '{self.titulo}' ha sido prestado")
        else:
            print(f"✗ '{self.titulo}' ya está prestado")

    def devolver(self):
        """
        Método para devolver el libro.
        """
        if self.prestado:
            self.prestado = False
            print(f"✓ '{self.titulo}' ha sido devuelto")
        else:
            print(f"✗ '{self.titulo}' no estaba prestado")

    def __del__(self):
        """
        DESTRUCTOR: Se ejecuta cuando el objeto va a ser ELIMINADO.
        Su función es REALIZAR TAREAS DE LIMPIEZA antes de que el objeto desaparezca.

        En este caso, mostramos estadísticas y decrementamos el contador.
        """
        Libro.total_libros -= 1

        print("=" * 50)
        print(f"[DESTRUCTOR ejecutado] Eliminando libro:")
        print(f"   Título: '{self.titulo}'")
        print(f"   Estadísticas: Leído {self.veces_leido} veces")
        print(f"   Libros restantes en memoria: {Libro.total_libros}")
        print("=" * 50)


# ==============================================
# PROGRAMA PRINCIPAL
# ==============================================
def main():
    """
    Función principal que demuestra el uso de constructores y destructores.
    """
    print(" DEMOSTRACIÓN DE CONSTRUCTORES Y DESTRUCTORES ")
    print("\n CREANDO LIBROS (se ejecutan constructores __init__):")

    # ========== CREAR LIBROS (CONSTRUCTORES) ==========
    # Cuando creamos estos objetos, automáticamente se ejecuta __init__
    libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 1967, 432)
    libro2 = Libro("Don Quijote", "Miguel de Cervantes", 1605, 863)
    libro3 = Libro("1984", "George Orwell", 1949, 328)

    print("\n USANDO LOS LIBROS:")
    print("-" * 30)

    # Usar métodos de los libros
    libro1.leer()
    libro1.prestar()
    libro2.leer()
    libro2.leer()  # Leer dos veces
    libro3.prestar()

    print("\n ELIMINANDO LIBROS (se ejecutarán destructores __del__):")
    print("-" * 30)

    # ========== ELIMINAR LIBROS (DESTRUCTORES) ==========
    # Cuando eliminamos objetos, automáticamente se ejecuta __del__

    print("\n1. Eliminando libro1...")
    del libro1  # Se ejecuta __del__ de libro1

    print("\n2. Eliminando libro2...")
    del libro2  # Se ejecuta __del__ de libro2

    print("\n3. Libro3 se eliminará automáticamente al final del programa")

    print("\n" + "=" * 60)
    print("PROGRAMA FINALIZADO")
    print("=" * 60)
    print(" Nota: Los destructores __del__ se ejecutan cuando:")
    print("   - Usamos 'del objeto' manualmente")
    print("   - El programa termina (para objetos que quedan)")
    print("   - Python ejecuta el recolector de basura")


# ==============================================
# EJECUCIÓN
# ==============================================
if __name__ == "__main__":
    main()

    # Al finalizar main(), libro3 se eliminará automáticamente
    # y se ejecutará su destructor __del__