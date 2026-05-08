# Ejercicio de Práctica: Gestión de Competencia de Atletismo

Una liga de atletismo necesita un programa en Python para registrar y clasificar los resultados de una carrera de 100 metros planos.

## Requerimientos del Programa

1. **Inicialización**:
   - Crea dos listas vacías: una para los nombres de los atletas y otra para sus tiempos.

2. **Registro de Atletas**:
   - Pregunta al usuario cuántos atletas desea registrar.
   - Utiliza un ciclo 'for' con 'range' para solicitar el nombre de cada atleta y agregarlo a la lista de nombres.

3. **Ingreso de Tiempos**:
   - Para cada atleta en la lista, solicita su tiempo de carrera.
   - Debes usar un ciclo 'while' para validar que el tiempo sea un número mayor a 0. Si el usuario ingresa un valor inválido, el programa debe insistir hasta que se ingrese un tiempo correcto.
   - Agrega el tiempo validado a la lista de tiempos.

4. **Clasificación y Resultados**:
   - Recorre las listas y muestra el nombre, el tiempo y la categoría de cada atleta siguiendo estas reglas:
     - **Elite**: Tiempo menor a 10.5 segundos.
     - **Promedio**: Tiempo entre 10.5 y 12.5 segundos (inclusive).
     - **Principiante**: Tiempo mayor a 12.5 segundos.

5. **Búsqueda Final**:
   - Al finalizar la clasificación, permite que el usuario ingrese el nombre de un atleta para buscar su información específica.
   - Si el atleta existe, muestra sus datos. Si no, muestra un mensaje indicando que no fue encontrado.

---
**Conceptos a practicar:**
- Listas (operaciones 'append', búsqueda).
- Ciclos 'for' con 'range'.
- Ciclos 'while' para validación.
- Estructuras condicionales anidadas o múltiples.
