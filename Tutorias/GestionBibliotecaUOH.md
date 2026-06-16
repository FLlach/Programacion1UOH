# Sistema de Gestión de Biblioteca

## Contexto
La Universidad de O'Higgins requiere un sistema para automatizar el préstamo de libros en su biblioteca central. El sistema debe permitir administrar el catálogo, realizar préstamos a estudiantes y llevar un control riguroso de la cantidad de libros solicitados por persona.

---

## Requerimientos Técnicos

### 1. Estructuras de Datos
El sistema debe utilizar las siguientes estructuras:
- **Diccionario:** Para el catálogo de libros, donde la *llave* es el título del libro y el *valor* es una lista que contiene [Autor, Género, Cantidad disponible].
- **Lista:** Para registrar los nombres de los libros que han sido prestados en la sesión actual.
- **Set (Conjunto):** Para almacenar los géneros literarios únicos presentes en la biblioteca.

### 2. Funciones
Debes implementar funciones que cumplan con:
- **Docstrings:** Explicación clara de qué hace la función, sus parámetros y su retorno.
- **Retorno de valores:** Las funciones deben devolver resultados (por ejemplo, un booleano indicando si el préstamo fue exitoso).
- **Parámetros por defecto:** Implementar al menos una función con un parámetro opcional (ej: el plazo de entrega en días).

### 3. Lógica y Control de Flujo
- **Ciclo While con Contador:** Para la funcionalidad de "Préstamo Express", debes usar un ciclo `while` junto con un **contador**. El sistema debe permitir a un estudiante pedir libros uno por uno hasta un máximo de 3 libros. El ciclo debe terminar cuando se alcance el límite o el usuario decida no pedir más.
- **Ciclo For:** Para recorrer el catálogo y mostrar solo los libros que pertenecen a un género específico o que tienen stock disponible.
- **Validaciones:** Uso de `if-elif-else` para verificar la existencia de libros y la disponibilidad de ejemplares.

---

## Funcionalidades Esperadas
1. **Mostrar Catálogo:** Listar todos los libros, sus autores y el stock disponible.
2. **Préstamo Express:** 
   - Solicitar el nombre del estudiante.
   - Utilizar un **contador** inicializado en 0.
   - Mientras el contador sea menor a 3, preguntar si desea pedir un libro.
   - Validar stock y actualizar el diccionario si el préstamo se concreta.
   - Incrementar el contador con cada préstamo exitoso.
3. **Agregar Nuevo Libro:** Permitir al bibliotecario ingresar nuevos títulos, asegurando que el Set de géneros se actualice automáticamente.
4. **Reporte de Sesión:** Al salir del programa, mostrar el total de libros prestados y la lista de títulos que salieron de la biblioteca.
5. **Salir:** Finalizar la ejecución del programa.
