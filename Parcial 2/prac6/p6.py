# Definición de la clase Libro
class Libro:
    def _init_(self, titulo, autor, isbn):
        """
        Constructor de la clase Libro.
        
        Inicializa los atributos privados de la clase.
        
        Args:
            titulo (str): Título del libro.
            autor (str): Autor del libro.
            isbn (str): Código ISBN único del libro.
        """
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn
        self.__estado = "disponible"  # Estado inicial del libro

    # Métodos getter para acceder a los atributos de forma controlada
    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_isbn(self):
        return self.__isbn

    def get_estado(self):
        return self.__estado

    # Método setter para modificar el estado del libro
    def set_estado(self, estado):
        """
        Modifica el estado del libro.
        
        Args:
            estado (str): Estado del libro, puede ser "disponible" o "prestado".
        """
        if estado in ["disponible", "prestado"]:
            self.__estado = estado
        else:
            print("Estado inválido")

    # Método para prestar el libro, cambia su estado a "prestado" si está disponible
    def prestar(self):
        """
        Cambia el estado del libro a "prestado" si está disponible.
        """
        if self.__estado == "disponible":
            self.__estado = "prestado"
            print(f"El libro '{self.__titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.__titulo}' ya está prestado.")

    # Método para devolver el libro, cambia su estado a "disponible" si está prestado
    def devolver(self):
        """
        Cambia el estado del libro a "disponible" si está prestado.
        """
        if self.__estado == "prestado":
            self.__estado = "disponible"
            print(f"El libro '{self.__titulo}' ha sido devuelto.")
        else:
            print(f"El libro '{self.__titulo}' ya está disponible.")


# Definición de la clase Biblioteca
class Biblioteca:
    def _init_(self):
        """
        Constructor de la clase Biblioteca.
        
        Inicializa una colección privada para almacenar los libros.
        """
        self.__coleccion_libros = []  # Colección privada de libros

    # Método para agregar un libro a la colección de la biblioteca
    def agregar_libro(self, libro):
        """
        Agrega un libro a la colección de la biblioteca.
        
        Args:
            libro (Libro): Objeto de la clase Libro a agregar.
        """
        self.__coleccion_libros.append(libro)
        print(f"Libro '{libro.get_titulo()}' agregado a la biblioteca.")

    # Método para buscar un libro en la colección por su ISBN
    def buscar_libro_por_isbn(self, isbn):
        """
        Busca un libro en la colección por su ISBN.
        
        Args:
            isbn (str): Código ISBN del libro a buscar.
            
        Returns:
            Libro: El libro encontrado o None si no existe.
        """
        for libro in self.__coleccion_libros:
            if libro.get_isbn() == isbn:
                return libro
        return None

    # Método para prestar un libro según su ISBN
    def prestar_libro(self, isbn):
        """
        Cambia el estado de un libro a "prestado" si está disponible.
        
        Args:
            isbn (str): Código ISBN del libro a prestar.
        """
        libro = self.buscar_libro_por_isbn(isbn)
        if libro:
            libro.prestar()
        else:
            print("Libro no encontrado en la biblioteca.")

    # Método para devolver un libro según su ISBN
    def devolver_libro(self, isbn):
        """
        Cambia el estado de un libro a "disponible" si está prestado.
        
        Args:
            isbn (str): Código ISBN del libro a devolver.
        """
        libro = self.buscar_libro_por_isbn(isbn)
        if libro:
            libro.devolver()
        else:
            print("Libro no encontrado en la biblioteca.")

    # Método para mostrar el estado actual de todos los libros en la colección
    def mostrar_libros(self):
        """
        Imprime el estado de todos los libros en la colección de la biblioteca.
        """
        print("Colección de libros en la biblioteca:")
        for libro in self.__coleccion_libros:
            print(f"Titulo: {libro.get_titulo()}, Autor: {libro.get_autor()}, ISBN: {libro.get_isbn()}, Estado: {libro.get_estado()}")

