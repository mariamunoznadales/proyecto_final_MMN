from datetime import time
from empleado import Empleado

class Horario:
    def __init__(self):
        self.dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        self.turnos_predefinidos = self._crear_turnos()

    def _crear_turnos(self):
        # Crear instancias de empleados
        empleado_1 = Empleado("Victoria", 101)
        empleado_2 = Empleado("Pedro", 102)
        empleado_3 = Empleado("Juan", 103)
        empleado_4 = Empleado("Ana", 104)
        jefe = Empleado("Maria", 999, es_jefe=True)

        self.empleados = [empleado_1, empleado_2, empleado_3, empleado_4, jefe]

        # Turnos predefinidos usando objetos time
        return {
            "Lunes": {
                empleado_1: (time(0, 0), time(6, 0)),
                empleado_2: (time(6, 0), time(12, 0)),
                empleado_3: (time(12, 0), time(18, 0)),
                empleado_4: (time(18, 0), time(23, 59)),
            },
            "Martes": {
                empleado_1: (time(6, 0), time(12, 0)),
                empleado_2: (time(12, 0), time(18, 0)),
                empleado_3: (time(18, 0), time(23, 59)),
                empleado_4: (time(0, 0), time(6, 0)),
            },
            "Miércoles": {
                empleado_1: (time(12, 0), time(18, 0)),
                empleado_2: (time(18, 0), time(23, 59)),
                empleado_3: (time(0, 0), time(6, 0)),
                empleado_4: (time(6, 0), time(12, 0)),
            },
            "Jueves": {
                empleado_1: (time(18, 0), time(23, 59)),
                empleado_2: (time(0, 0), time(6, 0)),
                empleado_3: (time(6, 0), time(12, 0)),
                empleado_4: (time(12, 0), time(18, 0)),
            },
            "Viernes": {
                empleado_1: (time(0, 0), time(6, 0)),
                empleado_2: (time(6, 0), time(12, 0)),
                empleado_3: (time(12, 0), time(18, 0)),
                empleado_4: (time(18, 0), time(23, 59)),
            },
            "Sábado": {
                empleado_1: (time(6, 0), time(12, 0)),
                empleado_2: (time(12, 0), time(18, 0)),
                empleado_3: (time(18, 0), time(23, 59)),
                empleado_4: (time(0, 0), time(6, 0)),
            },
            "Domingo": {
                empleado_1: (time(12, 0), time(18, 0)),
                empleado_2: (time(18, 0), time(23, 59)),
                empleado_3: (time(0, 0), time(6, 0)),
                empleado_4: (time(6, 0), time(12, 0)),
            },
        }

    def buscar_empleado(self, nombre, id):
        for empleado in self.empleados:
            if empleado.nombre == nombre and empleado.id == id:
                return empleado
        return None
