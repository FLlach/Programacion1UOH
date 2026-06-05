def suma_mas_uno(n):
    if n == 0:
        return 1
    return n + suma_mas_uno(n - 1)

# Análisis solicitado en el Problema #7:
# ¿Cuál es el resultado de suma_mas_uno(4)?
# 4 + suma(3)
# 4 + 3 + suma(2)
# 4 + 3 + 2 + suma(1)
# 4 + 3 + 2 + 1 + suma(0)
# 4 + 3 + 2 + 1 + 1 = 11

print(f"Resultado de suma_mas_uno(4): {suma_mas_uno(4)}")

# Respuestas a las preguntas adicionales:
# 1. ¿Qué pasa si se cambia if n == 0 por if n == 1?
# El caso base se alcanza antes, retornando 1 cuando n es 1.
# suma(4) = 4 + 3 + 2 + 1 = 10.

# 2. ¿Qué pasa si se quita el caso base?
# Ocurre un RecursionError (Maximum recursion depth exceeded) porque la función
# sigue llamándose a sí misma con números negativos infinitamente.
