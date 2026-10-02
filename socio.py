class Socio:
    MAX_LIBROS = 3

    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni
        self._libros = []

    @property
    def libros(self):
        return list(self._libros)

    def puede_pedir(self):
        return len(self._libros) < Socio.MAX_LIBROS

    def agregar_libro(self, libro):
        if not self.puede_pedir():
            raise ValueError(f"{self.nombre} ya tiene el máximo de {Socio.MAX_LIBROS} libros")
        self._libros.append(libro)

    def quitar_libro(self, libro):
        if libro not in self._libros:
            raise ValueError(f"{self.nombre} no tiene ese libro")
        self._libros.remove(libro)

    def __str__(self):
        return f"{self.nombre} (DNI {self.dni}) - {len(self._libros)} libro(s) prestado(s)"