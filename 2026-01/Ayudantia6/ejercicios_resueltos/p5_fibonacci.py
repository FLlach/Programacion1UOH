def fibonacci(n):
    # F0 = 0, F1 = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Programa principal
n = int(input("Ingrese n: "))
print(f"Los primeros {n} números de Fibonacci son:")
for i in range(n):
    print(fibonacci(i), end=" ")
print()
