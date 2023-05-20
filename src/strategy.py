from typing import List
from punto_geografico import PuntoGeografico


class RutaStrategy:
    def calcular_ruta(self) -> List[PuntoGeografico]:
        pass


class RutaEstrategiaA(RutaStrategy):
    def calcular_ruta(self) -> List[PuntoGeografico]:
        return []


class RutaEstrategiaB(RutaStrategy):
    def calcular_ruta(self) -> List[PuntoGeografico]:
        return []
