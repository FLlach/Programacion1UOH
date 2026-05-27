# Base de datos inicial
# Estructura: { "Titulo": ["Genero", ("Sala", "Horario"), Precio] }                            
cartelera = {
    "Inception": ["Sci-Fi", ("Sala 1", "18:00"), 3500.0],
    "The Whale": ["Drama", ("Sala 2", "20:00"), 3000.0]
}

asistentes = []
generos_disponibles = {"Sci-Fi", "Drama"}

def registrar_pelicula(inventario, generos_set, titulo, genero, sala, horario, precio):
    """
    Registra una nueva película en el sistema.
    Actualiza el diccionario de inventario y el set de géneros.
    """
    # La sala y el horario se guardan como una Tupla (inmutable)
    ubicacion = (sala, horario)
    inventario[titulo] = [genero, ubicacion, float(precio)]
    generos_set.add(genero)
    print(f"{titulo} ha sido añadida correctamente")
    return inventario, generos_set

def calcular_total(cantidad, precio_base, descuento=0.1):
    """
    Calcula el total a pagar aplicando un descuento por defecto del 10%.
    Retorna el valor final como float.
    """
    subtotal = cantidad * precio_base
    total = subtotal - (subtotal * descuento)
    return float(total)

def mostrar_cartelera(inventario):
    """
    Muestra de forma ordenada todas las películas registradas.
    Usa un ciclo for para recorrer el diccionario.
    """
    print("\n--- CARTELERA ACTUAL ---")
    if not inventario:
        print("No hay películas registradas.")
    for titulo, datos in inventario.items():
        genero = datos[0]
        sala, hora = datos[1] # Desempaquetado de tupla
        precio = datos[2]
        print(f"{titulo} | Género: {genero} | {sala} a las {hora} | Precio: ${precio}")

def menu(cartelera, asistentes, generos_disponibles):
    """
    Función principal que gestiona el menú del sistema.
    """
    flag = True
    while flag:
        print("\n=== BIENVENIDO AL FESTIVAL DE CINE UOH ===")
        print("1. Agregar Película")
        print("2. Ver Cartelera")
        print("3. Comprar Entradas")
        print("4. Ver Géneros Disponibles (Únicos)")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            genero = input("Género: ")
            sala = input("Sala: ")
            horario = input("Horario (HH:MM): ")
            precio = float(input("Precio Base: "))
            cartelera , generos_disponibles = registrar_pelicula(cartelera, generos_disponibles, titulo, genero, sala, horario, precio)


        elif opcion == "2":
            mostrar_cartelera(cartelera)

        elif opcion == "3":
            mostrar_cartelera(cartelera)
            peli_compra = input("\nIngrese el nombre de la película: ")
            if peli_compra in cartelera:
                cant = int(input("¿Cuántas entradas desea?: "))
                precio_unitario = cartelera[peli_compra][2]
                    
                # Si compra más de 5 entradas, aplicamos un descuento mayor (ej: 20%)
                if cant >= 5:
                    pago = calcular_total(cant, precio_unitario, 0.2)
                    print("¡Descuento grupal aplicado (20%)!")
                else:
                    pago = calcular_total(cant, precio_unitario) # Usa descuento por defecto (10%)
                    
                    nombre_cliente = input("Ingrese su nombre para el registro: ")
                    asistentes.append(nombre_cliente)
                    
                    print(f"Total a pagar: ${pago}")
                    print(f"¡Gracias {nombre_cliente}! Entrada registrada.")

            else:
                print("Esa película no está en cartelera.")

        elif opcion == "4":
            print("\n--- GÉNEROS EN EL FESTIVAL ---")
            # El set evita duplicados automáticamente
            for g in generos_disponibles:
                print(f"- {g}")

        elif opcion == "5":
            print(f"Cerrando sistema... Total de asistentes hoy: {len(asistentes)}")
            flag = False
        else:
            print("Opción no válida.")

menu(cartelera, asistentes, generos_disponibles)
