def suma_multiplos_3_recursivo(n):
    # Caso base: el bucle original era while n > 1
    if n <= 1:
        return 0
    
    # Caso inductivo (identificando lo que pasa en el bucle)
    if n % 3 == 0:
        return n + suma_multiplos_3_recursivo(n - 1)
    else:
        return suma_multiplos_3_recursivo(n - 1)

# Ejemplo de uso comparativo
n_input = int(input("Da un numero: "))

# Versión iterativa (del enunciado)
n = n_input
suma_iter = 0
while n > 1:
    if n % 3 == 0:
        suma_iter += n
    n -= 1

print(f"Suma iterativa: {suma_iter}")
print(f"Suma recursiva: {suma_multiplos_3_recursivo(n_input)}")
