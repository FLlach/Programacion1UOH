def es_palindromo(palabra):
    # Limpiar palabra (opcional, para ser robusto)
    palabra = palabra.lower().replace(" ", "")
    
    # Caso base
    if len(palabra) <= 1:
        return True
    
    # Regla inductiva: comparar extremos y llamar recursión con el interior
    if palabra[0] == palabra[-1]:
        return es_palindromo(palabra[1:-1])
    else:
        return False

# Programa principal
p = input("Ingrese una palabra: ")
if es_palindromo(p):
    print(f"Si, {p} es un palíndromo.")
else:
    print(f"No, {p} no es un palíndromo.")
