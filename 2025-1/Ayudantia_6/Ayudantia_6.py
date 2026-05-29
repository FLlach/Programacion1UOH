def calcular_promedio(notas: list[float])->float:
    if not notas:
        return 0.0
    return sum(notas) / len(notas)

def estado_alumno(promedio: float, umbral: float=4.0)->bool:
    aprobado: bool=True
    if promedio < umbral:
        aprobado = False
    return aprobado

def procesar_alumnos(alumnos: dict[str,float])->tuple:
    resultado = []
    for alumno in alumnos:
        prom = calcular_promedio(alumno["notas"])
        est = estado_alumno(prom)
        resultado.append((alumno["nombre"], prom, est))
    return tuple(resultado)

def imprimir_reporte(registro: list[tuple])->None:
    for nombre, prom, est in registro:
        print(f"{nombre}: promedio {prom:.2f} — Estado: {"Aprobado" if est == True else "Reprobado"}")

def main()->None:
    alumnos = [
        {"nombre": "Ana",  "notas": [5.5, 6.0, 7.0]},
        {"nombre": "Luis", "notas": [4.0, 3.5, 5.0]},
        {"nombre": "Marta","notas": [2.0, 3.0, 3.5]},
    ]

    registro: str= procesar_alumnos(alumnos)
    imprimir_reporte(registro)

if __name__ == "__main__":
    main()
