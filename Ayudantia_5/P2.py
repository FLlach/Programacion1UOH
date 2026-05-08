# Lista de compras vacía
lista_compras: list[str] = []
# Agregar elementos a la lista de compras
print("Agrega 5 productos a tu lista de compras:")

for i in range(5):
    producto: str = input(f"Ingresa el producto {i+1}: ")
    lista_compras.append(producto)  # Agrega el producto a la lista
    print(f"Producto '{producto}' agregado.")

# Mostrar la lista actual
print("\nTu lista de compras actual es:")
print(lista_compras)

# Eliminar un elemento de la lista usando remove()
producto_eliminar: str = input("\n¿Deseas eliminar algún producto por nombre? Ingresa su nombre: ")
if producto_eliminar in lista_compras:
    lista_compras.remove(producto_eliminar)  # Elimina el producto de la lista
    print(f"Producto '{producto_eliminar}' eliminado.")
else:
    print(f"El producto '{producto_eliminar}' no está en la lista.")

# Mostrar la lista actualizada
print("\nLista de compras actualizada:")
print(lista_compras)

# Eliminar el último elemento de la lista usando pop()
if lista_compras:  # Verifica si la lista no está vacía
    producto_eliminar_ultimo: str = input("\n¿Deseas eliminar el último producto de la lista? (sí/no): ").lower()
    if producto_eliminar_ultimo == "si":
        eliminado = lista_compras.pop()  # Elimina el último producto de la lista
        print(f"Producto '{eliminado}' eliminado (último producto).")
    else:
        print("No se eliminó ningún producto.")
else:
    print("La lista está vacía. No hay productos para eliminar.")

# Mostrar la lista final
print("\nTu lista de compras final es:")
print(lista_compras)