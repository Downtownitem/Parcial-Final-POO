from datetime import date, time
from camion import Camion
from ruta import Ruta
from factory import Factory
from typing import List
from observer import TurnoObserver
from persona import Persona


class Turno:
    def __init__(
            self,
            id_: int,
            dia: date,
            hora_inicio: time,
            hora_final: time,
            camion: Camion,
            ruta: Ruta,
            factory: Factory,
    ):
        self.id = id_
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_final = hora_final
        self.camion = camion
        self.ruta = ruta
        self.factory = factory
        self.observers: List[TurnoObserver] = []

    def asignar_persona(self, persona: Persona, puesto: str):
        self.camion.asignar_persona(persona, puesto)

    def notificar(self):
        for observer in self.observers:
            observer.update()
