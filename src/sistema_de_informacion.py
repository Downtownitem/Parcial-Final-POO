from turno import Turno
from centro_acopio import CentroAcopio
from typing import List
from datetime import date


class SistemaInformacion:
    def __init__(self):
        self.turnos: List[Turno] = []
        self.centros_acopio: List[CentroAcopio] = []

    def calcular_cantidad_de(self, dia: date, objeto: str) -> float:
        return 0.0
