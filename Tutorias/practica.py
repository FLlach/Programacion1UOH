import random 

string ="felipe"
def saludo(nombre):
    string=f"Hola {nombre}, como estás?"
    return string

#saludoespecial= saludo("felipe")
#print(saludoespecial)
#print(string)

a = "Hola"*5
print(a) #"HolaHolaHolaHolaHola"
indice=a.find("a",3) # 3
"""
string.find(substring, start, end) busca el substring
y retorna la psoición donde se encontró el substring
"""
print(indice) #3 porque es donde se encuentra la primera "a"

nuevoString="   ¡¡Soy un string de prueba!!    "
print(nuevoString.lstrip()) #Elimina los caracteres de la izquierda del string
print(nuevoString.rstrip()) #Elimina los caracteres de la derecha del string
print(nuevoString.strip()) #Elimina los caracteres de la izquierda y la derecha del string
