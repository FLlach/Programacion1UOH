# Ejercicio: Sistema de Gestión del Festival de Cine UOH

## Contexto
La universidad te ha encargado desarrollar un sistema para gestionar el primer **"Festival de Cine UOH"**. El programa debe permitir administrar la cartelera, vender entradas y generar estadísticas simples sobre los asistentes y géneros disponibles.

---

## Requerimientos Técnicos

### 1. Estructuras de Datos
El sistema debe utilizar obligatoriamente las siguientes estructuras:
- **Diccionario:** Para almacenar la cartelera donde la *llave* es el título de la película y el *valor* es una lista con su género, ubicación y precio.
- **Lista:** Para registrar cronológicamente los nombres de los asistentes que compran entradas.
- **Set (Conjunto):** Para mantener un registro de los géneros únicos disponibles (sin duplicados).
- **Tupla:** Para almacenar la ubicación fija (Sala, Horario) de cada película dentro del diccionario.

### 2. Funciones
Debes implementar al menos las siguientes funciones:
- Todas las funciones deben incluir **Docstrings** (documentación técnica).
- Deben recibir argumentos y retornar valores.
- Al menos una función debe utilizar un **parámetro por defecto** (por ejemplo, para aplicar un descuento estándar).

### 3. Flujo de Control y Lógica
- **Menú Principal:** Implementar un ciclo `while` que mantenga el programa ejecutándose hasta que el usuario decida salir.
- **Condicionales:** Usar `if-elif-else` para procesar las opciones del menú.
- **Ciclos For:** Para recorrer el diccionario de la cartelera y el set de géneros al mostrarlos en pantalla.
- **Casteo de Datos:** Asegurar que las entradas del usuario (`input`) sean convertidas al tipo de dato correcto (`int`, `float`) antes de realizar operaciones.
- **Operaciones Matemáticas:** Calcular totales de venta, descuentos y estadísticas.

---

## Funcionalidades Esperadas
1. **Agregar Película:** Solicitar datos al usuario y guardarlos en las estructuras correspondientes.
2. **Ver Cartelera:** Listar todas las películas con su sala, horario y precio.
3. **Comprar Entradas:** 
   - Buscar una película por nombre.
   - Calcular el precio total (Cantidad × Precio).
   - Aplicar un descuento (por defecto 10%, o 20% si la compra es grupal).
   - Registrar al asistente.
4. **Ver Géneros:** Mostrar los géneros únicos que hay en el festival.
5. **Estadísticas al Salir:** Mostrar cuántas personas asistieron en total antes de cerrar el programa.
