def invertir_palabra(palabra):
    # Caso base
    if len(palabra) <= 1:
        return palabra
    # Regla inductiva: último carácter + inversión del resto
    else:
        return palabra[-1] + invertir_palabra(palabra[:-1])

# Ejemplo de uso
p = input("Ingrese una palabra: ")
print(f"Invertida: {invertir_palabra(p)}")
