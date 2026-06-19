def unir_palabras(*palabras) -> str:
    """Une una cantidad variable de palabras separadas por un espacio."""
    return " ".join(palabras)

# Script de prueba
if __name__ == "__main__":
    print(f"Resultado: '{unir_palabras('Hola', 'mundo', 'desde', 'Python')}'")
    print(f"Resultado: '{unir_palabras('POO', 'es', 'genial')}'")
