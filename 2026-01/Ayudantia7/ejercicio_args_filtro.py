def filtrar_mayores(limite: float, *numeros) -> list:
    """Retorna una lista con los números mayores al límite."""
    return [num for num in numeros if num > limite]

# Script de prueba
if __name__ == "__main__":
    limite = 10
    numeros = (5, 12, 8, 20, 3, 15)
    resultado = filtrar_mayores(limite, *numeros)
    print(f"Números mayores a {limite} en {numeros}: {resultado}")
