# Resumen: Librería Turtle y Recursividad

Este documento resume los contenidos de la Unidad 2 de Programación (ING1312) sobre la librería Turtle y la técnica de Recursividad.

---

## 1. Librería Turtle

Turtle es una librería gráfica de Python que permite dibujar trazando líneas en un espacio 2D.

### Importar la Librería
Existen varias formas de importar la librería:

```python
# Opción 1: Estándar
import turtle
crush = turtle.Turtle()
turtle.done()

# Opción 2: Con alias
import turtle as ttl
crush = ttl.Turtle()
ttl.done()

# Opción 3: Importar todo (menos recomendado)
from turtle import *
crush = Turtle()
done()
```

### Movimiento y Rotación
La tortuga comienza en la posición `(0, 0)` apuntando hacia la derecha.

*   `forward(distancia)` o `fd(distancia)`: Mover hacia adelante.
*   `backward(distancia)` o `bk(distancia)`: Mover hacia atrás.
*   `right(grados)` o `rt(grados)`: Girar a la derecha.
*   `left(grados)` o `lt(grados)`: Girar a la izquierda.

### Control del Lápiz y Color
*   `pencolor("color")`: Cambia el color del trazo (ej: "blue", "red").
*   `penup()`: Levanta el lápiz (deja de dibujar al moverse).
*   `pendown()`: Baja el lápiz (vuelve a dibujar).

### Coordenadas y Módulo Math
*   `goto(x, y)`: Envía la tortuga a un punto específico.
*   `setworldcoordinates(llx, lly, urx, ury)`: Configura el sistema de coordenadas.
*   Se puede integrar con el módulo `math` para usar constantes como `math.pi` y funciones como `math.sin()`.

---

## 2. Recursividad

La recursividad es una técnica de programación fundamentada en la inducción matemática. Una función es recursiva cuando se define en términos de sí misma.

### Componentes Esenciales
1.  **Caso Base:** Un caso cuya resolución es inmediata. Evita que la recursión sea infinita.
2.  **Regla Inductiva:** Define la solución para el caso actual basándose en una llamada a la misma función con un problema de menor escala.

### Ejemplos Clásicos

#### Potencia ($a^n$)
*   **Caso base:** Si $n = 0$, retorna 1.
*   **Regla inductiva:** Si $n > 0$, retorna $a \cdot \text{potencia}(a, n-1)$.

#### Cuenta Atrás
*   **Caso base:** Si $a = 0$, no hace nada.
*   **Regla inductiva:** Si $a > 0$, imprime $a$ y llama a `cuentaAtras(a - 1)`.

### Manejo de Listas Recursivas
Es útil ver las listas como la unión de:
*   **Cabeza (`lista[0]`):** El primer elemento.
*   **Cola (`lista[1:]`):** El resto de la lista.

#### Ejemplo: Calcular el Máximo
*   **Caso base:** Si la lista tiene un elemento, ese es el máximo.
*   **Regla inductiva:** El máximo es el mayor valor entre la **cabeza** y el **máximo de la cola**.

#### Ejemplo: Método Mapear (Map)
Aplica una función a cada elemento de una lista de forma recursiva.
*   **Caso base:** El "map" de una lista vacía es `[]`.
*   **Regla inductiva:** Concatena el resultado de aplicar la función a la cabeza con el "mapeado" de la cola.

---

## 3. Problemas y Ejercicios Propuestos

El documento incluye varios problemas para practicar:
1.  **Ordenamiento de código:** Organizar líneas de Turtle para dibujar una estrella.
2.  **String Inverso:** Generar un string de $n$ a 1.
3.  **Factorial:** Calcular $n!$ recursivamente.
4.  **Sumatoria de Lista:** Sumar elementos de una lista sin bucles.
5.  **Fibonacci:** Generar los primeros $n$ números de la serie.
6.  **Cuadrados de una Lista:** Retornar una lista con los cuadrados de los elementos originales.
7.  **Seguimiento de código:** Analizar qué retorna una función de suma acumulada.
8.  **Multiplicación por Sumas:** Implementar `repetir(a, b)` como suma recursiva.
9.  **Patrón Numérico:** Imprimir una pirámide de números.
10. **Transformación de Strings:** Analizar una función que reemplaza caracteres por 'z'.
11. **Invertir Palabra:** Función recursiva para dar vuelta un string.
12. **Suma Condicional:** Convertir un bucle `while` que suma múltiplos de 3 en una función recursiva.
13. **Palíndromos:** Función `es_palindromo` para verificar si una palabra se lee igual en ambos sentidos.
