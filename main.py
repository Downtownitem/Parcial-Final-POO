from datetime import date, time
from typing import Dict, List, Union


class PuntoGeografico:
    def __init__(self, latitud: float, longitud: float):
        self.latitud = latitud
        self.longitud = longitud


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


class RutaStrategy:
    def calcular_ruta(self) -> List[PuntoGeografico]:
        pass


class RutaEstrategiaA(RutaStrategy):
    def calcular_ruta(self) -> List[PuntoGeografico]:
        return []


class RutaEstrategiaB(RutaStrategy):
    def calcular_ruta(self) -> List[PuntoGeografico]:
        return []


class Ruta:
    def __init__(self, id_: str, estrategia: RutaStrategy):
        self.id = id_
        self.puntos = []
        self.estrategia = estrategia

    def calcular_ruta(self):
        self.puntos = self.estrategia.calcular_ruta()


class CentroAcopio:
    def __init__(self, id_: int, ubicacion: PuntoGeografico):
        self.id = id_
        self.ubicacion = ubicacion
        self.id_camion_actual = None

    def asignar_persona(self, persona: Persona, puesto: str):
        pass


class TurnoObserver:
    def update(self):
        pass


class Observer(TurnoObserver):
    def update(self):
        pass


class Factory:
    def create_conductor(self) -> Conductor:
        pass

    def create_asistente(self) -> Asistente:
        pass


class TrashCityFactory(Factory):
    def create_conductor(self) -> Conductor:
        return Conductor(1, "Juan", "Perez", "123456", "A1234")

    def create_asistente(self) -> Asistente:
        return Asistente(2, "Maria", "Lopez", "789012", 1)


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


class SistemaInformacion:
    def __init__(self):
        self.turnos: List[Turno] = []
        self.centros_acopio: List[CentroAcopio] = []

    def calcular_cantidad_de(self, dia: date, objeto: str) -> float:
        return 0.0


def main():
    sistema = SistemaInformacion()

    factory = TrashCityFactory()
    conductor = factory.create_conductor()
    asistente = factory.create_asistente()

    camion = Camion(1, "ABC123", 2010, {"vidrio": 0.0, "papel": 0.0}, True)
    camion.asignar_persona(conductor, "conductor")
    camion.asignar_persona(asistente, "asistente1")

    ruta_estrategia = RutaEstrategiaA()
    ruta = Ruta("TestRuta", ruta_estrategia)
    ruta.calcular_ruta()

    ubicacion_acopio = PuntoGeografico(10.0, 20.0)
    acopio = CentroAcopio(1, ubicacion_acopio)

    turno = Turno(1, date.today(), time(8), time(17), camion, ruta, factory)

    sistema.turnos.append(turno)
    sistema.centros_acopio.append(acopio)

    while True:
        print("Seleccione una opción:")
        print("1: Calcular cantidad de un objeto en un día específico")
        print("2: Salir")
        opcion = int(input("Opción: "))

        if opcion == 1:
            dia_str = input("Ingrese la fecha en formato YYYY-MM-DD: ")
            dia = date.fromisoformat(dia_str)
            objeto = input("Ingrese el tipo de objeto: ")
            cantidad = sistema.calcular_cantidad_de(dia, objeto)
            print(f"La cantidad de {objeto} en {dia_str} es: {cantidad}")
        elif opcion == 2:
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()
