def string_inverso(n):
    # Caso base
    if n == 1:
        return "1"
    # Regla inductiva
    else:
        return str(n) + " " + string_inverso(n - 1)

# Ejemplo de uso
n = int(input("Ingrese n: "))
print(string_inverso(n))
