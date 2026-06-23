### Ejercicio 1: "Control de Saldo - Beca de Alimentación UOH"
La universidad requiere un sistema modular para procesar las compras diarias de la tarjeta de alimentación estudiantil. 

Debes implementar una función llamada `procesar_compras` que cumpla con los siguientes requisitos:
1. **Firma:** `def procesar_compras(saldo_inicial, consumos, descuento_comuna=0.0):`
   - `saldo_inicial` (float): El dinero disponible originalmente en la tarjeta.
   - `consumos` (list): Una lista con los montos (floats) de las compras que el estudiante intentó realizar en el día.
   - `descuento_comuna` (float, opcional): Un porcentaje de descuento que se aplica a **cada consumo individual** si el estudiante reside en una comuna con convenio (ej: `0.10` para un 10% de descuento). Su valor por defecto es `0.0`.
2. **Lógica:**
   - Debe recorrer la lista de consumos.
   - Para cada consumo, aplicar el descuento correspondiente: `monto_con_descuento = consumo * (1 - descuento_comuna)`.
   - Restar este monto descontado del saldo disponible.
   - **Validación crítica:** Si en alguna compra el saldo disponible queda por debajo de $0 (negativo), esa compra **no debe realizarse**. El proceso se debe detener inmediatamente, imprimir el mensaje `"¡Alerta! Saldo insuficiente para realizar la compra de $[monto_con_descuento]. Transacción cancelada."` y no procesar el resto de los consumos.
3. **Retorno:** Debe retornar una tupla con dos valores:
   - El saldo final resultante (float).
   - Un booleano (`True` si se pudieron procesar exitosamente todas las compras de la lista, o `False` si el proceso se interrumpió por saldo insuficiente).
4. **Documentación:** Debe incluir un Docstring completo explicando parámetros y retornos.

#### Plantilla para comenzar:
```python
def procesar_compras(saldo_inicial, consumos, descuento_comuna=0.0):
    """
    Procesa una lista de compras aplicando un descuento y validando el saldo disponible.
    
    Args:
        saldo_inicial (float): Saldo inicial en la tarjeta.
        consumos (list): Lista de montos de consumos a procesar.
        descuento_comuna (float, opcional): Porcentaje de descuento (0.0 a 1.0). Por defecto es 0.0.
        
    Returns:
        tuple: (saldo_final: float, exito_completo: bool)
    """
    # Tu código aquí
    pass
```

<details>
<summary><b>💡 Ver Solución Sugerida</b></summary>

```python
def procesar_compras(saldo_inicial, consumos, descuento_comuna=0.0):
    """
    Procesa una lista de compras aplicando un descuento y validando el saldo disponible.
    
    Args:
        saldo_inicial (float): Saldo inicial en la tarjeta.
        consumos (list): Lista de montos de consumos a procesar.
        descuento_comuna (float, opcional): Porcentaje de descuento (0.0 a 1.0). Por defecto es 0.0.
        
    Returns:
        tuple: (saldo_final: float, exito_completo: bool)
    """
    saldo_actual = saldo_inicial
    
    for consumo in consumos:
        # Aplicamos el descuento al consumo actual
        monto_con_descuento = consumo * (1 - descuento_comuna)
        
        # Validamos si tenemos saldo suficiente para esta transacción
        if saldo_actual - monto_con_descuento < 0:
            print(f"¡Alerta! Saldo insuficiente para realizar la compra de ${monto_con_descuento:.2f}. Transacción cancelada.")
            return saldo_actual, False
            
        # Si hay saldo, restamos el monto y continuamos
        saldo_actual -= monto_con_descuento
        
    return saldo_actual, True

# Ejemplo de prueba:
# saldo, exito = procesar_compras(10000, [3000, 4500, 2000], 0.10)
# print(f"Saldo final: {saldo}, ¿Éxito total?: {exito}")
```
</details>

---

## Recursividad

### Conceptos Clave
- **Caso Base:** Es la condición que detiene la recursión (el estado más simple posible, como una lista vacía o un string vacío) y retorna un valor directo sin hacer otra llamada. **¡Evita bucles infinitos!**
- **Caso Recursivo:** Es donde la función se llama a sí misma, reduciendo el problema a una versión más pequeña (acercándose al caso base).
- **Regla de oro:** No puedes usar `for` ni `while` dentro de funciones recursivas.

### Ejercicio 2.1: "Filtro de Notas Reprobadas" (Recursión en Listas)
En la UOH, se necesita analizar el rendimiento de un curso de forma rápida. Escribe una función recursiva llamada `sumar_reprobados_recursivo(notas)` que reciba una lista de calificaciones (floats entre 1.0 y 7.0) y devuelva la **suma acumulada** de todas las notas que sean menores a 4.0 (reprobadas).

- **Restricciones:** No utilices ciclos (`for`, `while`) ni funciones acumuladoras directas como `sum()` o `filter()`.
- **Caso Base:** Si la lista de notas está vacía, la suma es `0.0`.
- **Caso Recursivo:** Evalúa la primera nota (`notas[0]`):
  - Si es menor a 4.0, súmala al resultado de llamar recursivamente a la función con el resto de la lista (`notas[1:]`).
  - Si es mayor o igual a 4.0, omítela y simplemente retorna el resultado de llamar recursivamente a la función con el resto de la lista (`notas[1:]`).

#### Plantilla para comenzar:
```python
def sumar_reprobados_recursivo(notas):
    # Caso base: ¿qué pasa si la lista está vacía?
    if len(notas) == 0:
        return 0.0
        
    # Caso recursivo: evaluamos el primer elemento y lo reducimos
    nota_actual = notas[0]
    resto_notas = notas[1:]
    
    # Tu lógica aquí...
```

<details>
<summary><b>💡 Ver Solución Sugerida</b></summary>

```python
def sumar_reprobados_recursivo(notas):
    # Caso base: si la lista está vacía, la suma de reprobadas es 0.0
    if not notas:
        return 0.0
        
    # Caso recursivo: tomamos la primera nota y el resto
    nota_actual = notas[0]
    resto_notas = notas[1:]
    
    if nota_actual < 4.0:
        # Si está reprobada, la sumamos y procesamos el resto de la lista
        return nota_actual + sumar_reprobados_recursivo(resto_notas)
    else:
        # Si está aprobada, la ignoramos y procesamos el resto de la lista
        return sumar_reprobados_recursivo(resto_notas)

# Ejemplo de prueba:
# notas_seccion = [5.5, 3.2, 4.0, 2.8, 6.1, 3.9]
# total_reprobado = sumar_reprobados_recursivo(notas_seccion)
# print(f"Suma de notas reprobadas: {total_reprobado:.1f}")  # Debería dar 9.9 (3.2 + 2.8 + 3.9)
```
</details>

### Ejercicio 2.2: "Analizador de Asistencia" (Recursión en Strings)
El registro de asistencia académica de un estudiante se representa con una cadena de texto (string) donde cada caracter indica un estado: `'P'` (Presente), `'A'` (Ausente) y `'J'` (Justificado). Por ejemplo, un registro podría ser `"PPJPAP"`.

Escribe una función recursiva llamada `contar_asistencias(registro, tipo)` que reciba el string del registro y un caracter con el `tipo` de asistencia que se desea contar, y retorne cuántas veces aparece dicho caracter de manera recursiva.

- **Restricciones:** No utilices ciclos ni el método integrado `.count()` de los strings.
- **Caso Base:** Si el registro es un string vacío `""`, la cuenta es `0`.
- **Caso Recursivo:** Extrae el primer caracter y compara si coincide con el `tipo`:
  - Si coincide, suma `1` al resultado de la llamada recursiva con el resto de la cadena.
  - Si no coincide, suma `0` al resultado de la llamada recursiva con el resto de la cadena.

#### Plantilla para comenzar:
```python
def contar_asistencias(registro, tipo):
    # Caso Base: si el string está vacío
    if registro == "":
        return 0
        
    # Caso Recursivo: analizar primer caracter y reducir el string
    primer_dia = registro[0]
    resto_dias = registro[1:]
    
    # Tu lógica aquí...
```

<details>
<summary><b>💡 Ver Solución Sugerida</b></summary>

```python
def contar_asistencias(registro, tipo):
    # Caso Base: si la cadena está vacía, no hay nada que contar
    if not registro:
        return 0
        
    # Caso Recursivo: comparamos la primera posición con el tipo buscado
    primer_dia = registro[0]
    resto_dias = registro[1:]
    
    if primer_dia == tipo:
        # Coincide: sumamos 1 y llamamos recursivamente con el resto
        return 1 + contar_asistencias(resto_dias, tipo)
    else:
        # No coincide: sumamos 0 y llamamos recursivamente con el resto
        return contar_asistencias(resto_dias, tipo)

# Ejemplo de prueba:
# asistencias_estudiante = "PPJPAP"
# presentes = contar_asistencias(asistencias_estudiante, 'P')
# print(f"Total días asistidos (Presente): {presentes}")  # Debería dar 4
```
</details>

---

## Programación Orientada a Objetos (POO)

### Conceptos Clave
- **Clase (Class):** Es la plantilla o plano que define las propiedades (atributos) y comportamientos (métodos) de los objetos que crearemos.
- **Constructor (`__init__`):** El método especial que inicializa el estado del objeto cuando se crea con `nombre_clase(...)`. Siempre lleva el parámetro `self` al principio.
- **Atributos:** Variables asociadas al objeto (ej: `self.nombre`).
- **Métodos:** Funciones internas de la clase que definen lo que el objeto puede hacer. Reciben `self` para acceder a sus propios atributos.
- **Representación Textual (`__str__`):** Método especial que define cómo se verá el objeto si lo imprimimos con `print()`. Debe retornar obligatoriamente un string (`str`).

### Ejercicio 3: "Sistema de Lectura de la Biblioteca Digital UOH"
Para fomentar el hábito de la lectura digital, la biblioteca central de la UOH te pide diseñar una clase en Python para representar el seguimiento de lectura de un libro digital por parte de un usuario.

Debes crear la clase `LibroDigital` con los siguientes requerimientos:

1. **Constructor (`__init__`):**
   - Debe recibir obligatoriamente: `titulo` (str), `autor` (str) y `paginas_totales` (int).
   - Debe inicializar de manera automática e interna los siguientes atributos:
     - `pagina_actual` en `0` (el lector empieza desde la portada).
     - `completado` en `False` (el libro aún no ha sido terminado).

2. **Método `avanzar_lectura(paginas_leidas)`:**
   - Debe recibir la cantidad de páginas leídas (int) en la última sesión de lectura.
   - Si `paginas_leidas` es menor o igual a `0`, debe imprimir `"Error: El número de páginas leídas debe ser un valor positivo."` y no modificar nada.
   - Si es válido, debe sumar las páginas leídas a `pagina_actual`.
   - **Validación de finalización:** Si la nueva `pagina_actual` es mayor o igual a `paginas_totales`, se debe ajustar `pagina_actual` para que sea igual a `paginas_totales`, cambiar el estado `completado` a `True` y mostrar en pantalla: `"¡Felicidades! Completaste la lectura de '[titulo]' de [autor]."`
   - Si el libro no se ha terminado aún, debe imprimir: `"Progreso actualizado de '[titulo]': vas en la página [pagina_actual] de [paginas_totales]."`

3. **Método `reiniciar_lectura()`:**
   - Restablece `pagina_actual` a `0` y `completado` a `False`.
   - Imprime en pantalla: `"Se ha restablecido tu progreso para '[titulo]'. ¡Disfruta tu relectura!"`

4. **Método Especial `__str__`:**
   - Debe retornar una representación en texto del estado del libro según se haya completado o no:
     - Si está completado: `"Libro: [titulo] ([autor]) | Estado: Completado ✓"`
     - Si sigue en lectura: `"Libro: [titulo] ([autor]) | Progreso: [pagina_actual]/[paginas_totales] pág. (Leyendo)"`

#### Plantilla para comenzar:
```python
class LibroDigital:
    def __init__(self, titulo, autor, paginas_totales):
        # Inicialización de atributos
        pass
        
    def avanzar_lectura(self, paginas_leidas):
        # Lógica para avanzar la lectura con validaciones
        pass
        
    def reiniciar_lectura(self):
        # Lógica para reiniciar el progreso
        pass
        
    def __str__(self):
        # Representación en string de la clase
        pass
```

<details>
<summary><b>💡 Ver Solución Sugerida</b></summary>

```python
class LibroDigital:
    def __init__(self, titulo, autor, paginas_totales):
        self.titulo = titulo
        self.autor = autor
        self.paginas_totales = paginas_totales
        self.pagina_actual = 0
        self.completado = False
        
    def avanzar_lectura(self, paginas_leidas):
        # Validación de parámetro de entrada
        if paginas_leidas <= 0:
            print("Error: El número de páginas leídas debe ser un valor positivo.")
            return
            
        # Sumamos el avance
        self.pagina_actual += paginas_leidas
        
        # Validamos si terminó el libro
        if self.pagina_actual >= self.paginas_totales:
            self.pagina_actual = self.paginas_totales
            self.completado = True
            print(f"¡Felicidades! Completaste la lectura de '{self.titulo}' de {self.autor}.")
        else:
            print(f"Progreso actualizado de '{self.titulo}': vas en la página {self.pagina_actual} de {self.paginas_totales}.")
            
    def reiniciar_lectura(self):
        self.pagina_actual = 0
        self.completado = False
        print(f"Se ha restablecido tu progreso para '{self.titulo}'. ¡Disfruta tu relectura!")
        
    def __str__(self):
        if self.completado:
            return f"Libro: {self.titulo} ({self.autor}) | Estado: Completado ✓"
        else:
            return f"Libro: {self.titulo} ({self.autor}) | Progreso: {self.pagina_actual}/{self.paginas_totales} pág. (Leyendo)"

# Ejemplo de prueba de la clase:
# mi_libro = LibroDigital("El Alquimista", "Paulo Coelho", 180)
# print(mi_libro) # Imprime "Libro: El Alquimista (Paulo Coelho) | Progreso: 0/180 pág. (Leyendo)"
# mi_libro.avanzar_lectura(50)
# mi_libro.avanzar_lectura(140) # Esto supera los 180 totales, felicita y marca completado
# print(mi_libro) # Imprime "Libro: El Alquimista (Paulo Coelho) | Estado: Completado ✓"
# mi_libro.reiniciar_lectura()
# print(mi_libro)
```
</details>

---