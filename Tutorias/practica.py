import random 

string ="felipe"
def saludo(nombre):
    string=f"Hola {nombre}, como estás?"
    return string

saludoespecial= saludo("felipe")
print(saludoespecial)
print(string)

print(random.randint(0,10))
help(random.randint)