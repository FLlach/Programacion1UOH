def cabeza(lista):
    return lista[0]

def cola(lista):
    return lista[1:]

def cuadrados(lista):
    # Caso base
    if len(lista) == 0:
        return []
    # Regla inductiva: cuadrado de la cabeza concatenado con cuadrados de la cola
    else:
        return [cabeza(lista)**2] + cuadrados(cola(lista))

# Ejemplo de uso
numeros = [1, 2, 5, -2, 13]
print(f"Original: {numeros}")
print(f"Cuadrados: {cuadrados(numeros)}")
