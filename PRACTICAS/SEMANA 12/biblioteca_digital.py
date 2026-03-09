"""
SISTEMA DE GESTIÓN DE BIBLIOTECA DIGITAL
Versión simplificada
"""


# ============================================================
# CLASE LIBRO
# ============================================================
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Tupla para título y autor (inmutables)
        self._info = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    @property
    def titulo(self):
        return self._info[0]

    @property
    def autor(self):
        return self._info[1]

    def __str__(self):
        return f"'{self.titulo}' - {self.autor} ({self.categoria})"


# ============================================================
# CLASE USUARIO
# ============================================================
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista mutable

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)
        print(f"{self.nombre} tomó: {libro.titulo}")

    def devolver_libro(self, isbn):
        for libro in self.libros_prestados:
            if libro.isbn == isbn:
                self.libros_prestados.remove(libro)
                print(f"{self.nombre} devolvió: {libro.titulo}")
                return libro
        print("Libro no encontrado")
        return None

    def listar_prestados(self):
        if not self.libros_prestados:
            print(f"{self.nombre} no tiene libros")
        else:
            print(f"{self.nombre} tiene:")
            for libro in self.libros_prestados:
                print(f"   - {libro.titulo}")


# ============================================================
# CLASE BIBLIOTECA
# ============================================================
class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.catalogo = {}  # Diccionario: ISBN -> Libro
        self.usuarios = {}  # Diccionario: ID -> Usuario
        self.ids_usuarios = set()  # Conjunto: IDs únicos

    # ---- GESTIÓN DE LIBROS ----
    def agregar_libro(self, libro):
        if libro.isbn in self.catalogo:
            print("ISBN ya existe")
            return False
        self.catalogo[libro.isbn] = libro
        print(f"Libro agregado: {libro.titulo}")
        return True

    def quitar_libro(self, isbn):
        if isbn in self.catalogo:
            libro = self.catalogo.pop(isbn)
            print(f"Libro eliminado: {libro.titulo}")
            return True
        print("ISBN no encontrado")
        return False

    # ---- GESTIÓN DE USUARIOS ----
    def registrar_usuario(self, nombre, id_usuario):
        if id_usuario in self.ids_usuarios:
            print("ID ya existe")
            return False
        self.usuarios[id_usuario] = Usuario(nombre, id_usuario)
        self.ids_usuarios.add(id_usuario)
        print(f"Usuario registrado: {nombre}")
        return True

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            if usuario.libros_prestados:
                print(f"{usuario.nombre} tiene libros prestados")
                return False
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print("Usuario eliminado")
            return True
        print("ID no encontrado")
        return False

    # ---- PRÉSTAMOS ----
    def prestar_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios:
            print("Usuario no existe")
            return False
        if isbn not in self.catalogo:
            print("Libro no existe")
            return False

        # Verificar que no esté prestado
        for usuario in self.usuarios.values():
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    print("Libro ya prestado")
                    return False

        libro = self.catalogo[isbn]
        self.usuarios[id_usuario].prestar_libro(libro)
        return True

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios:
            print("Usuario no existe")
            return False
        return self.usuarios[id_usuario].devolver_libro(isbn) is not None

    # ---- BÚSQUEDAS ----
    def buscar_por_titulo(self, texto):
        print(f"\nBuscando por título: {texto}")
        encontrados = []
        for libro in self.catalogo.values():
            if texto.lower() in libro.titulo.lower():
                encontrados.append(libro)
                print(f"   - {libro}")
        return encontrados

    def buscar_por_autor(self, texto):
        print(f"\nBuscando por autor: {texto}")
        encontrados = []
        for libro in self.catalogo.values():
            if texto.lower() in libro.autor.lower():
                encontrados.append(libro)
                print(f"   - {libro}")
        return encontrados

    def buscar_por_categoria(self, texto):
        print(f"\nBuscando por categoría: {texto}")
        encontrados = []
        for libro in self.catalogo.values():
            if texto.lower() in libro.categoria.lower():
                encontrados.append(libro)
                print(f"   - {libro}")
        return encontrados

    # ---- LISTADOS ----
    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            self.usuarios[id_usuario].listar_prestados()

    def mostrar_catalogo(self):
        print(f"\nCATÁLOGO ({len(self.catalogo)} libros)")
        for libro in self.catalogo.values():
            print(f"   - {libro}")

    def mostrar_usuarios(self):
        print(f"\nUSUARIOS ({len(self.usuarios)})")
        for usuario in self.usuarios.values():
            print(f"   - {usuario.nombre} (ID: {usuario.id_usuario}) - {len(usuario.libros_prestados)} libros")


# ============================================================
# PRUEBA DEL SISTEMA
# ============================================================
if __name__ == "__main__":
    print("=" * 50)
    print("BIBLIOTECA DIGITAL")
    print("=" * 50)

    # Crear biblioteca
    biblio = Biblioteca("Mi Biblioteca")

    # Agregar libros
    print("\n--- AGREGANDO LIBROS ---")
    biblio.agregar_libro(Libro("Cien años de soledad", "García Márquez", "Novela", "001"))
    biblio.agregar_libro(Libro("1984", "George Orwell", "Ciencia Ficción", "002"))
    biblio.agregar_libro(Libro("El Principito", "Saint-Exupéry", "Infantil", "003"))

    # Registrar usuarios
    print("\n--- REGISTRANDO USUARIOS ---")
    biblio.registrar_usuario("Ana", "U1")
    biblio.registrar_usuario("Carlos", "U2")

    # Realizar préstamos
    print("\n--- PRÉSTAMOS ---")
    biblio.prestar_libro("U1", "001")
    biblio.prestar_libro("U1", "002")
    biblio.prestar_libro("U2", "003")

    # Ver préstamos
    print("\n--- ESTADO DE PRÉSTAMOS ---")
    biblio.listar_libros_prestados("U1")
    biblio.listar_libros_prestados("U2")

    # Búsquedas
    print("\n--- BÚSQUEDAS ---")
    biblio.buscar_por_titulo("cien")
    biblio.buscar_por_autor("orwell")
    biblio.buscar_por_categoria("infantil")

    # Devolver libro
    print("\n--- DEVOLUCIÓN ---")
    biblio.devolver_libro("U1", "001")

    # Estado final
    print("\n--- ESTADO FINAL ---")
    biblio.mostrar_catalogo()
    biblio.mostrar_usuarios()

    print("\n" + "=" * 50)
    print("FIN DEL PROGRAMA")
    print("=" * 50)