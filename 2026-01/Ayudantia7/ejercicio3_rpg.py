class Guerrero:
    def __init__(self, nombre: str):
        self.nombre = nombre
    
    def ejecutar_accion(self, objetivo: str) -> str:
        return f"[Guerrero] {self.nombre} ataca con espada a {objetivo} causando daño físico."

class Mago:
    def __init__(self, nombre: str):
        self.nombre = nombre
    
    def ejecutar_accion(self, objetivo: str) -> str:
        return f"[Mago] {self.nombre} lanza un hechizo de fuego a {objetivo} causando daño mágico."

class Curandero:
    def __init__(self, nombre: str):
        self.nombre = nombre
    
    def ejecutar_accion(self, objetivo: str) -> str:
        return f"[Curandero] {self.nombre} canaliza energía divina para curar las heridas de {objetivo}."

def ejecutar_turno(personajes: list, objetivo: str):
    """Ejecuta el turno de personajes usando Duck Typing."""
    for p in personajes:
        # Duck Typing: no importa la clase, solo que tenga el método ejecutar_accion
        print(p.ejecutar_accion(objetivo))

# Script de prueba
if __name__ == "__main__":
    equipo = [
        Guerrero("Conan"),
        Mago("Merlin"),
        Curandero("Gandalf")
    ]
    
    ejecutar_turno(equipo, "Monstruo")