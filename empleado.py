
class Empleado:
    def __init__(self, nombre, id, es_jefe=False):
        self._nombre = nombre
        self._id = id
        self._es_jefe = es_jefe

    @property
    def nombre(self):
        return self._nombre

    @property
    def id(self):
        return self._id

    @property
    def es_jefe(self):
        return self._es_jefe
