# Crear un diccionario vacío para la agenda de contactos
agenda: dict[str, int]= {}

# Agregar contactos a la agenda
print("Agregar 3 contactos a tu agenda:")

for i in range(3):
    nombre: str = input(f"Ingresa el nombre del contacto {i+1}: ")
    telefono: int = input(f"Ingresa el número de teléfono para {nombre}: ")
    agenda[nombre] = telefono  # Agrega el contacto al diccionario
    print(f"Contacto '{nombre}' agregado con número '{telefono}'.")

# Mostrar la agenda actual
print("\nTu agenda de contactos actual es:")
for nombre, telefono in agenda.items():
    print(f"{nombre}: {telefono}")

# Eliminar un contacto usando del
nombre_eliminar_del: str = input("\n¿Deseas eliminar un contacto usando 'del'? Ingresa el nombre: ")
if nombre_eliminar_del in agenda:
    del agenda[nombre_eliminar_del]  # Elimina el contacto del diccionario
    print(f"Contacto '{nombre_eliminar_del}' eliminado usando 'del'.")
else:
    print(f"El contacto '{nombre_eliminar_del}' no está en la agenda.")

# Mostrar la agenda después de usar del
print("\nAgenda después de usar 'del':")
for nombre, telefono in agenda.items():
    print(f"{nombre}: {telefono}")

# Eliminar un contacto usando pop()
nombre_eliminar_pop: str = input("\n¿Deseas eliminar un contacto usando 'pop()'? Ingresa el nombre: ")
telefono_eliminado: str = agenda.pop(nombre_eliminar_pop, None)  # Elimina el contacto y obtiene el valor
if telefono_eliminado:
    print(f"Contacto '{nombre_eliminar_pop}' eliminado usando 'pop()'.")
else:
    print(f"El contacto '{nombre_eliminar_pop}' no está en la agenda.")

# Mostrar la agenda después de usar pop()
print("\nAgenda después de usar 'pop()':")
for nombre, telefono in agenda.items():
    print(f"{nombre}: {telefono}")

# Eliminar el último contacto usando popitem()
if agenda:  # Verifica si la agenda no está vacía
    eliminado: str = agenda.popitem()  # Elimina y obtiene el último par clave-valor
    print(f"Contacto '{eliminado[0]}' eliminado usando 'popitem()'.")
else:
    print("La agenda está vacía. No hay contactos para eliminar usando 'popitem()'.")

# Mostrar la agenda después de usar popitem()
print("\nAgenda después de usar 'popitem()':")
for nombre, telefono in agenda.items():
    print(f"{nombre}: {telefono}")

# Vaciar la agenda usando clear()
vaciar_agenda: str = input("\n¿Deseas vaciar toda la agenda usando 'clear()'? (sí/no): ").lower()
if vaciar_agenda == 'sí':
    agenda.clear()  # Elimina todos los elementos del diccionario
    print("Toda la agenda ha sido vaciada usando 'clear()'.")
else:
    print("La agenda no ha sido vaciada.")

# Mostrar la agenda final
print("\nTu agenda final es:")
for nombre, telefono in agenda.items():
    print(f"{nombre}: {telefono}")

if not agenda:
    print("La agenda está vacía.")