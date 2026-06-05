def factorial(n):
    # Caso base
    if n == 0 or n == 1:
        return 1
    # Regla inductiva
    else:
        return n * factorial(n - 1)

# Ejemplo de uso
n = int(input("Ingrese un número entero positivo: "))
if n < 0:
    print("El número debe ser positivo.")
else:
    print(f"El factorial de {n} es {factorial(n)}")
