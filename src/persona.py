class Persona:
    def __init__(self, id_: int, nombre: str, apellido: str, cedula: str):
        self.id = id_
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula


class Conductor(Persona):
    def __init__(self, id_: int, nombre: str, apellido: str, cedula: str, licencia: str):
        super().__init__(id_, nombre, apellido, cedula)
        self.licencia = licencia

    def conducir(self, camion):
        pass


class Asistente(Persona):
    def __init__(self, id_: int, nombre: str, apellido: str, cedula: str, num_identificacion: int):
        super().__init__(id_, nombre, apellido, cedula)
        self.num_identificacion = num_identificacion
