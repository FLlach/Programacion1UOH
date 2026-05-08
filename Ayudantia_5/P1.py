# Lista de temperaturas de la semana
temperaturas: list[int] = [22, 27, 24, 30, 28, 26, 23]

# Inicializar contadores y variables
dias_calurosos: int = 0
max_temp: int = temperaturas[0]
suma_temperaturas: int = 0

# Recorrer la lista de temperaturas
for temp in temperaturas:
    # Contar los días con temperaturas superiores a 25°C
    if temp > 25:
        dias_calurosos += 1

    # Encontrar la temperatura máxima
    if temp > max_temp:
        max_temp = temp

    # Sumar todas las temperaturas para calcular el promedio
    suma_temperaturas += temp

# Calcular el promedio de la semana
promedio_temperaturas: float = suma_temperaturas / len(temperaturas)

# Imprimir los resultados
print(f"Número de días con temperatura superior a 25°C: {dias_calurosos}")
print(f"La temperatura máxima registrada fue: {max_temp}°C")
print(f"El promedio de las temperaturas fue: {promedio_temperaturas:.2f}°C")