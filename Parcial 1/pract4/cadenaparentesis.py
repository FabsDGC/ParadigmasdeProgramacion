def longest_valid_parentheses(s: str) -> int:
    max_len = 0  # Longitud máxima de subcadenas válidas
    stack = []   # Pila para rastrear los índices de los paréntesis no balanceados
    last_invalid = -1  # Índice del último paréntesis inválido

    for i, char in enumerate(s):
        if char == '(':  # Si es paréntesis de apertura, lo almacenamos en la pila
            stack.append(i)
        else:
            if stack:  # Si la pila no está vacía, hay un paréntesis de apertura para balancear
                stack.pop()  # Se balancea el paréntesis con uno de apertura
                if stack:  # Si aún hay paréntesis en la pila, calculamos la longitud
                    max_len = max(max_len, i - stack[-1])
                else:
                    max_len = max(max_len, i - last_invalid)
            else:
                last_invalid = i  # Marcamos el índice como último paréntesis inválido

    return max_len


# Bucle continuo para solicitar entradas al usuario hasta que decida terminar
while True:
    # Solicitar al usuario que ingrese una cadena de paréntesis
    cadena = input("Ingresa una cadena de paréntesis: ")

    # Llamar a la función y mostrar el resultado
    resultado = longest_valid_parentheses(cadena)
    print(f"La longitud de la subcadena válida más larga es: {resultado}")
    
    # Preguntar al usuario si desea continuar
    continuar = input("¿Deseas ingresar otra cadena? (sí/no): ").strip().lower()
    if continuar != 'sí':
        print("Programa terminado.")
        break
