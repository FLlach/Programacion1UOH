# Solución: Sistema de Gestión de Biblioteca "UOH Library"

# --- Estructuras de Datos Globales ---
# Formato Catálogo: { "Título": ["Autor", "Género", Stock] }
catalogo = {
    "Cien años de soledad": ["Gabriel García Márquez", "Realismo Mágico", 5],
    "1984": ["George Orwell", "Distopía", 3],
    "El Principito": ["Antoine de Saint-Exupéry", "Fábula", 10],
    "Don Quijote de la Mancha": ["Miguel de Cervantes", "Novela", 2]
}

# Lista de libros prestados en la sesión
libros_prestados = []

# Set de categorías únicas
generos_literarios = {"Realismo Mágico", "Distopía", "Fábula", "Novela"}

def mostrar_catalogo(inventario):
    """
    Recorre el diccionario del catálogo y muestra los libros disponibles.
    Usa un ciclo for para la visualización.
    """
    print("\n--- CATÁLOGO DE LIBROS UOH ---")
    print(f"{'Título':<30} | {'Autor':<25} | {'Stock':<5}")
    print("-" * 65)
    for titulo, datos in inventario.items():
        autor = datos[0]
        stock = datos[2]
        if stock > 0:
            print(f"{titulo:<30} | {autor:<25} | {stock:<5}")
    print("-" * 65)

def registrar_libro(inventario, set_generos, titulo, autor, genero, stock):
    """
    Agrega o actualiza un libro en el catálogo.
    Actualiza el set de géneros automáticamente.
    Retorna True si la operación fue exitosa.
    """
    inventario[titulo] = [autor, genero, stock]
    set_generos.add(genero)
    return True

def realizar_prestamo_express(inventario, prestados):
    """
    Gestiona el préstamo de hasta 3 libros usando un ciclo while con contador.
    Actualiza el inventario y la lista de prestados.
    """
    nombre_estudiante = input("\nIngrese su nombre: ")
    contador = 0
    maximo_libros = 3
    
    print(f"Bienvenido {nombre_estudiante}. Puedes solicitar hasta {maximo_libros} libros.")
    
    continuar = "si"
    while contador < maximo_libros and continuar == "si":
        print(f"\nLibros solicitados: {contador}/{maximo_libros}")
        libro_buscado = input("¿Qué libro desea pedir?: ")
        
        if libro_buscado in inventario:
            stock_actual = inventario[libro_buscado][2]
            
            if stock_actual > 0:
                # Actualizar stock y registro
                inventario[libro_buscado][2] -= 1
                prestados.append(libro_buscado)
                contador += 1
                print(f"¡Préstamo de '{libro_buscado}' exitoso!")
            else:
                print("Lo sentimos, no quedan ejemplares disponibles de este libro.")
        else:
            print("El libro no se encuentra en nuestro catálogo.")
        
        # Verificar si puede seguir pidiendo
        if contador < maximo_libros:
            continuar = input("¿Desea pedir otro libro? (si/no): ").lower()
        else:
            print("Has alcanzado el límite máximo de préstamos por sesión.")

    print(f"Sesión de préstamo finalizada para {nombre_estudiante}.")

def generar_reporte(prestados, dias_plazo=7):
    """
    Muestra un resumen de los libros prestados y el plazo de devolución.
    'dias_plazo' es un parámetro por defecto.
    """
    print("\n--- REPORTE DE SESIÓN ---")
    total = len(prestados)
    print(f"Total de libros prestados hoy: {total}")
    
    if total > 0:
        print("Títulos que salieron de la biblioteca:")
        for libro in prestados:
            print(f"- {libro}")
        print(f"\nRECUERDE: El plazo de devolución es de {dias_plazo} días hábiles.")
    else:
        print("No se realizaron préstamos en esta sesión.")

def menu_principal():
    """
    Controlador principal con ciclo while y validaciones if-elif-else.
    """
    activo = True
    while activo:
        print("\n=== SISTEMA DE BIBLIOTECA UOH ===")
        print("1. Mostrar Catálogo")
        print("2. Préstamo Express (Máx 3 libros)")
        print("3. Agregar/Actualizar Libro")
        print("4. Generar Reporte y Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            mostrar_catalogo(catalogo)
        
        elif opcion == "2":
            realizar_prestamo_express(catalogo, libros_prestados)
            
        elif opcion == "3":
            t = input("Título: ")
            a = input("Autor: ")
            g = input("Género: ")
            s = input("Stock inicial: ")
            
            # Validación manual sin try-except
            if s.isdigit():
                registrar_libro(catalogo, generos_literarios, t, a, g, int(s))
                print(f"Libro '{t}' registrado correctamente.")
            else:
                print("Error: El stock debe ser un número entero.")
                
        elif opcion == "4":
            generar_reporte(libros_prestados)
            print("\nGracias por usar UOH Library. ¡Hasta pronto!")
            activo = False
            
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

menu_principal()
