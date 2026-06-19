# Resumen: Programación Orientada a Objetos (POO)

Este documento resume los contenidos de la Unidad 3 de Programación (ING1312) sobre el paradigma de **Programación Orientada a Objetos (POO)**. Este paradigma permite estructurar el software agrupando el estado (datos) y el comportamiento (funciones) en contenedores llamados **objetos**.

---

## 1. Conceptos Fundamentales

La POO modela problemas del mundo real mediante el uso de objetos que interactúan entre sí.

### Clases y Objetos
*   **Clase (El Molde):** Es una plantilla o definición abstracta que describe cómo debe ser un objeto. Define qué atributos tendrá y qué acciones podrá realizar.
*   **Objeto (La Instancia):** Es la materialización concreta de una clase. Posee valores específicos para los atributos y puede ejecutar las acciones definidas en la clase.

### Atributos y Métodos
*   **Atributos (Estado):** Son variables dentro de la clase que almacenan información sobre el objeto.
*   **Métodos (Comportamiento):** Son funciones definidas dentro de la clase que determinan qué puede hacer el objeto. Siempre reciben como primer parámetro de manera implícita al propio objeto, denominado tradicionalmente `self`.

### El Constructor y `self`
El método especial `__init__` (constructor) se ejecuta automáticamente al instanciar (crear) un objeto. Su propósito principal es inicializar los atributos de la nueva instancia.

```python
class Perro:
    """Clase que representa a un perro mascota."""

    def __init__(self, nombre, raza):
        """
        Constructor de la clase Perro.
        
        :param nombre: Nombre del perro.
        :param raza: Raza del perro.
        """
        self.nombre = nombre  # Atributo de instancia
        self.raza = raza      # Atributo de instancia

    def ladrar(self):
        """Hace que el perro ladre usando su nombre."""
        return f"¡{self.nombre} dice Guau!"

# Instanciación (creación de objetos)
mi_perro = Perro("Boby", "Quiltro")
otro_perro = Perro("Luna", "Golden Retriever")

# Uso de atributos y métodos
print(mi_perro.nombre)    # Salida: Boby
print(otro_perro.ladrar()) # Salida: ¡Luna dice Guau!
```

---

## 2. Encapsulamiento

El **encapsulamiento** consiste en ocultar el estado interno y los detalles de implementación de un objeto, exponiendo únicamente una interfaz segura para interactuar con él. Esto evita modificaciones no autorizadas o accidentales de los datos.

### Niveles de Acceso en Python
A diferencia de otros lenguajes (como Java o C++), Python **no posee modificadores de acceso estrictos** (como `private` o `public`). En su lugar, utiliza convenciones de nomenclatura para indicar la visibilidad:

1.  **Público (`atributo`):** Accesible y modificable desde cualquier lugar del programa.
2.  **Protegido (`_atributo`):** Indica que es para uso interno de la clase y sus subclases. Es una advertencia para los programadores, pero técnicamente sigue siendo accesible.
3.  **Privado (`__atributo`):** Activa el mecanismo de *Name Mangling* (ofuscamiento de nombres). Python renombra internamente el atributo (a `_NombreClase__atributo`) para dificultar su acceso directo desde el exterior.

---

## 3. Herencia

La **herencia** permite crear una nueva clase (llamada **subclase** o clase hija) basándose en una clase existente (llamada **superclase** o clase padre). La subclase hereda automáticamente todos los atributos y métodos de la superclase, facilitando la reutilización del código y el diseño jerárquico.

### Relación "Es Un"
La herencia representa una relación conceptual de tipo **"Es un"**. Por ejemplo: un `Estudiante` **es una** `Persona`, un `Gato` **es un** `Animal`.

### La función `super()`
Se utiliza para invocar constructores o métodos definidos en la superclase, permitiendo extender o especializar el comportamiento en la subclase sin reescribir código.

### Sobreescritura de Métodos (Method Overriding)
Una subclase puede volver a definir un método que ya existe en la superclase para que se ejecute de una manera diferente y más específica.

```python
class Persona:
    """Clase base que representa a una persona general."""

    def __init__(self, nombre, rut):
        self.nombre = nombre
        self.rut = rut

    def presentarse(self):
        """Presentación genérica de una persona."""
        return f"Hola, mi nombre es {self.nombre}."


class Estudiante(Persona):
    """Clase hija que hereda de Persona."""

    def __init__(self, nombre, rut, carrera):
        # Llamamos al constructor de la clase padre (Persona)
        super().__init__(nombre, rut)
        self.carrera = carrera

    def presentarse(self):
        """Sobreescritura del método presentarse para añadir la carrera."""
        # Podemos usar super() para llamar al método del padre e incrementar su comportamiento
        presentacion_base = super().presentarse()
        return f"{presentacion_base} Estudio la carrera de {self.carrera}."

# Ejemplo de uso
persona_comun = Persona("Andrés", "12.345.678-9")
estudiante_uoh = Estudiante("Fernanda", "20.987.654-3", "Ingeniería Civil Civil")

print(persona_comun.presentarse())  # Salida: Hola, mi nombre es Andrés.
print(estudiante_uoh.presentarse()) # Salida: Hola, mi nombre es Fernanda. Estudio la carrera de Ingeniería Civil Civil.
```

---

## 4. Polimorfismo

El **polimorfismo** (del griego *"muchas formas"*) es la capacidad de que objetos de distintas clases respondan al mismo mensaje (método con el mismo nombre) de manera diferente según su propia naturaleza.

### Polimorfismo mediante Herencia
Ocurre cuando múltiples subclases heredan un método de la superclase pero cada una lo sobreescribe para adaptarlo a su propia lógica.

```python
class Animal:
    """Clase base abstracta para animales."""
    def hacer_sonido(self):
        pass  # Se definirá en las subclases

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"

# Una función que recibe un objeto de tipo Animal y ejecuta su sonido
def emitir_sonido_animal(animal):
    print(animal.hacer_sonido())

emitir_sonido_animal(Perro()) # Salida: Guau
emitir_sonido_animal(Gato()) # Salida: Miau
```

### Duck Typing (Tipado de Pato) en Python
Python es un lenguaje de tipado dinámico y utiliza el concepto de **Duck Typing**. La idea principal es:

> *"Si camina como un pato y grazna como un pato, entonces es un pato."*

Esto significa que, para lograr polimorfismo en Python, **no es estrictamente necesario que las clases hereden de la misma superclase**. Basta con que implementen un método con el mismo nombre y firma para que puedan ser tratadas indistintamente en una función.

```python
class Reloj:
    def tic_tac(self):
        return "Tic, Tac, Tic, Tac"

class Corazon:
    def tic_tac(self):
        return "Latiendo a 70 PPM"

# Función polimórfica que no requiere herencia común
def escuchar_ritmo(objeto_con_ritmo):
    # No importa qué clase sea, siempre y cuando tenga el método tic_tac
    print(objeto_con_ritmo.tic_tac())

reloj_mural = Reloj()
mi_corazon = Corazon()

escuchar_ritmo(reloj_mural) # Salida: Tic, Tac, Tic, Tac
escuchar_ritmo(mi_corazon)  # Salida: Latiendo a 70 PPM
```

---

## 5. Argumentos Variables: `*args` en Funciones

El parámetro especial `*args` permite que una función reciba una cantidad arbitraria de argumentos posicionales, los cuales son empaquetados dentro de una **tupla** internamente.

### Ejemplo
```python
def sumar(*numeros):
    return sum(numeros)

print(sumar(1, 2, 3)) # Salida: 6
```

### Ejercicios Propuestos (`*args`)

1. **Calculadora de Promedios:** Crea una función `calcular_promedio(*numeros)` que reciba cualquier cantidad de números y retorne su promedio. Si no se pasan argumentos, debe retornar 0 para evitar división por cero.
2. **Concatenador de Strings:** Crea una función `unir_palabras(*palabras)` que reciba una cantidad variable de palabras y las retorne unidas en una sola cadena, separadas por un espacio.
3. **Filtro de Mayores:** Crea una función `filtrar_mayores(limite, *numeros)` que reciba un número límite y una cantidad variable de números, y retorne una lista con los números que son mayores al límite.


### Ejercicio 1: Sistema de Notificaciones (POO Básica e Herencia)
Diseña una jerarquía de clases para simular el envío de notificaciones en un sistema digital.

1.  Crea una clase base llamada `Notificacion` que tenga:
    *   Un constructor `__init__` que inicialice el atributo de instancia `destinatario` (un string).
    *   Un método llamado `enviar(self)` que simplemente retorne un string genérico, por ejemplo: `"Enviando notificación general..."`.
2.  Crea una subclase llamada `NotificacionEmail` que herede de `Notificacion` y añada:
    *   Un atributo específico `asunto` (un string).
    *   Uso de `super()` en su constructor para inicializar el `destinatario`.
    *   Sobreescritura del método `enviar(self)` para que retorne: `"Enviando correo a [destinatario] con el asunto '[asunto]'."`
3.  Crea otra subclase llamada `NotificacionSMS` que herede de `Notificacion` y añada:
    *   Un atributo específico `numero_telefono` (un string).
    *   Uso de `super()` en su constructor.
    *   Sobreescritura del método `enviar(self)` para que retorne: `"Enviando SMS al número [numero_telefono] para [destinatario] con un código de verificación."`
4.  Escribe un script de prueba que cree una lista con instancias de ambos tipos de notificaciones y recorra la lista ejecutando el método `enviar()` de cada una, mostrando el resultado en consola (demostrando polimorfismo).

---

### Ejercicio 2: Liquidación de Sueldos
Una empresa local requiere un software para calcular de forma automatizada las liquidaciones mensuales de sus empleados según su tipo de contrato.

1.  Crea la clase base `Empleado` con:
    *   Atributos: `nombre`, `rut` y `salario_base`.
    *   Un método `calcular_sueldo(self)` que por defecto retorne el `salario_base`.
2.  Crea la subclase `EmpleadoTiempoCompleto` que herede de `Empleado` y añada:
    *   Atributo específico: `bono_mensual` (un valor float).
    *   Sobreescribe `calcular_sueldo(self)` utilizando `super()` para obtener el sueldo base y sumarle el bono mensual.
3.  Crea la subclase `EmpleadoPorHora` que herede de `Empleado` e ignore el `salario_base` (puedes pasarle `0` en el `super()`):
    *   Atributos específicos: `horas_trabajadas` (un entero) y `valor_hora` (un float).
    *   Sobreescribe `calcular_sueldo(self)` para calcular el salario multiplicando las horas trabajadas por el valor de cada hora.
4.  Crea una función externa al entorno de las clases llamada `mostrar_liquidacion(empleado)` que reciba un objeto `Empleado` (o cualquiera de sus subclases) e imprima una ficha formateada con el nombre, rut y el sueldo final calculado con `calcular_sueldo()`. Prueba esta función con instancias de ambas subclases.

---

### Ejercicio 3: Batalla de RPG
Para un videojuego de rol (RPG), se requiere un sistema dinámico que permita procesar el turno de combate de múltiples personajes con acciones distintas sin necesidad de usar una estructura jerárquica de herencia rígida.

1.  Crea la clase `Guerrero` con:
    *   Atributo `nombre`.
    *   Método `ejecutar_accion(self, objetivo)` que retorne el string: `"[Guerrero] [nombre] ataca con espada a [objetivo] causando daño físico."`
2.  Crea la clase `Mago` con:
    *   Atributo `nombre`.
    *   Método `ejecutar_accion(self, objetivo)` que retorne el string: `"[Mago] [nombre] lanza un hechizo de fuego a [objetivo] causando daño mágico."`
3.  Crea la clase `Curandero` con:
    *   Atributo `nombre`.
    *   Método `ejecutar_accion(self, objetivo)` que retorne el string: `"[Curandero] [nombre] canaliza energía divina para curar las heridas de [objetivo]."`
4.  Define una función externa llamada `ejecutar_turno(personajes, objetivo)` que reciba una lista con instancias mezcladas de estas tres clases (que no comparten ninguna clase padre común) y un string `objetivo`. La función debe iterar sobre la lista de personajes y llamar al método `ejecutar_accion(self, objetivo)` de cada uno, imprimiendo el resultado en consola.