def invertir_texto(texto):
    if len(texto) <= 1:
        return texto
    return texto[-1] + invertir_texto(texto[:-1])

def invertir_palabras(texto):
    lineas = texto.split('\n')
    lineas_invertidas = []

    for linea in lineas:
        palabras = linea.split()
        palabras_invertidas = palabras[::-1]
        linea_invertida = ' '.join(palabras_invertidas)
        lineas_invertidas.append(linea_invertida)

    return '\n'.join(lineas_invertidas)

def invertir_archivo(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()

    contenido_invertido = invertir_texto(contenido)
    with open('invertido_caracteres.txt', 'w', encoding='utf-8') as archivo_salida:
        archivo_salida.write(contenido_invertido)

    contenido_palabras = invertir_palabras(contenido)
    with open('invertido_palabras.txt', 'w', encoding='utf-8') as archivo_salida2:
        archivo_salida2.write(contenido_palabras)

    print("Archivos generados:")
    print("- invertido_caracteres.txt")
    print("- invertido_palabras.txt")
    

# Ejecución principal
nombre_archivo = "prueba.txt"
invertir_archivo(nombre_archivo)
