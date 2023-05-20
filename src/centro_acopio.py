from punto_geografico import PuntoGeografico
from persona import Persona


class CentroAcopio:
    def __init__(self, id_: int, ubicacion: PuntoGeografico):
        self.id = id_
        self.ubicacion = ubicacion
        self.id_camion_actual = None

    def asignar_persona(self, persona: Persona, puesto: str):
        pass
