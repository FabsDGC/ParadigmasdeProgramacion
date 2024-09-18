import math

#made by fabs 3BV2
#PARADIGMAS DE pROGRAMACIÓN
#función del circulo
def circulo():
    radio = float(input("Introduce el radio del círculo en metros: "))
    print("1. Calcular Área")
    print("2. Calcular Perímetro")
    print("3. Calcular Ambos")
    opcion = input("Elige una opción: ")
    
    if opcion == '1':
        area_m = math.pi * radio**2
        print(f"Área del círculo: {area_m:.2f} m² ({area_m * 10000:.2f} cm²)\n")
    elif opcion == '2':
        perimetro_m = 2 * math.pi * radio
        print(f"Perímetro del círculo: {perimetro_m:.2f} m ({perimetro_m * 100:.2f} cm)\n")
    elif opcion == '3':
        area_m = math.pi * radio**2
        perimetro_m = 2 * math.pi * radio
        print(f"Área del círculo: {area_m:.2f} m² ({area_m * 10000:.2f} cm²)")
        print(f"Perímetro del círculo: {perimetro_m:.2f} m ({perimetro_m * 100:.2f} cm)\n")


#funcion del cuadrado
def cuadrado():
    lado = float(input("Introduce el lado del cuadrado en metros: "))
    print("1. Calcular Área")
    print("2. Calcular Perímetro")
    print("3. Calcular Ambos")
    opcion = input("Elige una opción: ")
    
    if opcion == '1':
        area_m = lado**2
        print(f"Área del cuadrado: {area_m:.2f} m² ({area_m * 10000:.2f} cm²)\n")
    elif opcion == '2':
        perimetro_m = 4 * lado
        print(f"Perímetro del cuadrado: {perimetro_m:.2f} m ({perimetro_m * 100:.2f} cm)\n")
    elif opcion == '3':
        area_m = lado**2
        perimetro_m = 4 * lado
        print(f"Área del cuadrado: {area_m:.2f} m² ({area_m * 10000:.2f} cm²)")
        print(f"Perímetro del cuadrado: {perimetro_m:.2f} m ({perimetro_m * 100:.2f} cm)\n")


#función del rectangulo
def rectangulo():
    largo = float(input("Introduce el largo del rectángulo en metros: "))
    ancho = float(input("Introduce el ancho del rectángulo en metros: "))
    print("1. Calcular Área")
    print("2. Calcular Perímetro")
    print("3. Calcular Ambos")
    opcion = input("Elige una opción: ")
    
    if opcion == '1':
        area_m = largo * ancho
        print(f"Área del rectángulo: {area_m:.2f} m² ({area_m * 10000:.2f} cm²)\n")
    elif opcion == '2':
        perimetro_m = 2 * (largo + ancho)
        print(f"Perímetro del rectángulo: {perimetro_m:.2f} m ({perimetro_m * 100:.2f} cm)\n")
    elif opcion == '3':
        area_m = largo * ancho
        perimetro_m = 2 * (largo + ancho)
        print(f"Área del rectángulo: {area_m:.2f} m² ({area_m * 10000:.2f} cm²)")
        print(f"Perímetro del rectángulo: {perimetro_m:.2f} m ({perimetro_m * 100:.2f} cm)\n")

#función del triangulo

def triangulo():
    base = float(input("Introduce la base del triángulo en metros: "))
    altura = float(input("Introduce la altura del triángulo en metros: "))
    lado1 = float(input("Introduce el lado 1 del triángulo en metros: "))
    lado2 = float(input("Introduce el lado 2 del triángulo en metros: "))
    print("1. Calcular Área")
    print("2. Calcular Perímetro")
    print("3. Calcular Ambos")
    opcion = input("Elige una opción: ")
    
    if opcion == '1':
        area_m = (base * altura) / 2
        print(f"Área del triángulo: {area_m:.2f} m² ({area_m * 10000:.2f} cm²)\n")
    elif opcion == '2':
        perimetro_m = base + lado1 + lado2
        print(f"Perímetro del triángulo: {perimetro_m:.2f} m ({perimetro_m * 100:.2f} cm)\n")
    elif opcion == '3':
        area_m = (base * altura) / 2
        perimetro_m = base + lado1 + lado2
        print(f"Área del triángulo: {area_m:.2f} m² ({area_m * 10000:.2f} cm²)")
        print(f"Perímetro del triángulo: {perimetro_m:.2f} m ({perimetro_m * 100:.2f} cm)\n")

#función del traepcio

def trapecio():
    base_mayor = float(input("Introduce la base mayor del trapecio en metros: "))
    base_menor = float(input("Introduce la base menor del trapecio en metros: "))
    altura = float(input("Introduce la altura del trapecio en metros: "))
    lado1 = float(input("Introduce el lado 1 del trapecio en metros: "))
    lado2 = float(input("Introduce el lado 2 del trapecio en metros: "))
    print("1. Calcular Área")
    print("2. Calcular Perímetro")
    print("3. Calcular Ambos")
    opcion = input("Elige una opción: ")
    
    if opcion == '1':
        area_m = ((base_mayor + base_menor) * altura) / 2
        print(f"Área del trapecio: {area_m:.2f} m² ({area_m * 10000:.2f} cm²)\n")
    elif opcion == '2':
        perimetro_m = base_mayor + base_menor + lado1 + lado2
        print(f"Perímetro del trapecio: {perimetro_m:.2f} m ({perimetro_m * 100:.2f} cm)\n")
    elif opcion == '3':
        area_m = ((base_mayor + base_menor) * altura) / 2
        perimetro_m = base_mayor + base_menor + lado1 + lado2
        print(f"Área del trapecio: {area_m:.2f} m² ({area_m * 10000:.2f} cm²)")
        print(f"Perímetro del trapecio: {perimetro_m:.2f} m ({perimetro_m * 100:.2f} cm)\n")



#función del menú

def menu():
    while True:
        print("Menú de cálculo de área y perímetro")
        print("1. Círculo")
        print("2. Cuadrado")
        print("3. Rectángulo")
        print("4. Triángulo")
        print("5. Trapecio")
        print("6. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            circulo()
        elif opcion == '2':
            cuadrado()
        elif opcion == '3':
            rectangulo()
        elif opcion == '4':
            triangulo()
        elif opcion == '5':
            trapecio()
        elif opcion == '6':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.\n")

# ejecutar el menu
menu()

#Fabio Gonzalez