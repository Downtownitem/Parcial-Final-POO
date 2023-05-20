from strategy import RutaStrategy


class Ruta:
    def __init__(self, id_: str, estrategia: RutaStrategy):
        self.id = id_
        self.puntos = []
        self.estrategia = estrategia

    def calcular_ruta(self):
        self.puntos = self.estrategia.calcular_ruta()
