from biblioteca import biblioteca 

def menu():
    print('1.Agregar libro')
    print('2.Buscar libro')
    print('3.Pedir libro prestado')
    print('4.Devolver libro')
    print('5.Mostrar lista de libros')
    print('6.Salir')
    print('Ingresa una opcion para poder continuar:')


biblioteca1 = biblioteca()  
op = 0
j = len(biblioteca1.libros)
while(op!=6):
    menu()
    op = int(input())
    if op == 1: 
        titulo = input("Ingresa el titulo del libro: ")
        autor  = input("ingresa el autor del libro:")
        biblioteca1.agregarLibro(titulo,autor,j)
        print('El ISBN del libro es: ', j)
        j += 1   
    elif op == 2:
        bus = int(input("Ingresa el ISBN del libro a buscar: "))
        biblioteca1.buscarLibro(bus)
    elif op == 3: 
        pres = int(input('Ingresa el ISBN de libro:'))         
        biblioteca1.pedirLibro(pres)
    elif op == 4:
        dev = int(input('Ingresa el ISBN del libro: '))
        biblioteca1.devolverLibro(dev)
    elif op == 5:
        biblioteca1.show()
    elif op == 6:
        print('Programa terminado con exito gg.')
    else:
        print(op, ' no es una opcion valida ')