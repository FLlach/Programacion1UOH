def cabeza(lista):
    return lista[0]

def cola(lista):
    return lista[1:]

def sumatoria(lista):
    # Caso base: lista vacía
    if len(lista) == 0:
        return 0
    # Regla inductiva: cabeza + sumatoria de la cola
    else:
        return cabeza(lista) + sumatoria(cola(lista))

# Ejemplo de uso
numeros = [1, 2, 3, 4, 5]
print(f"La sumatoria de {numeros} es {sumatoria(numeros)}")
