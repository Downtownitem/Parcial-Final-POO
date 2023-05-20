from persona import Persona
from typing import Dict


class Camion:
    def __init__(
            self,
            id_: int,
            modelo: str,
            anio: int,
            carga: Dict[str, float],
            desplegar_asistentes: bool,
    ):
        self.id = id_
        self.modelo = modelo
        self.anio = anio
        self.carga = carga
        self.conductor = None
        self.asistente1 = None
        self.asistente2 = None
        self.desplegar_asistentes = desplegar_asistentes

    def asignar_persona(self, persona: Persona, puesto: str):
        if puesto == "conductor":
            self.conductor = persona
        elif puesto == "asistente1":
            self.asistente1 = persona
        elif puesto == "asistente2":
            self.asistente2 = persona
        else:
            raise ValueError("Puesto no válido")
