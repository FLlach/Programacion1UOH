def calcular_promedio(*numeros) -> float:
    """Calcula el promedio de una cantidad variable de números."""
    if not numeros:
        return 0.0
    return sum(numeros) / len(numeros)

# Script de prueba
if __name__ == "__main__":
    print(f"Promedio de (10, 20, 30): {calcular_promedio(10, 20, 30)}")
    print(f"Promedio de (5, 5): {calcular_promedio(5, 5)}")
    print(f"Promedio sin argumentos: {calcular_promedio()}")
