def repetir(a, b):
    # Caso base
    if b == 0:
        return 0
    elif b == 1:
        return a
    # Regla inductiva
    else:
        return a + repetir(a, b - 1)

# ¿Qué hace la función?
# Multiplica 'a' por 'b' utilizando sumas sucesivas.

# Ejemplo
a, b = 5, 3
print(f"{a} multiplicado por {b} (recursivo) es {repetir(a, b)}")
