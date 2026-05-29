# Clase base
class Figura:
    def __init__(self, nombre):
        self._nombre = nombre  # Encapsulamiento con atributo privado

    def get_nombre(self):
        return self._nombre

    def area(self):
        return 0  # Método genérico a ser sobrescrito


# Subclase Rectángulo
class Rectangulo(Figura):
    def __init__(self, nombre, base, altura):
        super().__init__(nombre)
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


# Subclase Círculo
class Circulo(Figura):
    def __init__(self, nombre, radio):
        super().__init__(nombre)
        self.radio = radio

    def area(self):
        return 3.1416 * self.radio * self.radio


# Función que demuestra polimorfismo
def mostrar_areas(lista_figuras):
    for figura in lista_figuras:
        print(f"{figura.get_nombre()}: Área = {figura.area()}")


# Ejemplo de uso
figuras = [
    Rectangulo("Rectángulo", 3, 4),
    Circulo("Círculo", 2)
]

mostrar_areas(figuras)
