class libro: 
    titulo = ''
    autor = ''
    isbn = 0
    estado = True  

    

    
    def __init__(self, titulo, autor, isbn, estado): #constructor 
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.estado = estado

    def getTitulo(self):
        return self.titulo
    
    def setTitulo(self,titulo):
        self.titulo = titulo
    
    def getAutor(self):
        return self.autor

    def setAutor(self,autor):
        self.autor = autor

    def getIsbn(self):
        return self.isbn

    def setIsbn(self, isbn):
        self.isbn = isbn

    def getEstado(self):
        return self.estado
    
    def setEstado(self, estado):
        self.estado = estado