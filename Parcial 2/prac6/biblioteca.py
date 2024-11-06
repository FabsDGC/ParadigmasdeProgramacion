from libro import libro

class biblioteca: 
    
    def __init__(self):
        self.libros = [
                libro('1984', 'George Orwell', 0, True), 
                libro('The great gatsby', 'F.Scott Fitzergald', 1, True)
                ]
    
    
    def agregarLibro(self, titulo, autor, isbn ):
        self.libros.append(libro(titulo,autor,isbn, True))

    def buscarLibro(self,isbn):
        j = -1
        for libro in self.libros:
            if(isbn == libro.getIsbn()):
              print("Titulo", libro.getTitulo())
              print('Autor', libro.getAutor())
              j = libro.getIsbn()

        if(j == -1):
            print("el libro no existe en la biblioteca")
    def pedirLibro(self, isbn):
        j = -1
        for libro in self.libros: 
            if(isbn == libro.getIsbn()) and (libro.getEstado() == True):
                libro.setEstado(False)
                print('Te hemos prestado el libro ', libro.getTitulo())
                j = libro.getIsbn()
                break
        if j == -1: 
            print('El libro no esta disponinble')
    
    def devolverLibro(self,isbn):
        j = -1
        for libro in self.libros:
            if(isbn == libro.getIsbn()) and  (libro.getEstado() == False ):
                libro.setEstado(True)
                print("Haz regresado el libro ", libro.getTitulo())
                j = libro.getIsbn()
        if j == -1:
            print('Nunca te prestamos ese libro')

    def show(self):
        for libro in self.libros:
            print("titulo: ", libro.getTitulo())
            print('Autor:', libro.getAutor())
            print('ISBN:', libro.getIsbn())
            print('Estado:', libro.getEstado())           


 
         