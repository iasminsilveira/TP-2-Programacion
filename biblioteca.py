class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self._libros = {}
        self._socios = {}

    def agregar_libro(self, libro):
        if libro.isbn in self._libros:
            raise ValueError(f"Ya existe un libro con ISBN {libro.isbn}")
        self._libros[libro.isbn] = libro

    def registrar_socio(self, socio):
        if socio.dni in self._socios:
            raise ValueError(f"Ya existe un socio con DNI {socio.dni}")
        self._socios[socio.dni] = socio

    def _buscar(self, isbn, dni):
        libro = self._libros.get(isbn)
        socio = self._socios.get(dni)
        if libro is None:
            raise ValueError(f"No existe el libro {isbn}")
        if socio is None:
            raise ValueError(f"No existe el socio {dni}")
        return libro, socio

    def prestar(self, isbn, dni):
        libro, socio = self._buscar(isbn, dni)
        if not libro.disponible:
            raise ValueError(f"El libro {libro.titulo} no está disponible")
        if not socio.puede_pedir():
            raise ValueError(f"{socio.nombre} llegó al máximo de libros")
        libro.prestar()
        socio.agregar_libro(libro)

    def devolver(self, isbn, dni):
        libro, socio = self._buscar(isbn, dni)
        socio.quitar_libro(libro)
        libro.devolver()

    def libros_disponibles(self):
        disponibles = []
        for libro in self._libros.values():
            if libro.disponible:
                disponibles.append(libro)
        return disponibles