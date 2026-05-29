menu_buffet = ("Ensalada", "Pasta", "Pollo asado", "Sopa", "Pan")

print("Menú original del buffet:")
for comida in menu_buffet:
    print(f"- {comida}")

try:
    menu_buffet[0] = "Pizza"
except TypeError as e:
    print("\nError al intentar modificar la tupla:", e)

menu_buffet = ("Ensalada", "Pasta", "Pizza", "Sushi", "Pan")

print("\nMenú actualizado del buffet:")
for comida in menu_buffet:
    print(f"- {comida}")
