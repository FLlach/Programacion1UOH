# Ejercicio: Sistema de Gestión de la Cafetería "UOH Coffee"

## Contexto
Has sido contratado para desarrollar el sistema de gestión de la nueva cafetería universitaria **"UOH Coffee"**. El objetivo es automatizar el control del menú, la toma de pedidos y la generación de reportes diarios.

---

## Requerimientos Técnicos

### 1. Estructuras de Datos
El sistema debe gestionar la información utilizando:
- **Diccionario:** Para el menú, donde la *llave* es el nombre del producto y el *valor* es una lista con su categoría, precio base y stock disponible.
- **Lista:** Para registrar las ventas realizadas en el día (cada venta puede ser una tupla).
- **Set (Conjunto):** Para almacenar las categorías únicas de productos que se ofrecen (ej: "Bebida Caliente", "Sandwich", "Pastelería").
- **Tupla:** Para representar cada pedido registrado: `(nombre_producto, cantidad, total_pagado)`.

### 2. Funciones y Modularización
Debes implementar funciones que cumplan con:
- **Docstrings:** Documentación completa de cada función.
- **Retorno de valores:** Casi todas las funciones deben devolver un resultado.
- **Parámetros por defecto:** Al menos una función debe tener un parámetro opcional (por ejemplo, un recargo por envase biodegradable o un descuento por ser estudiante).
- **Manejo de Scope:** Diferenciar correctamente entre variables globales (como el menú) y locales dentro de las funciones.

### 3. Lógica y Control de Flujo
- **Menú de Usuario:** Un ciclo `while` infinito que se rompa solo cuando el usuario decida salir.
- **Validaciones:** Uso de `if-elif-else` para verificar si un producto existe en el menú y si hay stock suficiente.
- **Procesamiento:** Ciclos `for` para mostrar el menú formateado y calcular estadísticas finales.
- **Biblioteca Estándar:** Utilizar el módulo `random` para generar un "Código de Descuento Aleatorio" al final de cada compra (ej: un número entre 1000 y 9999).

---

## Funcionalidades Esperadas
1. **Mostrar Menú:** Listar todos los productos, sus precios y categorías.
2. **Realizar Pedido:** 
   - Solicitar el nombre del producto y la cantidad.
   - Verificar stock.
   - Calcular el total (Cantidad x Precio).
   - Aplicar un descuento opcional (usar parámetro por defecto).
   - Actualizar el stock en el diccionario.
   - Guardar el pedido en la lista de ventas como una tupla.
3. **Agregar/Actualizar Producto:** Permitir al administrador añadir nuevos productos o reponer stock. Se debe actualizar el Set de categorías automáticamente.
4. **Reporte de Ventas:** Mostrar el total de dinero recaudado y el producto más vendido.
5. **Generar Cupón:** Al finalizar una compra, imprimir un código aleatorio para la siguiente visita.
6. **Salir:** Mostrar un mensaje de despedida y cerrar el programa.
