class Empleado:
    """Clase base para empleados."""
    def __init__(self, nombre: str, rut: str, salario_base: float):
        self.nombre = nombre
        self.rut = rut
        self.salario_base = salario_base

    def calcular_sueldo(self) -> float:
        return self.salario_base

class EmpleadoTiempoCompleto(Empleado):
    """Subclase para empleados a tiempo completo."""
    def __init__(self, nombre: str, rut: str, salario_base: float, bono_mensual: float):
        super().__init__(nombre, rut, salario_base)
        self.bono_mensual = bono_mensual

    def calcular_sueldo(self) -> float:
        return super().calcular_sueldo() + self.bono_mensual

class EmpleadoPorHora(Empleado):
    """Subclase para empleados por hora."""
    def __init__(self, nombre: str, rut: str, horas_trabajadas: int, valor_hora: float):
        super().__init__(nombre, rut, 0)
        self.horas_trabajadas = horas_trabajadas
        self.valor_hora = valor_hora

    def calcular_sueldo(self) -> float:
        return self.horas_trabajadas * self.valor_hora

def mostrar_liquidacion(empleado: Empleado):
    """Función para mostrar la liquidación de un empleado."""
    sueldo_final = empleado.calcular_sueldo()
    print(f"Empleado: {empleado.nombre} | RUT: {empleado.rut} | Sueldo Final: ${sueldo_final:,.0f}")

# Script de prueba
if __name__ == "__main__":
    emp1 = EmpleadoTiempoCompleto("Juan Perez", "11.111.111-1", 500000, 100000)
    emp2 = EmpleadoPorHora("Maria Lopez", "22.222.222-2", 40, 5000)
    
    mostrar_liquidacion(emp1)
    mostrar_liquidacion(emp2)
