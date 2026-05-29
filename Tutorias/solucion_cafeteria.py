import random

# --- Estructuras de Datos Globales ---
# Formato Menú: { "Producto": ["Categoría", PrecioBase, Stock] }
menu = {
    "Espresso": ["Bebida Caliente", 1500, 50],
    "Cappuccino": ["Bebida Caliente", 2500, 30],
    "Sandwich Jamon Queso": ["Sandwich", 3500, 15],
    "Muffin Arandano": ["Pasteleria", 1800, 20]
}

# Lista de ventas: Almacena tuplas (nombre, cantidad, total)
ventas_diarias = []

# Set de categorías únicas
categorias = {"Bebida Caliente", "Sandwich", "Pasteleria"}

def mostrar_menu(inventario):
    """
    Recorre el diccionario del menú y muestra los productos formateados.
    """
    print("\n--- MENÚ UOH COFFEE ---")
    print(f"{'Producto':<25} | {'Categoría':<20} | {'Precio':<8} | {'Stock':<5}")
    print("-" * 65)
    for producto, datos in inventario.items():
        cat, precio, stock = datos
        print(f"{producto:<25} | {cat:<20} | ${precio:<7} | {stock:<5}")

def calcular_pago(cantidad, precio_unitario, descuento=0.0):
    """
    Calcula el total aplicando un descuento opcional (parámetro por defecto).
    Retorna el total como float.
    """
    subtotal = cantidad * precio_unitario
    total = subtotal * (1 - descuento)
    return float(total)

def realizar_pedido(inventario, ventas):
    """
    Gestiona la lógica de compra de un producto.
    Actualiza el stock y registra la venta en la lista.
    """
    mostrar_menu(inventario)
    nombre_p = input("\nIngrese el nombre del producto que desea: ")
    
    if nombre_p in inventario:
        cant = input("¿Cuántas unidades desea?: ")
        # Validación manual de entero para evitar try-except
        if cant.isdigit():
            cant = int(cant)
            stock_actual = inventario[nombre_p][2]
            
            if cant <= stock_actual:
                precio_base = inventario[nombre_p][1]
                
                # Preguntar si es estudiante para aplicar descuento
                es_estudiante = input("¿Es estudiante? (si/no): ").lower()
                desc = 0.0
                if es_estudiante == "si":
                    desc = 0.15 # 15% de descuento
                    print("¡Descuento de estudiante aplicado!")
                
                total = calcular_pago(cant, precio_base, desc)
                
                # Actualizar Stock
                inventario[nombre_p][2] -= cant
                
                # Registrar Venta (Tupla)
                venta = (nombre_p, cant, total)
                ventas.append(venta)
                
                print(f"\nPedido exitoso: {cant}x {nombre_p}")
                print(f"Total a pagar: ${total}")
                
                # Generar Cupón con random
                codigo = random.randint(1000, 9999)
                print(f"¡Felicidades! Tu código de descuento para la próxima compra es: {codigo}")
                
            else:
                print(f"Error: Stock insuficiente. Solo quedan {stock_actual} unidades.")
        else:
            print("Error: La cantidad debe ser un número entero.")
    else:
        print("Error: El producto no existe en el menú.")

def gestionar_administracion(inventario, set_categorias):
    """
    Permite añadir nuevos productos o actualizar el stock.
    """
    print("\n--- MÓDULO DE ADMINISTRACIÓN ---")
    nuevo_p = input("Nombre del producto: ")
    cat = input("Categoría: ")
    precio = input("Precio: ")
    stock = input("Stock Inicial: ")
    
    if precio.replace('.','',1).isdigit() and stock.isdigit():
        inventario[nuevo_p] = [cat, float(precio), int(stock)]
        set_categorias.add(cat)
        print(f"Producto '{nuevo_p}' actualizado/añadido correctamente.")
    else:
        print("Error: Precio o Stock no válidos.")

def generar_reporte(ventas):
    """
    Calcula estadísticas básicas de las ventas del día.
    """
    print("\n--- REPORTE DE VENTAS DIARIAS ---")
    if not ventas:
        print("No se realizaron ventas hoy.")
        return

    total_recaudado = 0
    conteo_productos = {} # Para ver cuál se vendió más
    
    for v in ventas:
        nombre, cant, total = v
        total_recaudado += total
        
        # Lógica para encontrar el más vendido
        if nombre in conteo_productos:
            conteo_productos[nombre] += cant
        else:
            conteo_productos[nombre] = cant
            
    print(f"Total Recaudado: ${total_recaudado}")
    
    # Encontrar el máximo en el diccionario de conteo
    mas_vendido = ""
    max_cant = 0
    for p, c in conteo_productos.items():
        if c > max_cant:
            max_cant = c
            mas_vendido = p
            
    print(f"Producto más solicitado: {mas_vendido} ({max_cant} unidades)")

def menu_principal():
    """
    Controlador principal del programa.
    """
    ejecutando = True
    while ejecutando:
        print("\n=== SISTEMA UOH COFFEE ===")
        print("1. Ver Menú")
        print("2. Realizar Pedido")
        print("3. Administración (Agregar/Actualizar)")
        print("4. Generar Reporte del Día")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            mostrar_menu(menu)
        elif opcion == "2":
            realizar_pedido(menu, ventas_diarias)
        elif opcion == "3":
            gestionar_administracion(menu, categorias)
        elif opcion == "4":
            generar_reporte(ventas_diarias)
        elif opcion == "5":
            print("Gracias por usar el sistema UOH Coffee. ¡Adiós!")
            ejecutando = False
        else:
            print("Opción no válida, intente nuevamente.")

# Iniciar el programa
if __name__ == "__main__":
    menu_principal()
