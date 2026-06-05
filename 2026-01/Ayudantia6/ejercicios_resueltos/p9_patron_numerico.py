def imprimir_patron(n):
    if n > 0:
        imprimir_patron(n - 1)
        print((str(n) + " ") * n)

def imprimir_patron_al_reves(n):
    if n > 0:
        print((str(n) + " ") * n)
        imprimir_patron_al_reves(n - 1)

# Ejemplo de uso
num = 5
print(f"Patrón normal (n={num}):")
imprimir_patron(num)

print(f"\nPatrón al revés (n={num}):")
imprimir_patron_al_reves(num)
