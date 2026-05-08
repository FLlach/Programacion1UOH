# Solución: Gestión de Competencia de Atletismo

# 1. Inicialización
nombres = []
tiempos = []

# 2. Registro de Atletas (Uso de 'for' y 'range')
n_atletas = int(input("¿Cuántos atletas desea registrar?: "))

for i in range(n_atletas):
    nombre = input(f"Ingrese el nombre del atleta {i + 1}: ")
    nombres.append(nombre)

# 3. Ingreso de Tiempos (Uso de 'while' y Validaciones)
for i in range(len(nombres)):
    tiempo = -1
    while tiempo <= 0:
        tiempo = float(input(f"Ingrese el tiempo para {nombres[i]} (segundos): "))
        if tiempo <= 0:
            print("Error: El tiempo debe ser un número mayor a 0.")
    tiempos.append(tiempo)

# 4. Clasificación y Resultados (Uso de 'if', 'elif', 'else')
print("\n--- Resultados de la Competencia ---")
for i in range(len(nombres)):
    nombre = nombres[i]
    tiempo = tiempos[i]
    categoria = ""

    if tiempo < 10.5:
        categoria = "Elite"
    elif 10.5 <= tiempo <= 12.5:
        categoria = "Promedio"
    else:
        categoria = "Principiante"
    
    print(f"Atleta: {nombre} | Tiempo: {tiempo}s | Categoría: {categoria}")

# 5. Búsqueda Final (Uso de Listas y Condicionales)
print("\n--- Búsqueda de Atleta ---")
busqueda = input("Ingrese el nombre del atleta que desea buscar: ")

encontrado = False
for i in range(len(nombres)):
    if nombres[i].lower() == busqueda.lower():
        # Recalcular categoría para mostrar en la búsqueda
        if tiempos[i] < 10.5:
            cat = "Elite"
        elif 10.5 <= tiempos[i] <= 12.5:
            cat = "Promedio"
        else:
            cat = "Principiante"
        
        print(f"Información encontrada: Atleta {nombres[i]}, Tiempo {tiempos[i]}s, Categoría {cat}")
        encontrado = True
        break

if not encontrado:
    print(f"El atleta '{busqueda}' no se encuentra en el registro.")
